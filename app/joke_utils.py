from google.cloud import aiplatform

def generate_joke():
    aiplatform.init(project="YOUR_PROJECT_ID", location="us-central1")
    prompt = "Raconte une blague originale et marrante."
    response = aiplatform.TextGenerationModel.from_pretrained("text-bison").predict(prompt=prompt)
    return response.text.strip()
