from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Engine:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.engine = create_engine('sqlite:///db.sqlite3', echo=True)
        print(self.engine)

        self.session = sessionmaker(bind=self.engine)()
