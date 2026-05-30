import time
import json
import random
import os

# Define where the data should go (the data folder we created)
DATA_FILE = os.path.join("..", "data", "live_stream.json")

def generate_telemetry():
    print("Starting sensor simulation... Press Ctrl+C to stop.")
    while True:
        # Simulate sensor readings
        data = {
            # Change the range back to something normal
            "vibration": round(random.uniform(0.0, 10.0), 2), # Always above 8.0!,
            "heat": round(random.uniform(40.0, 120.0), 2),
            "pressure": round(random.uniform(20.0, 50.0), 2),
            "timestamp": time.time()
        }
        
        # Save to our shared data folder
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
        
        # Wait 1 second before generating new data
        time.sleep(1)

if __name__ == "__main__":
    generate_telemetry()