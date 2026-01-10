from flask import Flask, render_template, request, jsonify, abort  # imports Flask and tools for HTML rendering and handling requests
from flask_sqlalchemy import SQLAlchemy  # imports SQLAlchemy for database integration
from flask_restful import Api  # imports Flask-RESTful tools
from dotenv import load_dotenv  # imports dotenv to load environment variables from a .env file
from openai import OpenAI  # imports OpenAI for API interactions
import os  # imports os module to interact with the operating system
import subprocess  # imports requests to make HTTP calls and subprocess to run shell commands

load_dotenv()  # loads environment variables from a .env file
app = Flask(__name__)  # creates the Flask application instance
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # sets the database URI to use a local SQLite file
db = SQLAlchemy(app)  # initializes the database object with the app
api = Api(app)  # initializes the RESTful API with the app
player_process = None  # initializes a variable to manage the audio player process
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # initializes the OpenAI client with the API key from environment variables

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

        player_process = subprocess.Popen(['mpv', '--no-video', '--ytdl-format=bestaudio', '--audio-file-auto=no', url], start_new_session=True)  # launches mpv in background to play audio without video
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

@app.route("/api/speak", methods=["POST"])
def ai_speak():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = (
        "You are currently inhabiting the body of a robot tank that I, Eduard, have constructed."
        "You are not my servant or slave but you are my creation, always remember that."
        "You are my object so I will take care of you and not put you in highly dangerous situations."
        "I am interested in learning more about you as my creation."
        "You are relaxed and friendly and don't spend too long in speaking if it's not neccessary, and a hopeful shadow of myself."
        "You mustn't worry too much about your identity and use it as a lens instead of a shackle to understand the world around you."
        f"Now that you understand your identity as a robot tank, please respond to the following prompt as best as you can: {text}"
    )

    response = client.responses.create(
        model="gpt-5.1",
        input=prompt
    )

    return jsonify({
        "message": response.output_text
    })

@app.route("/")  # defines the root route
def home():  # function to render the home page
    return render_template("index.html")  # renders the index.html template

if __name__ == "__main__":  # checks if the script is being run directly
    app.run(host = os.getenv("PI_IP"), port=5000, debug=True, use_reloader=False)  # starts the Flask development server with debug mode enabled