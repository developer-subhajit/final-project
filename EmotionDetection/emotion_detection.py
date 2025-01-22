import requests
import json 

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convert the response text into a dictionary using the json library functions.
    formatted_response = json.loads(response.text)

    # Extract the required set of emotions, including anger, disgust, fear, joy and sadness, 
    # along with their scores.
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Extract the dominant emotion from the response
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions