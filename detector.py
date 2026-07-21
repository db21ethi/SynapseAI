import os
import cv2
import numpy as np
from ultralytics import YOLO

from config import *


class TrafficDetector:

    def __init__(self):

        print("\n" + "=" * 50)
        print("        SYNAPSE AI TRAFFIC ENGINE")
        print("=" * 50)

        print("Loading YOLOv8 model...")

        self.model = YOLO(MODEL_PATH)

        print("✓ YOLO Model Loaded Successfully\n")

        # Vehicle classes considered for traffic analysis
        self.vehicle_classes = {
            "car",
            "bus",
            "truck",
            "motorcycle",
            "bicycle"
        }

        # All detectable classes
        self.supported_classes = {
            "car",
            "bus",
            "truck",
            "motorcycle",
            "bicycle",
            "person"
        }

        # Future support
        self.emergency_classes = {
            "ambulance",
            "fire truck",
            "police car"
        }
            # =====================================================
    # COUNT OBJECTS
    # =====================================================

    def count_objects(self, boxes):

        counts = {
            "car": 0,
            "bus": 0,
            "truck": 0,
            "motorcycle": 0,
            "bicycle": 0,
            "person": 0
        }

        confidence_sum = 0
        detected = 0

        emergency_detected = False

        for box in boxes:

            cls = int(box.cls[0])

            confidence = float(box.conf[0])

            class_name = self.model.names[cls]

            # Ignore unsupported classes
            if class_name not in self.supported_classes:
                continue

            # Confidence filtering
            if confidence < CONFIDENCE:
                continue

            detected += 1

            confidence_sum += confidence

            if class_name in counts:
                counts[class_name] += 1

            # Reserved for future custom emergency model
            if class_name in self.emergency_classes:
                emergency_detected = True

        average_confidence = (
            round(confidence_sum / detected, 2)
            if detected > 0 else 0
        )

        return {

            "counts": counts,

            "average_confidence": average_confidence,

            "objects_detected": detected,

            "emergency_vehicle": emergency_detected

        }
            # =====================================================
    # CALCULATE TRAFFIC LOAD
    # =====================================================

    def calculate_load(self, counts):

        score = 0

        for vehicle, weight in VEHICLE_WEIGHTS.items():

            score += counts.get(vehicle, 0) * weight

        # Bonus score for pedestrians
        score += counts.get("person", 0) * 0.5

        return round(score, 2)


    # =====================================================
    # CALCULATE TRAFFIC DENSITY
    # =====================================================

    def density(self, score):

        if score <= LOW_LIMIT:

            return {
                "density": "LOW",
                "green_time": LOW_GREEN,
                "priority": 1
            }

        elif score <= MEDIUM_LIMIT:

            return {
                "density": "MEDIUM",
                "green_time": MEDIUM_GREEN,
                "priority": 2
            }

        elif score <= HIGH_LIMIT:

            return {
                "density": "HIGH",
                "green_time": HIGH_GREEN,
                "priority": 3
            }

        else:

            return {
                "density": "VERY HIGH",
                "green_time": VERY_HIGH_GREEN,
                "priority": 4
            }
                # =====================================================
    # ANALYZE IMAGE
    # =====================================================

    def analyze_image(self, image_path):

        if not os.path.exists(image_path):
            raise FileNotFoundError(image_path)

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError("Unable to read image.")

        # -----------------------------
        # YOLO Detection
        # -----------------------------

        results = self.model(

            image,

            conf=CONFIDENCE,

            verbose=False

        )

        result = results[0]

        annotated = result.plot()

        os.makedirs("output", exist_ok=True)

        cv2.imwrite(
            OUTPUT_IMAGE,
            annotated
        )

        # -----------------------------
        # Object Counting
        # -----------------------------

        detection = self.count_objects(result.boxes)

        counts = detection["counts"]

        avg_conf = detection["average_confidence"]

        detected = detection["objects_detected"]

        emergency = detection["emergency_vehicle"]

        # -----------------------------
        # Total Vehicles
        # -----------------------------

        total_vehicles = (

            counts["car"] +

            counts["bus"] +

            counts["truck"] +

            counts["motorcycle"] +

            counts["bicycle"]

        )

        # -----------------------------
        # Traffic Score
        # -----------------------------

        traffic_score = self.calculate_load(counts)

        traffic = self.density(traffic_score)

        # -----------------------------
        # Congestion %
        # -----------------------------

        congestion = min(

            round((traffic_score / HIGH_LIMIT) * 100, 1),

            100

        )

        # -----------------------------
        # AI Report
        # -----------------------------

        report = {

            "Cars": counts["car"],

            "Buses": counts["bus"],

            "Trucks": counts["truck"],

            "Motorcycles": counts["motorcycle"],

            "Bicycles": counts["bicycle"],

            "Persons": counts["person"],

            "Total Vehicles": total_vehicles,

            "Objects Detected": detected,

            "Average Confidence": avg_conf,

            "Emergency Vehicle": emergency,

            "Traffic Load Score": traffic_score,

            "Congestion (%)": congestion,

            "Traffic Density": traffic["density"],

            "Recommended Green Time": traffic["green_time"],

            "Priority Level": traffic["priority"],

            "Output Image": OUTPUT_IMAGE

        }

        return report
        # =====================================================
# TESTING
# =====================================================

if __name__ == "__main__":

    detector = TrafficDetector()

    report = detector.analyze_image(IMAGE_PATH)

    print("\n" + "=" * 60)
    print("             SYNAPSE AI DETECTION REPORT")
    print("=" * 60)

    for key, value in report.items():
        print(f"{key:<30}: {value}")

    print("=" * 60)
    print("✓ Analysis Completed Successfully")