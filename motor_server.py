from flask import Flask, request
import motor_driver

app = Flask(__name__)

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    direction = data.get("direction")
    if not direction:
        return {"error": "No direction provided"}, 400

    try:
        if direction == "up":
            motor_driver.forward()
        elif direction == "down":
            motor_driver.reverse()
        elif direction == "left":
            motor_driver.left()
        elif direction == "right":
            motor_driver.right()
        else:
            motor_driver.stop()
        return {"status": "executed", "direction": direction}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)