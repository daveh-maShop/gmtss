import couchbase.subdocument as SD

from couchbase.bucket import Bucket
from couchbase.exceptions import KeyExistsError, NotFoundError
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator


def get_bucket(bucket_id):

    cluster = Cluster('couchbase://10.101.3.79:8091')
    authenticator = PasswordAuthenticator('buckets', 'buckets')
    cluster.authenticate(authenticator)
    cb = cluster.open_bucket(bucket_id)
    return cb


def get_new_document_id(bucket, counter_id):
    auto_document_id = bucket.counter(counter_id, delta=1).value
    return str(auto_document_id)


"""
Full document methods...
"""


def get(bucket, document_id):
    rv = bucket.get(document_id)  # don't convert the dict to json.  the method will automatically
    return rv


def insert(bucket, document_id, document):
    try:
        bucket.insert(document_id, document)  # don't convert the dict to json.  the method will automatically
    except KeyExistsError:
        raise
    return document_id


def update(bucket, document_id, document):
    try:
        bucket.insert(document_id, document)  # don't convert the dict to json.  the method will automatically
    except NotFoundError:
        raise
    return document_id


def upsert(bucket, document_id, document):
    try:
        bucket.upsert(document_id, document)  # don't convert the dict to json.  the method will automatically
    except Exception:
        raise
    return document_id


def remove(bucket, document_id):
    try:
        bucket.remove(document_id)  # don't convert the dict to json.  the method will automatically
    except:
        raise


"""
Sub document methods...
"""


def subdocument_get(bucket, path, document_id):
    rv = bucket.lookup_in(document_id, SD.get(path))  # don't convert the dict to json.  the method will automatically
    return rv[0]


def subdocument_replace(bucket, document_id, path, subdocument):
    rv = bucket.mutate_in(document_id, SD.replace(path, subdocument))  # don't convert the dict to json.  the method will automatically
    return rv[0]


def subdocument_upsert(bucket, document_id, path, subdocument):
    rv = bucket.mutate_in(document_id, SD.replace(path, subdocument))  # don't convert the dict to json.  the method will automatically
    return rv[0]


def subdocument_insert(bucket, document_id, path, insertdoc):
    rv = bucket.mutate_in(document_id, SD.insert(path, insertdoc))  # don't convert the dict to json.  the method will automatically
    return rv[0]


def subdocument_remove(bucket, document_id, path):
    rv = bucket.mutate_in(document_id, SD.remove(path))  # don't convert the dict to json.  the method will automatically
    return rv[0]
