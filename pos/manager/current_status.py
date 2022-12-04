from pos.data import DisplayType, DocumentState, DocumentType, DocumentResult


class CurrentStatus:
    def __init__(self):
        self.__login_succeed = False
        self.__current_display_type = DisplayType.LOGIN     # initial display
        self.__document_state = DocumentState.NONE
        self.__document_type = DocumentType.NONE
        self.__document_result = DocumentResult.NONE

    @property
    def login_succeed(self):
        return self.__login_succeed

    @login_succeed.setter
    def login_succeed(self, value):
        if type(value) is bool:
            self.__login_succeed = value

    @property
    def current_display_type(self):
        return self.__current_display_type

    @current_display_type.setter
    def current_display_type(self, value):
        if value != DisplayType.LOGIN and self.__login_succeed is False:
            self.__current_display_type = DisplayType.LOGIN
        elif type(value) is DisplayType:
            self.__current_display_type = value

    @property
    def document_state(self):
        return self.__document_state

    @document_state.setter
    def document_state(self, value):
        if type(value) is DocumentState:
            self.__document_state = value

    @property
    def document_type(self):
        return self.__document_type

    @document_type.setter
    def document_type(self, value):
        if type(value) is DocumentType:
            self.__document_state = value

    @property
    def document_result(self):
        return self.__document_result

    @document_result.setter
    def document_result(self, value):
        if type(value) is DocumentResult:
            self.__document_result = value
