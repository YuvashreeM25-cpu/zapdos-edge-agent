# Zapdos Edge Agent
A modular, high-performance Edge Agent for digital factory anomaly detection.

## Architecture
- **Rust Engine**: Low-latency sensor monitoring (using `ndarray`).
- **Python Agent**: Secure Gemini-powered reasoning for maintenance.
- **Interface**: Real-time Streamlit dashboard for actionable insights.

## Security
- API keys are encrypted using `cryptography` (Fernet). 
- **Important**: Keep `secret.key` and `encrypted_key.bin` private!

## Setup
1. `pip install -r requirements.txt`
2. `cargo build --release` (in rust-engine)
3. Run the components in 4 separate terminal tabs:
   - `python scripts/mock_sensor.py`
   - `cargo run` (in rust-engine)
   - `python agent-brain/agent.py`
   - `streamlit run interface/app.py`
