from pos.data import DisplayType


class Data:
    def __init__(self):
        self.__login_succeed = False
        self.__display_type = DisplayType.LOGIN     # initial display

    @property
    def display_type(self):
        return self.__display_type

    @display_type.setter
    def display_type(self, value):
        if value != DisplayType.LOGIN and self.__login_succeed is False:
            self.__display_type = DisplayType.LOGIN
        elif type(value) is DisplayType:
            self.__display_type = value

    @property
    def login_succeed(self):
        return self.__login_succeed

    @login_succeed.setter
    def login_succeed(self, value):
        if type(value) is bool:
            self.__login_succeed = value
