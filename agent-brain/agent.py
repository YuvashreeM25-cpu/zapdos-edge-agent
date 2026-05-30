import json
import time
import google.generativeai as genai
from cryptography.fernet import Fernet

# --- SETUP GEMINI ---
MODEL_NAME = "gemini-3.1-flash-lite"
with open("../scripts/secret.key", "rb") as key_file:
    cipher_suite = Fernet(key_file.read())
with open("../scripts/encrypted_key.bin", "rb") as file:
    API_KEY = cipher_suite.decrypt(file.read()).decode()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name=MODEL_NAME)

HISTORY_FILE = "../data/history.json"

def get_gemini_recommendation(vibration):
    prompt = f"System alert: Sensor detected high vibration of {vibration}. Provide one brief, professional maintenance action."
    response = model.generate_content(prompt)
    return response.text

def run_agent():
    print("Agent watching for anomalies...")
    while True:
        try:
            with open("../data/live_stream.json", "r") as f:
                data = json.load(f)
            
            vib = data.get("vibration", 0)
            
            if vib > 9.3:
                print(f"!!! ANOMALY DETECTED: {vib} !!!") # NEW: Debug print
                insight = get_gemini_recommendation(vib)
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                
                # 2. Append to history
                history =[]
                if os.path.exists(HISTORY_FILE):
                    with open(HISTORY_FILE, "r") as f:
                        history = json.load(f)
                
                history.append({"timestamp": timestamp, "instruction": insight})
                
                with open(HISTORY_FILE, "w") as f:
                    json.dump(history, f)
                
                print("Anomaly logged to history.")
                time.sleep(30) # Cool-down
        except: pass
        
        time.sleep(2)

if __name__ == "__main__":
    import os
    run_agent()