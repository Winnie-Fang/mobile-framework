from appium.webdriver import webdriver
# from mypy.checkpattern import self_match_type_names

from page.ios.panel.keyboard import Keyboard
from page.ios.questions import IOSQuestionsPage
from page.ios.situation import IOSSituationPage
from page.ios.wms.login import WMSLoginPage
from page.ios.login import IhaveLoginPage
from page.ios.overview import IOSOverviewPage
from page.ios.personal import IOSPersonalPage
from page.ios.preview import PreviewPage
from page.ios.iWA.iWA import IWALoginPage


class NavigatoriOSZh:

    def __init__(self):
        # self.__driver = None
        self.__keyboard: Keyboard() = None
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

    @property
    def ihave_login_page(self) -> IhaveLoginPage:
        if self.__ihave_login_page is None:
            self.__ihave_login_page = IhaveLoginPage()
        return self.__ihave_login_page

    @property
    def ios_overview_page(self) -> IOSOverviewPage:
        if self.__ios_overview_page is None:
            self.__ios_overview_page = IOSOverviewPage()
        return self.__ios_overview_page

    @property
    def ios_personal_page(self) -> IOSPersonalPage:
        if self.__ios_personal_page is None:
            self.__ios_personal_page = IOSPersonalPage()
        return self.__ios_personal_page

    @property
    def question_page(self) -> IOSQuestionsPage:
        if self.__ios_questions_page is None:
            self.__ios_questions_page = IOSQuestionsPage()
        return self.__ios_questions_page

    @property
    def situation_page(self) -> IOSSituationPage:
        if self.__ios_situation_page is None:
            self.__ios_situation_page = IOSSituationPage()
        return self.__ios_situation_page

    @property
    def preview_page(self) -> PreviewPage:
        if self.__ios_preview_page is None:
            self.__ios_preview_page = PreviewPage()
        return self.__ios_preview_page

    @property
    def iwa_login_page(self) -> IWALoginPage:
        if self.__iwa_login_page is None:
            self.__iwa_login_page = IWALoginPage()
        return self.__iwa_login_page
