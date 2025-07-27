# app.py

from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Dental AI Voice Bot is running!"

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    response.say("Hi, thanks for calling Smile Dental. Our clinic hours are Monday to Friday, 9 AM to 5 PM. How can we help you today?")              
    return Response(str(response), mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/", methods=["GET"])
def home():
    return "Dental AI Voice Bot is running!"
@app.route("/", methods=["GET"])
def home():
    return "Dental AI Voice Bot is running!"


