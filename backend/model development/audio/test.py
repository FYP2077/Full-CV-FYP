from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
import torch
import torchaudio
import os

def extracting_audio(type_of_audio_path):
    wav = os.path.join('data',type_of_audio_path)
    data_path = os.listdir(wav)
    return (wav,data_path)

model_name = './audiomodel'

model = AutoModelForAudioClassification.from_pretrained(model_name)
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)

def predict_emotion(path):
    speech_array, sampling_rate = torchaudio.load(path)

    resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16000)
    speech = resampler(speech_array).squeeze().numpy()

    inputs = feature_extractor(speech, sampling_rate=16000, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = torch.argmax(logits).item()
    return model.config.id2label[predicted_class_id]

path,sad_path = extracting_audio("Sad")
print(predict_emotion(f"{path}/{sad_path[0]}"))