from page.android.login import IhaveLoginPage
from page.android.overview import OverviewPage
from page.android.personal import PersonalPage
from page.android.question import QuestionPage
from page.android.question_sliding import QuestionPageSliding


class NavigatorAndroidZh:

    def __init__(self):
        self.__page = None
        self.__ihave_login_page = None
        self.__overview_page = None
        self.__personal_page = None
        self.__question_page = None
        self.__question_page_sliding = None

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
    def personal_page(self) -> PersonalPage:
        if self.__personal_page is None:
            self.__personal_page = PersonalPage()
        return self.__personal_page
    @property
    def question_page(self) -> QuestionPage:
        if self.__question_page is None:
            self.__question_page = QuestionPage()
        return self.__question_page

    @property
    def question_page_sliding(self) -> QuestionPageSliding:
        if self.__question_page_sliding is None:
            self.__question_page_sliding = QuestionPageSliding()
        return self.__question_page_sliding