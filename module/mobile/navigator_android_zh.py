from page.android.login import GMBLoginPage
from page.android.overview import GMBOverviewPage
from page.android.otp import AndroidOTPPage


class NavigatorAndroidZh:

    def __init__(self):
        self.__page = None
        self.__role = None
        self.__gmb_login_page = None
        self.__gmb_overview_page = None
        self.__otp_page = {}

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

    def otp_page(self, role: str) -> AndroidOTPPage:
        if role not in self.__otp_page:
            self.__otp_page[role] = AndroidOTPPage(role=role)
        return self.__otp_page[role]
