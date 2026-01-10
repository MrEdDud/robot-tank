#!/usr/bin/bash
echo "Starting motor server..."
python3 motor_server.py &
MOTOR_PID=$!

cleanup() {
    echo -e "\n * Shutting down motor server..."
    kill $MOTOR_PID
}
trap cleanup EXIT

echo "Activating virtual environment..."
source ~/Desktop/robot-tank/.venv/bin/activate

echo "Starting ROBOT TANK..."
python3 api.py

wait