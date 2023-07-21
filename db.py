from google.cloud import firestore

db = firestore.Client()
collection_name = 'jokes'

def add_records(records):
    for record in records:
        add_new_record_if_not_exists('id', record['id'], record)

def check_record_existence(property_name, property_value):
    query = db.collection(collection_name).where(property_name, "==", property_value)
    result = query.get()
    return len(result) > 0

def add_new_record_if_not_exists(property_name, property_value, new_record_data):
    if not check_record_existence(property_name, property_value):
        db.collection(collection_name).add(new_record_data)
