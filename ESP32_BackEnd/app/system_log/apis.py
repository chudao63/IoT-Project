from app import api 
from flask_restful import Resource
import os, sys
from flask import send_from_directory


class DownloadLogFileApi(Resource):
    def get(self):
        return send_from_directory(
            directory= f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/logs", path= f"log.log", as_attachment = True)