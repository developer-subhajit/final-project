"""
This module contains the Flask application for the emotion detection service.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handles the emotion detection route.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)

    if emotions.get("dominant_emotion") is None:
        return "Invalid text! Please try again"

    return f"""For the given statement, the system response is
    'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 
    'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}.
    The dominant emotion is <strong>{emotions['dominant_emotion']}</strong>"""

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
