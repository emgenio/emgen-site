from pymongo import MongoClient
from .config import *

mongo = MongoClient(STORAGE_DSN)
db = mongo[STORAGE_DB]