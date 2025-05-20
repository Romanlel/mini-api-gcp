import os
from google.cloud import aiplatform

def get_ai_joke():
    aiplatform.init(project=os.getenv("PROJECT_ID"), location="us-central1")
    model = aiplatform.TextGenerationModel.from_pretrained("text-bison")
    response = model.predict(prompt="Raconne une blague marrante")
    return response.text.strip()
