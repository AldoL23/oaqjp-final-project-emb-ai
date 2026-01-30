from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import requests
import json

app= Flask("emotionDetector")

@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return"Error: No text provide. Please provide a text to analyze."
    result= emotion_detector(text_to_analyze)
    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']} "
        f"with a score of {result['dominant_score']:.2f}."
    )
    
    return response_text

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
