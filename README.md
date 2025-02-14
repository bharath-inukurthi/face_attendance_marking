# Face Attendance Marking

This repository contains scripts for face-based attendance marking using either a system camera or an ESP32 web camera. It also includes the necessary requirements and Arduino code for ESP32 setup.

## 📂 Project Structure
```
face_attendance_marking/
├── requirements.txt
├── requirements/
│   ├── cmake.exe
│   └── dlib/
├── system_camera.py         # Python script for system camera input
├── esp32_camera.py          # Python script for ESP32 web camera input
└── esp32_arduino.ino       # Arduino code for ESP32 WiFi camera setup
```

## 🛠️ Requirements
- Python 3.9 or later
- CMake
- dlib
- OpenCV

### 1️⃣ Install Python Dependencies
First, install the necessary Python libraries from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 2️⃣ Install CMake
CMake is required for building dlib. You can find `cmake.exe` in the `requirements` folder.
- **Windows:** Run `requirements/cmake.exe` to install CMake.
- **Linux/Mac:** Use your package manager:
  ```bash
  sudo apt-get install cmake  # For Debian/Ubuntu
  brew install cmake         # For macOS
  ```

### 3️⃣ Install dlib
Make sure to install `dlib` from the provided files to ensure compatibility:
```bash
pip install dlib --no-cache-dir --find-links=requirements/dlib/
```

## 🚀 Usage
### 1️⃣ Using System Camera
Run the script to capture attendance from the system camera:
```bash
python system_camera.py
```

### 2️⃣ Using ESP32 Web Camera
Make sure the ESP32 is set up and connected to WiFi. Then run:
```bash
python esp32_camera.py --url http://<esp32-ip>:81/stream
```
Replace `<esp32-ip>` with your ESP32's IP address.

## 📡 ESP32 Arduino Setup
Upload the provided `esp32_arduino.ino` to your ESP32 board using Arduino IDE:
1. Select **Board:** ESP32 Wrover Module.
2. Set the **Upload Speed:** 921600.
3. Configure your **WiFi credentials** in the `.ino` file.
4. Upload the code and check the serial monitor for the streaming URL.

## 💡 Notes
- Ensure your firewall allows access to the ESP32 camera feed.
- Use the same WiFi network for your ESP32 and the computer running the script.

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📜 License
This project is licensed under the **Apache 2.0 License**. Please give proper credit if you use this work.
