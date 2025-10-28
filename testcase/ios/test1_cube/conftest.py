# import pytest
# from appium import webdriver
# from appium.options.common import AppiumOptions
#
# # from module.ios.cube.en_common import CubeCommonEN
# # from module.ios.cube.zh_common import CubeCommon。
# from module.mobile.device_manager import DeviceManager
# from huskypo import Appium, Log
#
# from module.mobile.globalvar import GlobalVar
#
#
# # @pytest.fixture(scope='function', params=['ipad1', 'ipad2'])
# # def iphone(request, ipads):
# #     """
# #     Setup device to testcase.\n
# #     iOS can input `xcrun xctrace list devices` to get informations.
# #
# #     xdist appium and xcuitest server settings.
# #     appium -p 4801 --driver-xcuitest-webdriveragent-port 8201
# #     appium -p 4802 --driver-xcuitest-webdriveragent-port 8202
# #     """
# #     # 顯示 uipo 的 live log 並記錄於檔案中
# #     Log.RECORD = True
# #
# #     # 設置最多兩部裝置
# #     iphone = None  # aws device farm default
# #     connection = Appium.LOCALHOST + ':4723'
# #     if ipads is not None:
# #         len_ipads = len(ipads)
# #         if len_ipads > 2:
# #             raise ValueError('❌ 最多只能設置兩部iphone')
# #         iphone = ipads[0]
# #         connection = Appium.LOCALHOST + ':4723'
# #         # 此處確保當有兩台裝置時才設置server，否則都用同一個即可
# #         if request.param == 'iphone2' and len_ipads == 2:
# #             iphone = ipads[1]
# #             connection = Appium.LOCALHOST + ':4802'
# #
# #     # driver 參數設定
# #     options = AppiumOptions()
# #     # bundleid = env['bundleid']
# #     # noreset = True if 'UT' in bundleid else False
# #     options.set_capability('platformName', 'iOS')
# #     options.set_capability('automationName', 'XCUITest')
# #     if iphone is not None:
# #         options.set_capability('deviceName', iphone['deviceName'])
# #         print(iphone["deviceName"])
# #         options.set_capability('udid', iphone['udid'])
# #     options.set_capability('udid', DeviceManager.get_uuid())
# #     # options.set_capability('bundleId', bundleid)
# #     # options.set_capability('noReset', noreset)
# #     options.set_capability('forceAppLaunch', True)
# #     options.set_capability('autoGrantPermissions', True)
# #     options.set_capability('includeSafariInWebviews', True)
# #     print("before")
# #     options.set_capability('newCommandTimeout', 720)
# #
# #     # 開始執行 driver 實體，並在每個 testcase 結束後關閉 driver
# #     driver = webdriver.Remote(connection, options=options)
# #     yield driver
# #     driver.quit()
#
#
# #
# # @pytest.fixture(scope='function')
# # def version(env):
# #     """
# #     取得app的版本
# #     """
# #     return env['version']
# #
# # @pytest.fixture(scope="session",autouse=True)
# # def set_platform_variable():
# #     yield
# #     GlobalVar.PLATFORM="ios"
#
# @pytest.fixture(scope='function', params=['ipad_mini'])  # 設置單一模擬器
# def ipad(request, ipads):
#     """
#     Setup device to testcase.\n
#     iOS can input `xcrun xctrace list devices` to get informations.
#     xdist appium and xcuitest server settings.
#     """
#     # 顯示 uipo 的 live log 並記錄於檔案中
#     Log.RECORD = True
#
#     # 設置最多兩部裝置
#     ipad = None  # aws device farm default
#     connection = Appium.LOCALHOST + ':4723'
#     if ipads is not None:
#         connection = Appium.LOCALHOST + ':4723'
#         ipad = ipads[0]
#
#     options = AppiumOptions()
#
#     options.set_capability('platformName', 'iOS')
#     options.set_capability('automationName', 'XCUITest')
#     options.set_capability('platformVersion','18.2')
#     if ipad is not None:
#         # options.set_capability('deviceName', 'iPad mini (A17 Pro)')
#         options.set_capability('deviceName', ipad["deviceName"])
#         options.set_capability('forceAppLaunch', True)  # 強制啟動應用
#     options.set_capability('autoGrantPermissions', True)  # 自動授權權限
#     options.set_capability('includeSafariInWebviews', True)  # 包含 Safari WebView
#     options.set_capability('newCommandTimeout', 720)
#     options.set_capability('app', "/Users/twinb00776283/Downloads/0203測試檔案/智能財富顧問.app")
#
#     # 開始執行 driver 實體，並在每個 testcase 結束後關閉 driver
#     driver = webdriver.Remote(connection, options=options)
#     yield driver
#     driver.quit()
