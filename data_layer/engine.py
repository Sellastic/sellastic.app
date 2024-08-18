from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings.settings import Settings


class Engine:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.engine = create_engine(self._create_connection_string(), echo=True)
        print(self.engine)

        self.session = sessionmaker(bind=self.engine)()

    def _create_connection_string(self):
        settings = Settings()
        connection_string = ""
        if settings.db_engine == "sqlite":
            connection_string = f"{settings.db_engine}:///{settings.db_database_name}"
        print("connection_string:", connection_string)
        return connection_string
