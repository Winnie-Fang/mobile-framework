# import pytest
# from huskypo import logstack
# from module.mobile.navigator import Navigator
# from module.mobile.device_manager import DeviceManager
#
#
# class PreConditionAndroidZh:
#     case_map = {}
#
#     def setup_method(self, method):
#         """
#         初始化導航器，根據 case_map 決定是否初始化
#         """
#         try:
#             self.navigator = Navigator().android.zh
#             test_name = method.__name__
#             if not self.case_map or self.case_map.get(test_name) is None:
#                 logstack.info("🕹️ skip_setup_method")
#                 return
#         except Exception as e:
#             logstack.error(f"Setup Fail: {e}")
#             # 僅記錄錯誤，不主動呼叫 teardown，讓 pytest 處理
#
#     def teardown_method(self):
#         driver = DeviceManager.STATIC_DRIVER
#         if driver is not None:
#             driver.quit()
#             DeviceManager.STATIC_DRIVER = None
#         DeviceManager.KEEP_APP_STATE = False
#
#     @pytest.fixture(autouse=True)
#     def auto_teardown(self, request):
#         yield
#         self.teardown_method()
#         logstack.info("🧹 Teardown complete")
#
