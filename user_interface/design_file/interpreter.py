import tomllib

from pos.data import DisplayType
from setting import env_data


class Interpreter:
    __instance = None
    __display_type = None

    def __new__(cls, display_type: DisplayType, *args, **kwargs):
        if cls.__instance is None or cls.__display_type is not display_type:
            cls.__instance = super().__new__(cls)
            cls.__display_type = display_type
        return cls.__instance

    def __init__(self, display_type: DisplayType):
        self.__display_type = display_type
        self.__toml_file_name = self.__set_toml_file_name()

        with open(self.__toml_file_name, "rb") as file_object:
            self.__design_file_data = tomllib.load(file_object)

    @property
    def settings(self):
        settings_data = self.__design_file_data.get("settings")
        if settings_data:
            return settings_data
        return {'name': 'Sellastic',
                'functionality': 'NONE',
                'login_required': False,
                'toolbar': False,
                'statusbar': False,
                'background_color': 0xFFFFFF,
                'foreground_color': 0x000000,
                'width': 1280,
                'height': 640}

    @property
    def toolbar_settings(self):
        design_data = self.__design_file_data.get("toolbar_settings")
        return design_data

    @property
    def design(self):
        design_data = self.__design_file_data.get("design")
        return design_data

    def __set_toml_file_name(self):
        toml_file_name = "design_files/default.toml"
        match self.__display_type:
            case DisplayType.LOGIN:
                toml_file_name = f"design_files/{env_data.main_display_data['login']}"
            case DisplayType.MENU:
                toml_file_name = f"design_files/{env_data.main_display_data['menu']}"
            case DisplayType.SALE:
                toml_file_name = f"design_files/{env_data.main_display_data['sale']}"
            case DisplayType.SERVICE:
                toml_file_name = f"design_files/{env_data.main_display_data['service']}"
            case DisplayType.SETTING:
                toml_file_name = f"design_files/{env_data.main_display_data['setting']}"
            case DisplayType.PARAMETER:
                toml_file_name = f"design_files/{env_data.main_display_data['parameter']}"
            case DisplayType.REPORT:
                toml_file_name = f"design_files/{env_data.main_display_data['report']}"
            case DisplayType.FUNCTION:
                toml_file_name = f"design_files/{env_data.main_display_data['function']}"
            case DisplayType.CUSTOMER:
                toml_file_name = f"design_files/{env_data.main_display_data['customer']}"
            case DisplayType.VOID:
                toml_file_name = f"design_files/{env_data.main_display_data['void']}"
            case DisplayType.REFUND:
                toml_file_name = f"design_files/{env_data.main_display_data['refund']}"
            case DisplayType.STOCK:
                toml_file_name = f"design_files/{env_data.main_display_data['stock']}"
            case DisplayType.END_OF_DAY:
                toml_file_name = f"design_files/{env_data.main_display_data['end_of_day']}"
        return toml_file_name
