#!/bin/bash
echo "Starting motor server..."
python3 motor_server.py &

echo "Activating virtual environment..."
source ~/Desktop/robot-tank/.venv/bin/activate

echo "Starting ROBOT TANK..."
python3 api.py