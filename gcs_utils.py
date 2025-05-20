import os, json
from google.cloud import storage

def read_from_gcs():
    client = storage.Client()
    bucket = client.bucket(os.getenv("BUCKET_NAME"))
    blob = bucket.blob(os.getenv("FILE_PATH"))
    content = blob.download_as_text()
    return json.loads(content)

def write_to_gcs(new_entry):
    client = storage.Client()
    bucket = client.bucket(os.getenv("BUCKET_NAME"))
    blob = bucket.blob(os.getenv("FILE_PATH"))
    
    content = json.loads(blob.download_as_text())
    content.append(new_entry)
    blob.upload_from_string(json.dumps(content), content_type="application/json")
    return {"status": "ok", "added": new_entry}
