from appium.webdriver import webdriver
# from mypy.checkpattern import self_match_type_names

from page.ios.panel.keyboard import Keyboard
from page.ios.login import iOSLoginPage
from page.ios.overview import iOSOverviewPage



class NavigatoriOSZh:

    def __init__(self):
        # self.__driver = None
        self.__pre_login_page = None
        self.__ios_login_page = None
        self.__ios_overview_page = None
        self.__keyboard = None


    # @property
    # def driver(self) -> webdriver:
    #     return DeviceManager.get_driver()

    @property
    def ios_login_page(self) -> iOSLoginPage:
        if self.__ios_login_page is None:
            self.__ios_login_page = iOSLoginPage()
        return self.__ios_login_page
    @property
    def ios_overview_page(self) -> iOSOverviewPage:
        if self.__ios_overview_page is None:
            self.__ios_overview_page = iOSOverviewPage()
        return self.__ios_overview_page
    @property
    def keyboard(self) -> Keyboard:
        if self.__keyboard is None:
            self.__keyboard = Keyboard()
        return self.__keyboard


