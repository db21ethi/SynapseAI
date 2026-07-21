# 🚦 Synapse AI

### AI-Powered Smart Traffic Signal Optimization using YOLOv8

Synapse AI is an intelligent traffic management system that uses **YOLOv8 Computer Vision**, **Streamlit**, and **Artificial Intelligence** to detect traffic density, optimize signal timing, analyze videos, and manage multiple road junctions.

---

## 🌟 Features

✅ Vehicle Detection using YOLOv8

✅ Smart Traffic Density Analysis

✅ AI-based Green Signal Recommendation

✅ Image Traffic Analysis

✅ Video Traffic Analysis

✅ Multi-Junction Signal Optimization

✅ Environmental Analytics

✅ Traffic Load Score Calculation

✅ Interactive Dashboard

✅ PDF Report Generation

---

## 🛠 Tech Stack

- Python
- YOLOv8
- OpenCV
- Streamlit
- Plotly
- Pandas
- NumPy
- FPDF

---

## 📂 Project Structure

```
SynapseAI/
│
├── app.py
├── detector.py
├── analytics.py
├── signal_controller.py
├── report_generator.py
├── video_processor.py
├── junction_controller.py
├── config.py
├── requirements.txt
│
├── models/
│     yolov8n.pt
│
├── samples/
│
├── output/
│
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/db21ethi/SynapseAI.git
```

Move into the project folder

```bash
cd SynapseAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🚦 Working

### Image Mode

- Upload a traffic image
- Detect vehicles
- Calculate traffic density
- Recommend green signal timing

---

### Video Mode

- Upload a traffic video
- Detect vehicles frame-by-frame
- Generate processed video
- Produce analytics dashboard

---

### Multi-Junction AI

Upload four road images.

The AI compares all four lanes based on:

- Vehicle Count
- Traffic Density
- Traffic Load Score
- Green Signal Time

Then automatically selects the lane that should receive the green signal first.

---

## 📊 Analytics

The system generates:

- Vehicle Count
- Traffic Load Score
- Traffic Density
- Recommended Green Time
- Fuel Saving Estimation
- CO₂ Reduction
- Traffic Efficiency
- Waiting Time Analysis

---

## 📄 Report Generation

Synapse AI automatically generates a downloadable PDF report containing:

- Vehicle Statistics
- Traffic Analytics
- Environmental Analytics
- Signal Recommendation

---

## 🎯 Future Improvements

- Emergency Vehicle Detection
- Number Plate Recognition
- Live CCTV Integration
- Cloud Deployment
- AI Traffic Prediction
- IoT Signal Integration

---

## 👩‍💻 Developer

**Dharshini Baskaran**

GitHub: https://github.com/db21ethi

---

## 📜 License

This project is licensed under the MIT License.

---

# ⭐ If you like this project, please consider giving it a Star!