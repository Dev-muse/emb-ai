from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    # Get the input text from query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    # Analyze emotions using the emotion_detector function
    response = emotion_detector(text_to_analyze)
    # Extract individual emotions and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    # Format the response
    result = (
            "For the given statement, the system response is 'anger': {}, 'disgust': {}, "
            "'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}."
        ).format(anger, disgust, fear, joy, sadness, dominant)

    return result

@app.route("/")
def render_index_page():
    return render_template('index.html')

# Run the app on localhost:5000
if __name__ == "__main__":
    app.run(host="localhost", port=5000)
