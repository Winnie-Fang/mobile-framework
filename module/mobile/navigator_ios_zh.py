from appium.webdriver import webdriver
# from mypy.checkpattern import self_match_type_names

# from page.ios.panel.keyboard import Keyboard



class NavigatoriOSZh:

    def __init__(self):
        # self.__driver = None
        self.__pre_login_page = None
        self.__wms_login_page = None
        self.__ihave_login_page = None
        self.__ios_overview_page = None
        self.__ios_personal_page = None
        self.__ios_questions_page = None
        self.__ios_situation_page = None
        self.__ios_preview_page = None
        self.__iwa_login_page = None

    # @property
    # def driver(self) -> webdriver:
    #     return DeviceManager.get_driver()

    # @property
    # def wms_login_page(self) -> WMSLoginPage:
    #     if self.__wms_login_page is None:
    #         self.__wms_login_page = WMSLoginPage()
    #     return self.__wms_login_page

