from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import jsonify
import data_processor

DB_URI = 'mongodb://admin:admin1234$@ds117336.mlab.com:17336/iml_db'
# DB_URI = 'mongodb://localhost:27017'
DB = 'iml_db'


def get_db():
    return MongoClient(DB_URI)[DB]


def get_one_record():
    doc = get_db().reviews.find_one({"labelled": False})
    if doc is None:
        print("No reviews to label ! Wow - Good to know")
        return False
    return doc


def replace_one(record):
    result = get_db().reviews.replace_one({"_id": ObjectId(record["_id"])}, record, upsert=True)

    if result.matched_count == 1:
        return True
    else:
        None


def save(instance):
    result = get_db().reviews.update_one({"_id": ObjectId(instance["oid"])}, {
        '$set': {
            "rationals": instance['rationales'],
            "labelled": True,
        }}
                            )
    p = result
    print(result.matched_count)
    # replace_one()
    # result = get_db().reviews.replace_one({"_id": ObjectId(record["_id"])}, record, upsert=True)
    #
    # if result.matched_count == 1:
    #     return True
    # else:
    #     None


def get_one():
    doc = get_one_record()

    if not doc:
        return doc

    return jsonify({'id': str(doc["_id"]),
                    'reviewText': doc["cleaned_review_text"],
                    'product_url': f"https://www.amazon.com/dp/{doc['asin']}"
                    })


def get_review_words():
    doc = get_one_record()

    if not doc:
        return doc
    words = data_processor.make_word_fragments(doc["cleaned_review_text"])
    url = f"https://www.amazon.com/dp/{doc['asin']}"
    object_id = doc['_id']
    ratings = doc['overall']
    return (object_id, url, words, ratings)

# Test case
# replace_one(get_one_record())
