import os
import cv2
from ultralytics import YOLO

from config import *


class VideoProcessor:

    def __init__(self):

        print("✓ Video Processor Ready")

        self.model = YOLO(MODEL_PATH)

        self.vehicle_classes = {

            "car",
            "bus",
            "truck",
            "motorcycle",
            "bicycle"

        }
            # =====================================================
    # PROCESS SINGLE FRAME
    # =====================================================

    def process_frame(self, frame):

        results = self.model(

            frame,

            conf=CONFIDENCE,

            verbose=False

        )

        result = results[0]

        annotated = result.plot()

        counts = {

            "car": 0,

            "bus": 0,

            "truck": 0,

            "motorcycle": 0,

            "bicycle": 0,

            "person": 0

        }

        score = 0

        for box in result.boxes:

            cls = int(box.cls[0])

            name = self.model.names[cls]

            if name in counts:

                counts[name] += 1

        # Weighted Traffic Score

        score += counts["car"] * VEHICLE_WEIGHTS["car"]

        score += counts["bus"] * VEHICLE_WEIGHTS["bus"]

        score += counts["truck"] * VEHICLE_WEIGHTS["truck"]

        score += counts["motorcycle"] * VEHICLE_WEIGHTS["motorcycle"]

        score += counts["bicycle"] * VEHICLE_WEIGHTS["bicycle"]

        # Traffic Density

        if score < LOW_LIMIT:

            density = "LOW"

            green = LOW_GREEN

        elif score < MEDIUM_LIMIT:

            density = "MEDIUM"

            green = MEDIUM_GREEN

        elif score < HIGH_LIMIT:

            density = "HIGH"

            green = HIGH_GREEN

        else:

            density = "VERY HIGH"

            green = VERY_HIGH_GREEN

        report = {

            "Cars": counts["car"],

            "Buses": counts["bus"],

            "Trucks": counts["truck"],

            "Motorcycles": counts["motorcycle"],

            "Bicycles": counts["bicycle"],

            "Persons": counts["person"],

            "Total Vehicles":

                counts["car"]

                + counts["bus"]

                + counts["truck"]

                + counts["motorcycle"]

                + counts["bicycle"],

            "Traffic Load Score": round(score, 2),

            "Traffic Density": density,

            "Recommended Green Time": green

        }

        return annotated, report
            # =====================================================
    # PROCESS VIDEO
    # =====================================================

    def process_video(self, video_path):

        if not os.path.exists(video_path):
            raise FileNotFoundError(video_path)

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            raise ValueError("Unable to open video.")

        os.makedirs("output", exist_ok=True)

        output_path = "output/output_video.mp4"

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        writer = cv2.VideoWriter(
            output_path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (width, height)
        )

        frame_count = 0

        total_cars = 0
        total_buses = 0
        total_trucks = 0
        total_motorcycles = 0
        total_bicycles = 0
        total_persons = 0

        total_score = 0

        last_density = "LOW"
        last_green = LOW_GREEN

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            annotated, report = self.process_frame(frame)

            writer.write(annotated)

            frame_count += 1

            total_cars += report["Cars"]
            total_buses += report["Buses"]
            total_trucks += report["Trucks"]
            total_motorcycles += report["Motorcycles"]
            total_bicycles += report["Bicycles"]
            total_persons += report["Persons"]

            total_score += report["Traffic Load Score"]

            last_density = report["Traffic Density"]
            last_green = report["Recommended Green Time"]

        cap.release()
        writer.release()

        if frame_count == 0:
            frame_count = 1

        avg_cars = round(total_cars / frame_count)
        avg_buses = round(total_buses / frame_count)
        avg_trucks = round(total_trucks / frame_count)
        avg_motorcycles = round(total_motorcycles / frame_count)
        avg_bicycles = round(total_bicycles / frame_count)
        avg_persons = round(total_persons / frame_count)

        avg_score = round(total_score / frame_count, 2)

        final_report = {

            "Cars": avg_cars,

            "Buses": avg_buses,

            "Trucks": avg_trucks,

            "Motorcycles": avg_motorcycles,

            "Bicycles": avg_bicycles,

            "Persons": avg_persons,

            "Total Vehicles":
                avg_cars +
                avg_buses +
                avg_trucks +
                avg_motorcycles +
                avg_bicycles,

            "Traffic Load Score": avg_score,

            "Traffic Density": last_density,

            "Recommended Green Time": last_green,

            "Output Video": output_path

        }

        return final_report
        # =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    processor = VideoProcessor()

    report = processor.process_video(VIDEO_PATH)

    print("\n" + "=" * 60)
    print("         SYNAPSE AI VIDEO REPORT")
    print("=" * 60)

    for key, value in report.items():
        print(f"{key:<30}: {value}")

    print("=" * 60)
    print("✓ Video Processing Completed Successfully")