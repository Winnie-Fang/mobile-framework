import platform
import re
import subprocess
import sys

from appium import webdriver
from appium.options.common import AppiumOptions
from huskypo import Appium, Log, logstack

# from module.ios.native_appid import IOS_CUBE
from module.mobile.globalvar import GlobalVar
from framework import global_adapter


class DeviceManager:
    STATIC_IOS_DRIVER = None
    Log.PRINT = True
    Log.RECORD = True
    KEEP_APP_STATE = True
    STATIC_DRIVER = None

    @classmethod
    def adb_executor(cls, adb_commands: list) -> subprocess.CompletedProcess:
        """
        執行ADB命令並返回結果。

        參數:
        adb_commands (list): 要執行的ADB命令列表

        返回:
        subprocess.CompletedProcess: 包含命令執行結果的對象

        異常:
        subprocess.CalledProcessError: 當 ADB 命令執行失敗時拋出
        Exception: 當發生其他未預期的錯誤時拋出
        """

        try:
            return subprocess.run(
                adb_commands,
                shell=cls.is_windows(),
                check=True,
                capture_output=True,
                text=True
            )

        except subprocess.CalledProcessError as e:
            print(f"Error clearing UIAutomator2 server data: {e}")
            raise
        except Exception as e:
            logstack.error(f"Unexpected error: {e}")
            raise

    @classmethod
    def android_device_name(cls) -> bool:
        """
        獲取連接的 Android 型號
        例：pixel 7a
        """

        return cls.adb_executor(['adb', 'shell', 'getprop', 'ro.product.model']).stdout.strip()

    @classmethod
    def android_device_serial_number(cls):
        """
        獲取連接的 Android 設備的序列號（udid）

        返回:
        str: Android 設備的序列號
        """
        logstack.info(cls.adb_executor(['adb', 'get-serialno']).stdout.strip())
        return cls.adb_executor(['adb', 'get-serialno']).stdout.strip()

    @classmethod
    def is_windows(cls) -> bool:
        """
        判斷當前操作系統是否為 Windows。

        返回:
        bool: 如果是 Windows 返回 True，否則返回 False
        """

        return platform.system() == 'Windows'

    @classmethod
    def is_package_exists(cls, package_name: str) -> bool:
        """
        檢查指定的包是否存在於連接的 Android 設備上。

        參數:
        package_name (str): 要檢查的 package_name

        返回:
        bool: 如果包存在返回 True，否則返回 False
        """

        device_name = cls.get_android_devices()
        result = cls.adb_executor(
            ["adb", "-s", device_name, "shell", "pm", "list", "packages", package_name]
        )

        if result.returncode == 0 and package_name in result.stdout:
            return True
        return False

    @classmethod
    def get_android_devices(cls):
        """
        獲取連接的 Android 設備列表。

        返回:
        list: 包含連接的 Android 設備 ID 的列表。如果只有一個設備，返回該設備 ID。
        如果沒有設備或發生錯誤，返回值可能為 None。
        """

        adb_command = cls.adb_executor(
            ["adb", "devices"]
        )

        try:
            if adb_command.returncode == 0:
                device_lines = adb_command.stdout.strip().splitlines()[1:]
                devices = [line.split()[0] for line in device_lines if "device" in line]
                # logstack.info(f'Devices: {devices}')
                return devices[0]

            logstack.info(f"命令執行失敗，錯誤訊息: {adb_command.stderr}")
        except Exception as e:
            logstack.info(f"發生錯誤: {e}")

    @classmethod
    def get_uuid(cls) -> str:
        """
        獲取連接的 iOS 設備 UDID。

        返回:
        str: 包含連接的 iOS 設備 UDID 的列表。如果只有一個設備，返回該設備 UDID。
        如果沒有設備或發生錯誤，返回值可能為 None。
        """

        adb_command = cls.adb_executor(
            ["idevice_id", "-l"]
        )

        try:
            if adb_command.returncode == 0:
                udid = adb_command.stdout.strip()
                logstack.info(f'iPhone UDID: {udid}')
                return udid

            logstack.info(f"命令執行失敗，錯誤訊息: {adb_command.stderr}")
        except Exception as e:
            logstack.info(f"發生錯誤: {e}")

    @classmethod
    def get_booted_simulator_udid(cls):
        """
        獲取當前啟動的 iOS 模擬器 UDID。

        返回:
        str: 當前啟動的 iOS 模擬器 UDID。如果沒有啟動的模擬器，返回 None。
        """

        try:
            result = cls.adb_executor(
                ["xcrun", "simctl", "list", "devices"],
            )

            booted_match = re.search(r'\(([\dA-F-]+)\) \(Booted\)', result.stdout)

            if booted_match:
                logstack.info(booted_match.group(1))
                return booted_match.group(1)
            else:
                logstack.info("沒有 Booted 設備")
                return None

        except Exception as e:
            logstack.info(f"Error: {e}")
            return None

    @classmethod
    def is_debug_mode(cls) -> bool:
        if sys.gettrace():
            return True
        return False

    @classmethod
    def clear_uiautomator2_server(cls) -> None:
        """
        清除 UIAutomator2 服務器相關的 package_name。
        這個方法會嘗試移除預定義的 UIAutomator2 package_name。
        """
        UIAUTOMATOR2_PACKAGES = [
            "io.appium.uiautomator2.server",
            "io.appium.uiautomator2.server.test"
        ]

        for package in UIAUTOMATOR2_PACKAGES:
            try:
                adb_command = cls.adb_executor(
                    ["adb", "-s", cls.get_android_devices(), "shell", "pm", "uninstall", package]
                )
                if adb_command.returncode == 0 and cls.is_package_exists(package):
                    logstack.info(f"adb -s {cls.get_android_devices()} shell pm uninstall {package}")
                    logstack.info(f"Successfully uninstalled {package}")
            except subprocess.CalledProcessError as e:
                logstack.warning(f"Failed to uninstall {package}: {e}")

    @classmethod
    def get_driver(cls):
        """獲得當前平台的 Appium Driver"""
        if cls.STATIC_DRIVER is None:
            cls.STATIC_DRIVER = cls._create_driver()
        return cls.STATIC_DRIVER

    @classmethod
    def __is_ios_device(cls):
        """
        判斷當前設備是否為 iOS 實機。

        返回:
        bool: 如果是 iOS 實機返回 True，否則返回 False
        """

        if cls.get_uuid:
            return True
        return False

    @classmethod
    def __is_ios_simulator(cls):
        """
        判斷當前設備是否為 iOS 模擬器。

        返回:
        bool: 如果是 iOS 模擬器返回 True，否則返回 False
        """

        if cls.get_booted_simulator_udid():
            return True
        return False

    @classmethod
    def __is_android_deivces(cls):
        """
        判斷當前設備是否為 Android 設備。

        返回:
        bool: 如果是 Android 設備返回 True，否則返回 False
        """

        if cls.get_android_devices:
            return True
        return False

    @classmethod
    def _create_driver(cls):
        """根據平台建立對應的 Driver"""
        # if GlobalVar.PLATFORM == 'ios':
        system_platform = global_adapter.CommonVar.PLATFORM.lower()
        if system_platform == 'ios':
            if cls.__is_ios_simulator():
                return cls.ios_simulator_driver()
            if cls.__is_ios_device():
                return cls.ios_driver()
        elif system_platform == 'android':
            if cls.__is_android_deivces():
                return cls.android_driver()

    @classmethod
    def android_driver(cls):
        """
        初始化並返回Android Appium WebDriver。

        此方法設置Appium所需的配置，並創建一個連接到 Android 設備的 WebDriver 實例。
        它還處理了一些預設置，如清理 UIAutomator2 服務器和設置日誌選項。

        返回:
        webdriver.Remote: 配置好的 Appium WebDriver 實例，用於控制 Android 設備。

        注意:
        - 此方法假定已經安裝了必要的Appium服務器和Android SDK。
        - 目標應用程序是 'com.cathaybk.nemo.uat'，主活動是 'com.cathaybk.nemo.android.MmbActivity'。
        """

        if not GlobalVar.AWS:
            cls.clear_uiautomator2_server()
        PATH = global_adapter.CommonVar.APP_PATH

        options = AppiumOptions()
        options.set_capability('platformName', 'Android')
        options.set_capability('udid', cls.android_device_serial_number())
        options.set_capability('deviceName', cls.android_device_name())
        options.set_capability('automationName', 'UiAutomator2')
        options.set_capability('autoGrantPermissions', True)
        options.set_capability('enableMultiWindows', True)
        options.set_capability('appPackage', 'com.cathaybk.geb.cubuat')
        options.set_capability('appActivity', 'com.cathaybk.geb.feature.BootActivity')
        options.set_capability('appWaitActivity', "com.cathaybk.geb.feature.login.LoginActivity")
        # options.set_capability('appActivity', 'com.cathaybk.nemo.android.MmbActivity')
        options.set_capability('noReset', cls.KEEP_APP_STATE)
        options.set_capability('shouldTerminateApp', True)
        options.set_capability('disableIdLocatorAutocompletion', True)
        options.set_capability('waitForIdleTimeout', 100)
        # options.set_capability('app', "/Users/twinb00551192/Desktop/ihave_uat/iHave.apk")
        # options.set_capability('app', PATH)
        # 動態 systemPort（平行 Android 必須唯一）
        # options.set_capability("systemPort",  8201)
        # system_port = getattr(global_adapter.CommonVar, 'SYSTEM_PORT', None)
        # if system_port:
        #     options.set_capability('systemPort', system_port)
        #     options.set_capability('newCommandTimeout', 1800)  # 1800 秒
        #     logstack.info("Debug模式:newCommandTimeout設為 1800 秒")
        #     options.set_capability('newCommandTimeout', 100)  # 默認為 100 秒
        #     logstack.info(f"非Debug模式:newCommandTimeout設為 100 秒")

        if cls.is_debug_mode():
            options.set_capability('newCommandTimeout', 1800)  # 1800 秒
            logstack.info(f"Debug模式:newCommandTimeout設為 1800 秒")
        else:
            options.set_capability('newCommandTimeout', 100)  # 默認為 100 秒
            logstack.info(f"非Debug模式:newCommandTimeout設為 100 秒")

        driver = webdriver.Remote(Appium.LOCALHOST + ':4850', options=options)
        # driver = webdriver.Remote(Appium.LOCALHOST + ':4723', options=options)
        return driver

    @classmethod
    def ios_driver(cls):
        """
        設置並初始化一個 iOS Appium 驅動實例。

        該方法創建一個 AppiumOptions 對象，設置所需的 iOS 驅動參數，
        並使用這些參數來初始化 WebDriver 的遠程連接。

        返回:
            webdriver.Remote: 配置好的 Appium 驅動實例。
        """
        PATH = global_adapter.CommonVar.APP_PATH
        options = AppiumOptions()
        options.set_capability('platformName', 'iOS')
        options.set_capability('automationName', 'XCUITest')
        options.set_capability('udid', cls.get_uuid())
        # options.set_capability('bundleId', IOS_CUBE_STG)
        # options.set_capability('bundleId', 'IOS_CUBE')
        options.set_capability('noReset', cls.KEEP_APP_STATE)
        options.set_capability('forceAppLaunch', True)
        options.set_capability('includeSafariInWebviews', True)
        options.set_capability('newCommandTimeout', 3000)  # 设置新命令的超时时间，单位是秒
        options.set_capability('showXcodeLog', True)  # 顯示 Xcode 日誌
        options.set_capability('xcodeOrgId', 'cathayqa')
        # options.set_capability('app', "/Users/twinb00551192/Desktop/ihave_uat/國泰員工服務.app")
        options.set_capability('app', "/Users/twinb00551192/Desktop/QA_file/app-artifact.ipa")
        # options.set_capability('app', PATH)
        driver = webdriver.Remote(Appium.LOCALHOST + Appium.PORT_4723, options=options)
        return driver

    @classmethod
    def ios_simulator_driver(cls):
        """
        設置並初始化一個 iOS Appium 驅動實例。

        該方法創建一個 AppiumOptions 對象，設置所需的 iOS 驅動參數，
        並使用這些參數來初始化 WebDriver 的遠程連接。

        返回:
            webdriver.Remote: 配置好的 Appium 驅動實例。
        """
        PATH = global_adapter.CommonVar.APP_PATH
        options = AppiumOptions()
        options.set_capability('platformName', 'iOS')
        options.set_capability('automationName', 'XCUITest')
        # options.set_capability('deviceName', 'iPhone 16 Pro')
        options.set_capability('deviceName', 'iPad (10th generation)')
        # options.set_capability('udid', cls.get_booted_simulator_udid())
        options.set_capability('udid', '5B44B2FA-8079-4C72-8F53-9A80314280CC')
        # options.set_capability('bundleId', IOS_CUBE_STG)
        # options.set_capability('bundleId', "IOS_CUBE")
        options.set_capability('noReset', cls.KEEP_APP_STATE)
        options.set_capability('forceAppLaunch', True)
        options.set_capability('includeSafariInWebviews', True)
        options.set_capability('newCommandTimeout', 3000)  # 设置新命令的超时时间，单位是秒
        # options.set_capability('app', "/Users/twinb00551192/Desktop/QA_file/iWA-DEV.app")
        options.set_capability('wdaLocalPort', 8102)
        # options.set_capability('mjpegServerPort', 9100)
        options.set_capability('app',PATH)
        driver = webdriver.Remote(Appium.LOCALHOST + Appium.PORT_4723, options=options)
        return driver


if __name__ == '__main__':
    print(DeviceManager.get_booted_simulator_udid())
