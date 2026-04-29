import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model-small-en-us-0.15"
SAMPLERATE = 16000
BLOCKSIZE = 8000

audio_queue = queue.Queue()

model = Model(MODEL_PATH)


def audio_callback(indata, frames, time, status):
    if status:
        print(status)

    audio_queue.put(bytes(indata))


def listen_once():
    """
    Listens until speech is recognized once,
    then returns the recognized text.
    """
    recognizer = KaldiRecognizer(model, SAMPLERATE)

    with sd.RawInputStream(
        samplerate=SAMPLERATE,
        blocksize=BLOCKSIZE,
        dtype="int16",
        channels=1,
        callback=audio_callback
    ):
        while True:
            data = audio_queue.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())

                if result.get("text"):
                    return result["text"]