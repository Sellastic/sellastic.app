import os
import sys
import tomllib


class Settings:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        with open("settings.toml", "rb") as file_object:
            self.setting_data = tomllib.load(file_object)
            self.database = self.setting_data.get("database")
            self.main_display = self.setting_data.get("main_display")
            self.customer_display = self.setting_data.get("customer_display")
            self.design_files_list = self.setting_data.get("design_files")

    @property
    def db_engine(self):
        if self.database:
            return self.database.get("engine")
        return None

    @property
    def db_database_name(self):
        if self.database:
            return self.database.get("database_name")
        return None

    @property
    def md_width(self):
        if self.main_display:
            return self.main_display.get("width")
        return 1280

    @property
    def md_height(self):
        if self.main_display:
            return self.main_display.get("height")
        return 640

    @property
    def cd_width(self):
        if self.customer_display:
            return self.customer_display.get("width")
        return 1280

    @property
    def cd_height(self):
        if self.customer_display:
            return self.customer_display.get("height")
        return 640

    @property
    def main_display_data(self):
        if self.design_files_list["main_display"]:
            return self.design_files_list["main_display"]
        return None

    @property
    def customer_display_data(self):
        if self.design_files_list["customer_display"]:
            return self.design_files_list["customer_display"]
        return None

    @property
    def image_absolute_folder(self):
        project_path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
        image_path = os.path.join(project_path, 'design_files', 'images')
        return image_path
