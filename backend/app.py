from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from models import predict_emotion
from pydantic  import BaseModel

class AudioData(BaseModel):
    file : str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Just want to add the file collected from the frontend 
@app.post('/audio_prediction')
async def audio(file : UploadFile = File(...)):
    try:
        contents = await file.read()
        with open(f"uploaded_audios/{file.filename}", "wb") as f:
            f.write(contents)
        return { 'prediction' : predict_emotion(file.file) }
    except Exception as e:
        return { 'error' : str(e) }
