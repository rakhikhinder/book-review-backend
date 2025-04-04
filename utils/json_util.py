from bson import ObjectId

def serialize_document(document):
    """Convert MongoDB document to a JSON serializable dictionary."""
    if isinstance(document, list):
        return [serialize_document(doc) for doc in document]
    elif isinstance(document, dict):
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)
            elif isinstance(value, dict):
                document[key] = serialize_document(value)
            elif isinstance(value, list):
                document[key] = [serialize_document(item) for item in value]
        return document
    elif isinstance(document, ObjectId):
        return str(document)
    return document
