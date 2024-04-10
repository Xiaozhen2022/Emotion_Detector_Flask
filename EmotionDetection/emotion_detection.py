import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    print(response.status_code)
    if response.status_code == 200:
        format_response = json.loads(response.text)['emotionPredictions'][0]['emotion']
        max_key = max(format_response.items(), key=lambda x: x[1])[0]
        format_response['dominant_emotion']=max_key
    elif response.status_code == 400 or response.status_code == 500:
        format_response = None
    return format_response

