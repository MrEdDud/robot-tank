from flask import Flask, render_template, request, jsonify, abort  # imports Flask and tools for HTML rendering and handling requests
from flask_sqlalchemy import SQLAlchemy  # imports SQLAlchemy for database integration
from flask_restful import Api  # imports Flask-RESTful tools
from motor_driver import forward, reverse, turn_left, turn_right, motor_stop  # imports motor control functions from motor_driver module
import requests, subprocess, os  # imports requests to make HTTP calls and subprocess to run shell commands

app = Flask(__name__)  # creates the Flask application instance
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # sets the database URI to use a local SQLite file
db = SQLAlchemy(app)  # initializes the database object with the app
api = Api(app)  # initializes the RESTful API with the app
player_process = None  # initializes a variable to manage the audio player process

PI_IP = "http://192.168.0.108:5001"  # stores the Raspberry Pi's local IP address and port
ALLOWED_IP = os.getenv("ALLOWED_IP")

@app.before_request
def limit_remote_addr():
    if request.remote_addr != ALLOWED_IP:
        abort(403)

@app.route("/api/move", methods=["POST"])  # defines a POST endpoint at /api/move
def move():  # function to handle movement commands
    data = request.get_json()  # gets JSON data from the POST request
    direction = data.get("direction")  # extracts the "direction" value from the JSON
    if not direction:
        return {"error": "No direction provided"}, 400

    try:
        if direction == "up":
            forward()
        elif direction == "down":
            reverse()
        elif direction == "left":
            turn_left()
        elif direction == "right":
            turn_right()
        else:
            motor_stop()

        return {"status": "executed", "direction": direction}
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/api/play", methods=["POST"])  # defines another POST endpoint at the same path (this will override the above one)
def play_audio():  # function to play audio locally using mpv
    global player_process  # declares player_process as a global variable to manage the audio player process
    data = request.get_json()  # gets JSON data from the request
    url = data.get("url")  # extracts the "url" from the data

    if not url:  # checks if the URL is missing
        return jsonify({"error": "No URL provided"}), 400  # returns error if URL was not provided

    try:
        if player_process and player_process.poll() is None:  # checks if the player process is already running
            player_process.terminate()  # terminates the existing player process if it is running

        player_process = subprocess.Popen(['mpv', '--no-video', '--ytdl-format=bestaudio', url])  # launches mpv in background to play audio without video
        return jsonify({"message": "Playing audio at volume {volume}"}), 200  # returns success message
    except Exception as e:  # handles exceptions
        return jsonify({"error": str(e)}), 500  # returns error message with 500 status code

@app.route("/api/stop", methods=["POST"])
def stop_audio():
    global player_process
    if player_process and player_process.poll() is None:
        player_process.terminate()
        return jsonify({"message": "Audio stopped"}), 200
    else:
        return jsonify({"message": "No audio playing"}), 200

@app.route("/")  # defines the root route
def home():  # function to render the home page
    return render_template("index.html")  # renders the index.html template

if __name__ == "__main__":  # checks if the script is being run directly
    app.run(host = "0.0.0.0", debug=True)  # starts the Flask development server with debug mode enabled
