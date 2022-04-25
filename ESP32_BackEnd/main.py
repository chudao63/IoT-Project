from multiprocessing.spawn import import_main_path
from app import app
from app.subcriber import*
from app.apis import *
from app.models import *
from app.system_log.urls import *


if __name__ == '__main__':
    app.run()
