import pydantic
from dotenv import load_dotenv
import os


class Config(pydantic.BaseModel):
    load_dotenv()
    login: str = os.environ.get('USER')
    access_key: str = os.environ.get('KEY')


config = Config()
