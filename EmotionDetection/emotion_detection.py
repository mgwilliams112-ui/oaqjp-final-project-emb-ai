'''This module will import Watson's emotion detector 
   and make it available for use within the app.'''
import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers, timeout=5)
    formatted = json.loads(response.text)
    Emotions_dict = formatted['emotionPredictions'][0]['emotion']
    anger_score = Emotions_dict['anger']
    disgust_score = Emotions_dict['disgust']
    fear_score = Emotions_dict['fear']
    joy_score = Emotions_dict['joy']
    sadness_score = Emotions_dict['sadness']
    high_score = max(Emotions_dict.values())
    rev_emotions = {v: k for k, v in Emotions_dict.items()}
    dominant = rev_emotions[high_score]
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant
    }