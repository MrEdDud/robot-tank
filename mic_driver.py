import queue
import json
import sounddevice as sd
import time
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model-small-en-us-0.15"
SAMPLERATE = 16000
BLOCKSIZE = 8000

audio_queue = queue.Queue()
model = Model(MODEL_PATH)


def audio_callback(indata, frames, time_info, status):
    if status:
        print(status)

    audio_queue.put(bytes(indata))


def listen_once(timeout=5):
    DEVICE_INDEX = 1

    """
    Listen for up to `timeout` seconds,
    then return recognized speech.
    """
    recognizer = KaldiRecognizer(model, SAMPLERATE)

    print("Listening...")
    start_time = time.time()

    with sd.RawInputStream(
        samplerate=SAMPLERATE,
        blocksize=BLOCKSIZE,
        dtype="int16",
        channels=1,
        callback=audio_callback,
        device=DEVICE_INDEX
    ):
        while time.time() - start_time < timeout:
            data = audio_queue.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())

                if result.get("text"):
                    return result["text"]

        # Timeout fallback
        partial = json.loads(recognizer.FinalResult())

        return partial.get("text", "")