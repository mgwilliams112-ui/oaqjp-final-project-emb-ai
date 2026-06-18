from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection():
    target_text = request.args.get('textToAnalyze')
    result = emotion_detector(target_text)
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']
    if dominant == None:
        return ('Invalid text! Please try again!')
    return f'''For the given statement, the system response is 
    'anger': {anger}, 'disgust': {disgust}, 
    'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. 
    The dominant emotion is {dominant}.'''

if __name__ == "__main__":
    app.run(debug=True)
    