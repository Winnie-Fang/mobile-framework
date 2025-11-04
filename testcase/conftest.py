import pytest
from utils.appium_manager import AppiumManager
from module.mobile.device_manager import DeviceManager
from framework import global_adapter
import logging


@pytest.fixture(scope='session', autouse=True)
def appium_server(pytestconfig):
    """
    根據 pytest 指令列參數初始化對應平台的 Appium 服務
    """
    # platform = global_adapter.CommonVar.PLATFORM.lower()
    platform = 'android'
    if platform == 'android':
        AppiumManager(4850).start()
        logging.info('🟢 Appium server for Android started on port 4801')

    elif platform == 'ios':
        AppiumManager(4723).start()
        logging.info('🟢 Appium server for Android started on port 4723')

    else:
        pytest.exit("請使用 --platform=android 或 --platform=ios 啟動測試")


@pytest.fixture(autouse=True)
def teardown_driver():
    """
    測試後自動關閉 Appium driver 並重置狀態
    """
    yield
    driver = DeviceManager.STATIC_DRIVER
    if driver is not None:
        driver.quit()
        DeviceManager.STATIC_DRIVER = None
    DeviceManager.KEEP_APP_STATE = False
    logging.info("🧹 Teardown complete")
