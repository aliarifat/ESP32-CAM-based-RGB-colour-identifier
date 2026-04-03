# 🎨 ESP32-CAM RGB Colour Identifier

An IoT + Computer Vision project that detects **Red, Green, and Blue objects in real-time** using an ESP32-CAM and Python OpenCV.

---

## 📌 Project Overview

The world is full of colors, and while humans can easily distinguish them, teaching machines to do so requires computer vision techniques.

This project uses:
- 📷 ESP32-CAM (image streaming)
- 🌐 Wi-Fi (data transfer)
- 🧠 Python + OpenCV (color detection)

to build a real-time RGB color detection system.

---

## 🧠 System Architecture

### 1. Overview
- ESP32-CAM acts as a **camera server**
- Python script acts as a **processing unit**
- Communication happens over **local Wi-Fi**

---

### 2. Components

#### 🔧 Hardware
- ESP32-CAM (AI Thinker)
- Wi-Fi Router
- Computer (Laptop/Desktop/Raspberry Pi)

#### 💻 Software
- ESP32 firmware (Arduino)
- Python script using OpenCV

---

## 🔄 Data Flow

1. ESP32-CAM connects to Wi-Fi  
2. Starts HTTP server  
3. Captures JPEG image (800×600)  
4. Python script fetches image  
5. Converts to HSV  
6. Detects Red, Green, Blue regions  
7. Draws contours and labels  
8. Displays processed frame  

---

## 🧰 Components Required

| Component | Quantity |
|----------|---------|
| ESP32-CAM | 1 |
| FTDI Programmer | 1 |
| Jumper Wires | Few |
| Micro USB Cable | 1 |

---

## 🔌 Circuit Connections

| ESP32-CAM | FTDI |
|----------|------|
| VCC | 5V |
| GND | GND |
| U0R | TX |
| U0T | RX |
| IO0 | GND (for upload only) |

⚠️ After upload:
- Disconnect IO0 from GND  
- Press RESET  

---

## ⚙️ Setup Instructions

### 1. Arduino Setup
- Install ESP32 board package  
- Install ESP32-CAM library  
- Select board: **AI Thinker ESP32-CAM**  
- Upload code  
- Open Serial Monitor to get IP  

---

## 🖥️ Python Environment Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

---
## ⚙️ Setup Instructions
### 1. Arduino Setup
- Install ESP32 board package  
- Install ESP32-CAM library  
- Select board: **AI Thinker ESP32-CAM**  
- Upload code  
- Open Serial Monitor to get IP  

---

## 🖥️ Python Environment Setup

### 1. Create Virtual Environment
Activate:
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate


### 2. Install Dependencies
pip install opencv-python numpy urllib3


---
### How does the color detection work
- Step 1: Convert Image to HSV
- Step 2: Apply Color Masks
- Step 3: Clean Image  
- Step 4: Detect Contours 
- Step 5: Filter Objects
- Step 5: Filter Objects
- Step 6: Track Object


---



### Output
- Real-time video window
- Detected colors labeled
- Center points marked 

---





### Test
<img width="1064" height="938" alt="Screenshot 2025-01-29 190338" src="https://github.com/user-attachments/assets/3f9eb59b-a208-456e-9768-31d825dbaa59" />
<img width="978" height="921" alt="Screenshot 2025-01-29 190717" src="https://github.com/user-attachments/assets/5af2063a-87d0-48db-ac52-cb8afcff6ff6" />
<img width="1052" height="782" alt="Screenshot 2025-01-29 191040" src="https://github.com/user-attachments/assets/be3e3308-f1f5-4a84-ae3c-ae931841b1e7" />


