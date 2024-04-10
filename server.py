''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detetor")

@app.route("/emotionDetector")
def sent_detection():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response is None:
        return "Invalid text! Please try again!."
    result = f''' For the given statement, the system response is
    'anger': {response['anger']}, 'disgust': {response['disgust']},
    'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}.
    The dominant emotion is {response['dominant_emotion']}.'''
    return result

@app.route("/")
def render_index_page():
    ''' This code open and initiat the index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
