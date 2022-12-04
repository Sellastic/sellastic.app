from pos.data import DisplayType
from data_layer import Cashier


class GeneralEvent:
    def _exit_application(self):
        self.app.quit()

    def _login(self):
        if self.login_succeed:
            return
        user_name = ""
        password = ""
        for key, value in self.interface.window.get_textbox_values().items():
            if key == "user_name":
                user_name = value
            if key == "password":
                password = value
        cashiers = Cashier().filter_by(user_name=user_name.lower(), password=password)

        if cashiers.count() == 0 and not (user_name.lower() == "admin" and password == "admin"):
            return
        if cashiers.count() == 0 and (user_name.lower() == "admin" and password == "admin"):
            cashier = Cashier(user_name=user_name.lower(), password=password,
                              name="", last_name="", identity_number="", description="",
                              is_active=True, is_administrator=True)
            cashier.save()
        else:
            pass
        self.login_succeed = True
        self.current_display_type = DisplayType.MENU
        self.interface.redraw(self.current_display_type)


    def _logout(self):
        self.login_succeed = False
        self.current_display_type = DisplayType.LOGIN
        self.interface.redraw(self.current_display_type)