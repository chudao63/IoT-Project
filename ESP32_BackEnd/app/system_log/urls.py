from .apis import *
from app import api 

api.add_resource(
    DownloadLogFileApi,
    "/log"
)