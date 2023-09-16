import pytest

from generic.base_setup import Base_SetUp
from page.login_page import LoginPage
from generic.excel import Excel
class Test_InvalidLogin(Base_SetUp):

    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        un = Excel.get_cell_data(self.XL_PATH,"invalidlogin",2,1)
        pw = Excel.get_cell_data(self.XL_PATH, "invalidlogin", 2, 2)
        # 1. Enter invalid UN
        loginpage=LoginPage(self.driver)
        loginpage.set_username(un)
        # 2. Enter invalid PW
        loginpage.set_password(pw)
        # 3. Click on login Button
        loginpage.click_login_button()
        # 4. Verify that Err Msg is Displayed
        status=loginpage.verify_err_msg_displayed(self.wait)
        assert status