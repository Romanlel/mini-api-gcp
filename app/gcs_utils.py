from google.cloud import storage
import os, json

BUCKET_NAME = os.environ["BUCKET_NAME"]
FILE_PATH = os.environ["FILE_PATH"]

def read_file_from_gcs():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(FILE_PATH)
    data = blob.download_as_text()
    return json.loads(data)

def write_file_to_gcs(new_data):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(FILE_PATH)
    content = json.loads(blob.download_as_text())
    content.append(new_data)
    blob.upload_from_string(json.dumps(content), content_type='application/json')
    return {"status": "success", "data": new_data}
