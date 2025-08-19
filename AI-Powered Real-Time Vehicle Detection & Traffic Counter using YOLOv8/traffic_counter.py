import cv2
import csv
import numpy as np
from ultralytics import YOLO
import os

# --- Setup and Configuration ---

# Choose source: 
#  - Put a video filename (e.g., "input_video.mp4")
#  - Or set to 0 for webcam
VIDEO_PATH = "input_video.mp4"   # change to 0 for webcam

# Paths for outputs
OUTPUT_VIDEO_PATH = "output_video_with_counts.mp4"
OUTPUT_CSV_PATH = "vehicle_log.csv"

# Counting lines [(x1, y1), (x2, y2)]
COUNTING_LINES = [
    ((100, 500), (900, 500))  # example horizontal line
]

line_counts = {i: 0 for i in range(len(COUNTING_LINES))}
counted_vehicle_ids = set()
vehicle_log = []

# --- Model and Video Initialization ---
model = YOLO("yolov8n.pt")

# If VIDEO_PATH is a string but file doesn't exist → switch to webcam
if isinstance(VIDEO_PATH, str) and not os.path.exists(VIDEO_PATH):
    print(f"⚠️ Video file '{VIDEO_PATH}' not found. Switching to webcam...")
    VIDEO_PATH = 0

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print(f"❌ Error: Could not open video source '{VIDEO_PATH}'.")
    exit()

# Get video properties (use defaults if webcam)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)
fps = int(cap.get(cv2.CAP_PROP_FPS) or 30)

# Save video only if source is a file (not webcam)
out = None
if isinstance(VIDEO_PATH, str):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (frame_width, frame_height))

print("✅ Starting detection... Press 'q' to quit.")

# --- Main Loop ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("✔️ End of video stream.")
        break

    # Run YOLO object detection + tracking
    results = model.track(frame, persist=True, tracker="bytetrack.yaml", verbose=False)

    if results and results[0].boxes:
        boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
        ids = results[0].boxes.id.cpu().numpy().astype(int)
        clss = results[0].boxes.cls.cpu().numpy().astype(int)

        for box, track_id, cls_id in zip(boxes, ids, clss):
            x_center = int((box[0] + box[2]) / 2)
            y_center = int((box[1] + box[3]) / 2)
            center_point = (x_center, y_center)

            # Draw detection
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {track_id}", (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Check line crossing
            for line_idx, line_coords in enumerate(COUNTING_LINES):
                x1, y1 = line_coords[0]
                x2, y2 = line_coords[1]

                is_on_line = False
                if y1 == y2:  # horizontal line
                    is_on_line = (y_center in range(y1 - 5, y1 + 5))
                elif x1 == x2:  # vertical line
                    is_on_line = (x_center in range(x1 - 5, x1 + 5))

                if is_on_line and (track_id, line_idx) not in counted_vehicle_ids:
                    line_counts[line_idx] += 1
                    counted_vehicle_ids.add((track_id, line_idx))
                    current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
                    vehicle_log.append([track_id, line_idx + 1, f"{current_time_ms/1000:.2f}s"])
                    print(f"🚗 Vehicle {track_id} crossed line {line_idx+1} → Count: {line_counts[line_idx]}")

    # Draw lines & counts
    for line_coords in COUNTING_LINES:
        cv2.line(frame, line_coords[0], line_coords[1], (255, 0, 0), 2)

    for line_idx, count in line_counts.items():
        text_pos = (COUNTING_LINES[line_idx][0][0] + 20, COUNTING_LINES[line_idx][0][1] - 20)
        cv2.putText(frame, f"Lane {line_idx+1} Count: {count}", text_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Save if video, else show live
    if out:
        out.write(frame)

    cv2.imshow("Traffic Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# --- Cleanup ---
cap.release()
if out:
    out.release()
cv2.destroyAllWindows()

# Save CSV
try:
    with open(OUTPUT_CSV_PATH, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Vehicle ID", "Lane No.", "Timestamp (s)"])
        writer.writerows(vehicle_log)
    print(f"📄 Vehicle log saved: {OUTPUT_CSV_PATH}")
except IOError as e:
    print(f"❌ Error saving CSV file: {e}")

print("✅ Project execution complete.")
