from flask import Flask, render_template, request  # imports Flask and tools for HTML rendering and handling requests
from flask_sqlalchemy import SQLAlchemy  # imports SQLAlchemy for database integration
from flask_restful import Api  # imports Flask-RESTful tools
import requests, subprocess  # imports requests to make HTTP calls and subprocess to run shell commands

# THIS IS UPDATED WOOHOO

# This Flask API was created with the help of the following video:
# https://www.youtube.com/watch?v=z3YMz-Gocmw&t=128s

app = Flask(__name__)  # creates the Flask application instance
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # sets the database URI to use a local SQLite file
db = SQLAlchemy(app)  # initializes the database object with the app
api = Api(app)  # initializes the RESTful API with the app

PI_IP = "http://192.168.0.108:5001"  # stores the Raspberry Pi's local IP address and port

@app.route("/api/move", methods=["POST"])  # defines a POST endpoint at /api/move
def move():  # function to handle movement commands
    data = request.get_json()  # gets JSON data from the POST request
    direction = data.get("direction")  # extracts the "direction" value from the JSON
    if direction:  # checks if a direction was provided
        try:
            response = requests.post(f"{PI_IP}/move", json={"direction": direction})  # sends a POST request to the Pi with the direction
            return {"status": "sent", "pi_response": response.json()}  # returns success response with Pi's response
        except Exception as e:  # handles exceptions
            return {"error": str(e)}, 500  # returns error message with 500 status code
    return {"error": "No direction provided"}, 400  # returns error if direction was missing

@app.route("/api/play", methods=["POST"])  # defines a POST endpoint at /api/play
def play():  # function to send a play URL to the Pi
    data = request.get_json()  # gets JSON data from the request
    url = data.get("url")  # extracts the "url" from the data
    if url:  # checks if a URL was provided
        try:
            response = requests.post(f"{PI_IP}/play", json={"url": url})  # sends a POST request to the Pi with the URL
            return {"status": "sent", "pi_response": response.json()}  # returns success response with Pi's response
        except Exception as e:  # handles exceptions
            return {"error": str(e)}, 500  # returns error message with 500 status code
    return {"error": "No URL provided"}, 400  # returns error if URL was missing

@app.route("/api/play", methods=["POST"])  # defines another POST endpoint at the same path (this will override the above one)
def play_audio():  # function to play audio locally using mpv
    data = request.get_json()  # gets JSON data from the request
    url = data.get("url")  # extracts the "url" from the data
    if not url:  # checks if the URL is missing
        return {"error": "No URL provided"}, 400  # returns error if URL was not provided

    try:
        subprocess.Popen(['mpv', '--no-video', '--ytdl-format=bestaudio', url])  # launches mpv in background to play audio without video
        return {"message": "Playing audio"}, 200  # returns success message
    except Exception as e:  # handles exceptions
        return {"error": str(e)}, 500  # returns error message with 500 status code

@app.route("/")  # defines the root route
def home():  # function to render the home page
    return render_template("index.html")  # renders the index.html template

if __name__ == "__main__":  # checks if the script is being run directly
    app.run(debug=True)  # starts the Flask development server with debug mode enabled
