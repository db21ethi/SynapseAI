# =====================================================
# SYNAPSE AI CONFIGURATION
# =====================================================

import os

# =====================================================
# YOLO MODEL
# =====================================================

MODEL_PATH = "yolov8n.pt"

CONFIDENCE = 0.35

# =====================================================
# PATHS
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

OUTPUT_IMAGE = os.path.join(
    OUTPUT_FOLDER,
    "detected_image.jpg"
)

OUTPUT_VIDEO = os.path.join(
    OUTPUT_FOLDER,
    "processed_video.mp4"
)

# Optional test files

IMAGE_PATH = "sample.jpg"

VIDEO_PATH = "sample.mp4"

# Create folders automatically

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

os.makedirs(REPORT_FOLDER, exist_ok=True)

# =====================================================
# VEHICLE WEIGHTS
# =====================================================

VEHICLE_WEIGHTS = {

    "car": 1,

    "motorcycle": 0.6,

    "bicycle": 0.4,

    "bus": 3,

    "truck": 4

}
# =====================================================
# TRAFFIC DENSITY THRESHOLDS
# =====================================================

LOW_LIMIT = 15

MEDIUM_LIMIT = 35

HIGH_LIMIT = 60

# =====================================================
# AI GREEN SIGNAL TIMINGS (Seconds)
# =====================================================

LOW_GREEN = 15

MEDIUM_GREEN = 30

HIGH_GREEN = 45

VERY_HIGH_GREEN = 60

# =====================================================
# DASHBOARD COLORS
# =====================================================

PRIMARY_COLOR = "#2563EB"

SUCCESS_COLOR = "#16A34A"

WARNING_COLOR = "#F59E0B"

DANGER_COLOR = "#DC2626"

BACKGROUND_COLOR = "#111827"

TEXT_COLOR = "#FFFFFF"

# =====================================================
# ANALYTICS CONSTANTS
# =====================================================

FUEL_CONSUMPTION_PER_SECOND = 0.00035

CO2_PER_LITRE = 2.31

MAX_WAIT_TIME = 60

# =====================================================
# PDF SETTINGS
# =====================================================

REPORT_TITLE = "Synapse AI Report"

PROJECT_NAME = "Synapse AI"

PROJECT_DESCRIPTION = (
    "AI Powered Smart Traffic Management System"
)

# =====================================================
# VERSION
# =====================================================

VERSION = "2.0.0"

AUTHOR = "Synapse AI Team"

COPYRIGHT = "© 2026 Synapse AI"