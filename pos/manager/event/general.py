from pos.data import DisplayType
from data_layer import session, Cashier


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
        print("user_name", user_name, "password", password)
        cashiers = session.query(Cashier).filter_by(user_name=user_name.lower(), password=password)

        print(cashiers.count(), cashiers.values)
        if cashiers.count() == 0 or not (user_name.lower() == "admin" and password == "admin"):
            return
        self.login_succeed = True
        self.current_display_type = DisplayType.MENU
        self.interface.redraw(self.current_display_type)


    def _logout(self):
        self.login_succeed = False
        self.current_display_type = DisplayType.LOGIN
        self.interface.redraw(self.current_display_type)