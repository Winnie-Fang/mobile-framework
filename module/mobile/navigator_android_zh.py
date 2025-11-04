from page.android.login import IhaveLoginPage
from page.android.login_gmb import GMBLoginPage
from page.android.overview import OverviewPage
from page.android.gmb_overview import GMBOverviewPage
from page.android.question_sliding import QuestionPageSliding


class NavigatorAndroidZh:

    def __init__(self):
        self.__page = None
        self.__ihave_login_page = None
        self.__overview_page = None
        self.__question_page_sliding = None
        self.__gmb_login_page = None
        self.__gmb_overview_page = None

    @property
    def ihave_login_page(self) -> IhaveLoginPage:
        if self.__ihave_login_page is None:
            self.__ihave_login_page = IhaveLoginPage()
        return self.__ihave_login_page

    @property
    def overview_page(self) -> OverviewPage:
        if self.__overview_page is None:
            self.__overview_page = OverviewPage()
        return self.__overview_page

    @property
    def question_page_sliding(self) -> QuestionPageSliding:
        if self.__question_page_sliding is None:
            self.__question_page_sliding = QuestionPageSliding()
        return self.__question_page_sliding

    @property
    def gmb_login_page(self) -> GMBLoginPage:
        if self.__gmb_login_page is None:
            self.__gmb_login_page = GMBLoginPage()
        return self.__gmb_login_page

    @property
    def gmb_overview_page(self) -> GMBOverviewPage:
        if self.__gmb_overview_page is None:
            self.__gmb_overview_page = GMBOverviewPage()
        return self.__gmb_overview_page
