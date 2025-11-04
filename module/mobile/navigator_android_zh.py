from page.android.login import GMBLoginPage
from page.android.overview import GMBOverviewPage


class NavigatorAndroidZh:

    def __init__(self):
        self.__page = None
        self.__gmb_login_page = None
        self.__gmb_overview_page = None

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
