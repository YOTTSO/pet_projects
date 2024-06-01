from pydantic import BaseSettings

class Settings(BaseSettings):
        db_url = "asyncopg2+postgresql://{user}:{password}@{host}/{db}".format()
