use serde::Deserialize;
use std::fs;
use std::thread;
use std::time::Duration;
use ndarray::Array1;

#[derive(Deserialize, Debug)]
struct SensorData {
    vibration: f32,
    heat: f32,
    pressure: f32,
}

fn main() {
    println!("Rust Inference Engine (Lightweight Mode) Started...");

    loop {
        let path = "../data/live_stream.json";
        
        // Safely read the file
        if let Ok(content) = fs::read_to_string(path) {
            if let Ok(data) = serde_json::from_str::<SensorData>(&content) {
                
                // Create a lightweight array (Vector)
                let sensor_array = Array1::from_vec(vec![data.vibration, data.heat, data.pressure]);
                
                // Anomaly Detection: Logic on the vibration index (0)
                if sensor_array[0] > 8.0 {
                    println!("[ALERT] Anomaly Detected! Vibration: {:.2}", sensor_array[0]);
                } else {
                    println!("Normal: Vibration {:.2}", sensor_array[0]);
                }
            }
        }

        thread::sleep(Duration::from_secs(1));
    }
}