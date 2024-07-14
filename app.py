from flask import Flask, render_template_string, request, session
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  
app.secret_key = 'your_secret_key'

genai.configure(api_key='AIzaSyDBj64LSdzZ0PwVtoFLtmydS6yl20r5Z2A')
model = genai.GenerativeModel('gemini-pro')

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

app.after_request(add_cors_headers)

@app.route('/', methods=['POST'])
def video_transcript_summarizer():
    video_id = request.form.get('video_id')
    if video_id:
        summary = generate_summary(video_id)
        return summary
    else:
        return "Please enter a video ID."

def generate_summary(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = " ".join(text['text'] for text in transcript)
    
    if transcript_text:
        prompt = f"""
        Your task is to summarize the transcript of video to provide quick overview of
        video for helping a student to understand video in short.

        Transcript to be summarized: {transcript_text}
        """

        response = model.generate_content(prompt)
        return response.text
    else:
        return "Transcript not found for this video ID."

if __name__ == '__main__':
    app.run(debug=True)

