from appium.webdriver import webdriver
# from mypy.checkpattern import self_match_type_names

from page.ios.panel.keyboard import Keyboard
from page.ios.login import iOSLoginPage
from page.ios.overview import iOSOverviewPage
from page.ios.login_otp import iOSOTOPage
from page.ios.login_otp_multi import MUiOSOTPage


class NavigatoriOSZh:

    def __init__(self, role=None):
        # self.__driver = None
        self.role = role

        self.__pre_login_page = None
        self.__ios_login_page = None
        self.__ios_overview_page = None
        self.__keyboard = None
        self.__ios_otp_page = None
        self.__ios_otp_page_mu = {}
        self.__keyboard_mu = {}

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

    @property
    def ios_otp_page(self) -> iOSOTOPage:
        if self.__ios_otp_page is None:
            self.__ios_otp_page = iOSOTOPage()
        return self.__ios_otp_page

    def ios_otp_page_mu(self, role: str) -> MUiOSOTPage:
        if role not in self.__ios_otp_page_mu:
            self.__ios_otp_page_mu[role] = MUiOSOTPage(role=role)
        return self.__ios_otp_page_mu[role]

    def keyboard_mu(self, role: str) -> Keyboard:
        if role not in self.__keyboard_mu:
            self.__keyboard_mu[role] = Keyboard(role=role)
        return self.__keyboard_mu[role]
