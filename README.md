# 🚦 AI-Powered Real-Time Vehicle Detection & Traffic Counter (YOLOv8)

## 🔹 Project Overview

This project uses **YOLOv8 (You Only Look Once v8)** for real-time **vehicle detection, tracking, and counting** from CCTV or live video streams. It not only detects different types of vehicles (car, bike, bus, truck, etc.), but also **tracks each vehicle** as it moves and **counts them** accurately.

The system can overlay live detection results on the video and store/export **traffic analytics**, which can help in **smart traffic monitoring** and **congestion management**.

---

## 🔹 Key Features

1. **Real-Time Vehicle Detection**

   * Detects vehicles in every video frame using **YOLOv8 deep learning model**.
   * Works with CCTV cameras, dashcams, or video files.

2. **Vehicle Classification**

   * Identifies **vehicle type** (car, bus, truck, motorcycle, bicycle, etc.).
   * Can be extended to detect emergency vehicles (ambulance, police car).

3. **Object Tracking**

   * Uses object tracking algorithms like **DeepSORT/ByteTrack**.
   * Assigns a **unique ID** to each vehicle → avoids double-counting.

4. **Traffic Counting**

   * Counts vehicles crossing a **virtual line/region of interest (ROI)**.
   * Maintains per-class counts (cars = 120, bikes = 50, trucks = 30, etc.).

5. **Live Video Overlay**

   * Shows bounding boxes, labels, and counts **directly on the live feed**.

6. **Exportable Analytics**

   * Stores data in **CSV/Excel/Database**.
   * Can generate **graphs & reports** (vehicles/hour, peak traffic time, congestion trends).

---

## 🔹 How the Project Works (Step-by-Step Flow)

1. **Input Source**

   * Video feed (CCTV/live webcam/video file).

2. **Vehicle Detection (YOLOv8)**

   * Each video frame → YOLOv8 model → Detect objects.
   * Output: bounding box, confidence score, class (car, truck, bus…).

3. **Vehicle Tracking (DeepSORT/ByteTrack)**

   * Assigns unique ID to each detected vehicle.
   * Tracks it across multiple frames.

4. **Counting Mechanism**

   * Define a **counting line/region**.
   * When a vehicle with a unique ID crosses the line → count increases.

5. **Overlay Results**

   * Display bounding boxes, IDs, class labels, and counters on the live feed.

6. **Data Export & Analytics**

   * Store counts in CSV/Database.
   * Generate charts (traffic volume per hour, per vehicle type).

---

## 🔹 Tools & Technologies

* **Programming Language**: Python
* **Deep Learning Model**: YOLOv8 (Ultralytics)
* **Tracking**: DeepSORT / ByteTrack
* **Libraries**: OpenCV, NumPy, Pandas, Matplotlib, Ultralytics YOLO
* **Optional Storage**: Firebase / MySQL / MongoDB for analytics
* **Deployment Options**: Local system, Raspberry Pi, or Cloud (AWS, GCP, Azure)

---

## 🔹 Benefits

1. **Traffic Management**

   * Detect traffic jams in real-time.
   * Identify busiest routes and peak hours.

2. **Accurate Vehicle Counts**

   * Replaces manual counting or loop detectors.
   * Can separate counts by vehicle type.

3. **Congestion Analysis**

   * Helps governments & city planners design better infrastructure.
   * Useful for smart city projects.

4. **Law Enforcement**

   * Identify illegal parking, wrong-way driving.
   * Helps with surveillance and accident analysis.

5. **Scalability**

   * Can integrate with **IoT & cloud dashboards** for real-time monitoring of multiple locations.

---

## 🔹 Real-Life Use Cases

* **Smart Traffic Lights** → Adjust signal timings based on real-time vehicle count.
* **Toll Booth Automation** → Count and classify vehicles automatically.
* **Highway Traffic Monitoring** → Monitor vehicle flow and congestion patterns.
* **Accident Detection** → Detect sudden vehicle stops or wrong-way driving.
* **Parking Lot Management** → Count available spots and detect vehicles.

---

## 🔹 Example Output

* **On Screen**: Live video with bounding boxes, labels (`Car 87%`), and counters (`Cars: 120, Bikes: 50, Trucks: 30`).
* **Saved File (CSV/Excel)**:

| Time        | Cars | Bikes | Trucks | Buses | Total |
| ----------- | ---- | ----- | ------ | ----- | ----- |
| 08:00-09:00 | 120  | 60    | 20     | 5     | 205   |
| 09:00-10:00 | 150  | 70    | 30     | 8     | 258   |

---

✅ In short:
This project **uses AI (YOLOv8) + tracking** to **detect, track, and count vehicles in real-time**, producing **live overlays and analytics**. It is highly useful for **traffic management, smart cities, and law enforcement**.

---
<img width="1429" height="732" alt="Screenshot 2025-08-25 at 1 35 25 AM" src="https://github.com/user-attachments/assets/3a6e6fd2-eeaa-4995-8e8f-5a8536f761a8" />

