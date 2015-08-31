from .connection import db
from pymongo.errors import WriteError
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId
import datetime

def create_throwaway(email=0):
    """ Creates a throwaway email """
    if email is 0:
        return False
    record = db.throwaway.find_one_and_update({"to":email},{"$set":{"to":email}, "$setOnInsert":{"created": datetime.datetime.utcnow()}}, upsert=True, return_document=ReturnDocument.AFTER)
    return record['_id']

def find_address_and_delete(id=0):
    if not valid_object_id(id) is True:
        return False
    return db.throwaway.find_one_and_delete({"_id":ObjectId(id)},  projection=['to'])

def valid_object_id(id=0):
    if isinstance(id, str) and len(id) is 24:
        return True
    return False