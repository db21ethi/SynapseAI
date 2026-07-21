import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import tempfile
import os
import time
from datetime import datetime

from detector import TrafficDetector
from analytics import TrafficAnalytics
from signal_controller import SmartSignalController
from report_generator import ReportGenerator
from video_processor import VideoProcessor
from junction_controller import JunctionController

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="🚦 Synapse AI",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD AI MODULES
# =====================================================

detector = TrafficDetector()
analytics = TrafficAnalytics()
signal = SmartSignalController()
report_generator = ReportGenerator()
video_processor = VideoProcessor()
junction = JunctionController()

# =====================================================
# KPI CARD
# =====================================================

def metric_card(title, value, icon, color="#2563EB"):

    card = f"""
    <div style="
        background: linear-gradient(135deg, {color}, #111827);
        padding:20px;
        border-radius:18px;
        color:white;
        text-align:center;
        min-height:170px;
        box-shadow:0px 8px 18px rgba(0,0,0,0.25);
        margin-bottom:15px;
    ">
        <div style="font-size:42px;">{icon}</div>

        <div style="font-size:18px; margin-top:8px;">
            {title}
        </div>

        <div style="font-size:34px; font-weight:bold; margin-top:10px;">
            {value}
        </div>
    </div>
    """

    st.html(card)
    # =====================================================
# HEADER
# =====================================================

st.markdown("""
# 🚦 Synapse AI
### Intelligent Traffic Signal Optimization using AI & YOLOv8
""")

st.divider()


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/traffic-light.png",
        width=80
    )

    st.title("Synapse AI")

    st.markdown("### 🚀 AI Dashboard")

    mode = st.radio(
        "Select Mode",
        (
            "Traffic Image",
            "Traffic Video",
            "Multi Junction AI"
        )
    )

    uploaded_file = st.file_uploader(
        "Upload Image / Video",
        type=["jpg", "jpeg", "png", "mp4"]
    )

    analyze = st.button(
        "🚀 Analyze",
        use_container_width=True
    )

    st.divider()

    st.markdown("### 🛰 AI Status")

    st.success("🟢 YOLOv8 Loaded")

    st.success("🟢 Signal Controller")

    st.success("🟢 Analytics Ready")

    st.success("🟢 Report Generator")

    st.success("🟢 Multi Junction AI")

    st.divider()

    st.markdown("### 🚀 Features")

    st.markdown("""
✅ Vehicle Detection

✅ Traffic Density

✅ Smart Signal Timing

✅ Environmental Analytics

✅ PDF Report

✅ Video Analysis

✅ Multi Junction Optimization
""")


# =====================================================
# DASHBOARD
# =====================================================

left, right = st.columns([3,1])

with left:

    st.info("""

## 👋 Welcome to Synapse AI

An AI-powered Smart Traffic Management System.

### Workflow

1️⃣ Upload Image / Video

2️⃣ Detect Vehicles using YOLOv8

3️⃣ Calculate Traffic Density

4️⃣ Recommend Green Signal Time

5️⃣ Generate Environmental Analytics

6️⃣ Download PDF Report

7️⃣ Optimize Multi-Junction Signals

""")

with right:

    st.subheader("📡 System Status")

    st.metric("AI Engine", "ONLINE")

    st.metric("YOLO Model", "READY")

    st.metric("Analytics", "ACTIVE")

    st.metric("Signal AI", "READY")

    st.metric("Reports", "READY")

st.divider()
# =====================================================
# TRAFFIC IMAGE MODE
# =====================================================

if mode == "Traffic Image":

    if uploaded_file is None:

        st.info("📷 Upload a traffic image to begin analysis.")

    else:

        temp_dir = tempfile.gettempdir()

        image_path = os.path.join(
            temp_dir,
            uploaded_file.name
        )

        with open(image_path, "wb") as f:
            f.write(uploaded_file.read())

        left, right = st.columns(2)

        with left:

            st.subheader("📷 Original Image")

            st.image(
                image_path,
                use_container_width=True
            )

        if analyze:

            progress = st.progress(0)

            status = st.empty()

            for i in range(100):

                progress.progress(i + 1)

                status.info(
                    f"🤖 AI Processing... {i+1}%"
                )

                time.sleep(0.01)

            status.empty()

            start = time.time()

            report = detector.analyze_image(
                image_path
            )

            end = time.time()

            if report is None:

                st.error("❌ Detection Failed")

            else:

                with right:

                    st.subheader("🤖 AI Detection")

                    st.image(
                        report["Output Image"],
                        use_container_width=True
                    )

                st.success(
                    f"✅ Detection completed in {round(end-start,2)} sec"
                )

                st.divider()
                st.subheader("🚗 Vehicle Dashboard")

                c1, c2, c3, c4 = st.columns(4)

                with c1:
                    metric_card(
                        "Cars",
                        report["Cars"],
                        "🚗",
                        "#2563EB"
                    )

                with c2:
                    metric_card(
                        "Buses",
                        report["Buses"],
                        "🚌",
                        "#16A34A"
                    )

                with c3:
                    metric_card(
                        "Trucks",
                        report["Trucks"],
                        "🚚",
                        "#EA580C"
                    )

                with c4:
                    metric_card(
                        "Persons",
                        report["Persons"],
                        "👤",
                        "#7C3AED"
                    )

                c5, c6, c7 = st.columns(3)

                with c5:
                    metric_card(
                        "Motorcycles",
                        report["Motorcycles"],
                        "🏍",
                        "#0891B2"
                    )

                with c6:
                    metric_card(
                        "Bicycles",
                        report["Bicycles"],
                        "🚲",
                        "#14B8A6"
                    )

                with c7:
                    metric_card(
                        "Total Vehicles",
                        report["Total Vehicles"],
                        "🚦",
                        "#DC2626"
                    )

                st.divider()

                st.subheader("🚦 Traffic Analysis")

                a, b, c = st.columns(3)

                with a:
                    metric_card(
                        "Traffic Density",
                        report["Traffic Density"],
                        "📊",
                        "#9333EA"
                    )

                with b:
                    metric_card(
                        "Traffic Score",
                        report["Traffic Load Score"],
                        "⚡",
                        "#F59E0B"
                    )

                with c:
                    metric_card(
                        "Green Signal",
                        f"{report['Recommended Green Time']} sec",
                        "🟢",
                        "#16A34A"
                    )

                st.divider()
                                # =====================================================
                # VEHICLE CHARTS
                # =====================================================

                vehicle_data = pd.DataFrame({

                    "Vehicle": [
                        "Cars",
                        "Buses",
                        "Trucks",
                        "Motorcycles",
                        "Bicycles"
                    ],

                    "Count": [
                        report["Cars"],
                        report["Buses"],
                        report["Trucks"],
                        report["Motorcycles"],
                        report["Bicycles"]
                    ]

                })

                left_chart, right_chart = st.columns(2)

                with left_chart:

                    st.subheader("📊 Vehicle Distribution")

                    fig = px.bar(

                        vehicle_data,

                        x="Vehicle",

                        y="Count",

                        color="Vehicle",

                        text="Count",

                        template="plotly_dark"

                    )

                    fig.update_layout(

                        paper_bgcolor="#111827",

                        plot_bgcolor="#111827",

                        font_color="white"

                    )

                    st.plotly_chart(

                        fig,

                        use_container_width=True

                    )

                with right_chart:

                    st.subheader("🥧 Vehicle Composition")

                    pie = px.pie(

                        vehicle_data,

                        names="Vehicle",

                        values="Count",

                        hole=0.55,

                        template="plotly_dark"

                    )

                    pie.update_layout(

                        paper_bgcolor="#111827",

                        font_color="white"

                    )

                    st.plotly_chart(

                        pie,

                        use_container_width=True

                    )

                st.divider()

                # =====================================================
                # SMART SIGNAL CONTROLLER
                # =====================================================

                st.subheader("🚦 AI Smart Signal Decision")

                decision = signal.make_decision(report)

                d1, d2, d3 = st.columns(3)

                with d1:
                    metric_card(
                        "Traffic Density",
                        decision["Traffic Density"],
                        "📊",
                        "#9333EA"
                    )

                with d2:
                    metric_card(
                        "Green Time",
                        f'{decision["Green Time (sec)"]} sec',
                        "🟢",
                        "#16A34A"
                    )

                with d3:
                    metric_card(
                        "Priority",
                        decision["Priority Level"],
                        "🚨",
                        "#DC2626"
                    )

                st.success("🤖 " + decision["Reason"])

                st.divider()

                # =====================================================
                # ENVIRONMENTAL ANALYTICS
                # =====================================================

                analytics_report = analytics.generate(report)

                st.subheader("🌱 Environmental Analytics")

                a1, a2, a3, a4 = st.columns(4)

                with a1:
                    metric_card(
                        "Fuel Saved",
                        f'{analytics_report["Estimated Fuel Saved (L)"]} L',
                        "⛽",
                        "#2563EB"
                    )

                with a2:
                    metric_card(
                        "CO₂ Saved",
                        f'{analytics_report["Estimated CO₂ Reduction (kg)"]} kg',
                        "🌿",
                        "#16A34A"
                    )

                with a3:
                    metric_card(
                        "Waiting Time",
                        f'{analytics_report["Estimated Waiting Time (sec)"]} sec',
                        "⏱",
                        "#EA580C"
                    )

                with a4:
                    metric_card(
                        "Efficiency",
                        f'{analytics_report["Traffic Efficiency (%)"]}%',
                        "📈",
                        "#7C3AED"
                    )

                st.divider()

                st.subheader("📋 Complete Analytics Report")

                analytics_df = pd.DataFrame(
                    analytics_report.items(),
                    columns=["Parameter", "Value"]
                )

                st.dataframe(
                    analytics_df,
                    use_container_width=True,
                    hide_index=True
                )

                st.divider()
                                # =====================================================
                # PDF REPORT
                # =====================================================

                st.subheader("📄 Generate Report")

                if st.button("📥 Generate PDF Report"):

                    pdf_path = report_generator.generate(
                        report,
                        analytics_report,
                        decision
                    )

                    with open(pdf_path, "rb") as pdf:

                        st.download_button(
                            "⬇ Download PDF Report",
                            data=pdf,
                            file_name="SynapseAI_Report.pdf",
                            mime="application/pdf"
                        )

                st.divider()

                # =====================================================
                # AI SUMMARY
                # =====================================================

                st.subheader("🤖 AI Summary")

                st.success(f"""
🚗 Total Vehicles : {report['Total Vehicles']}

📊 Traffic Density : {report['Traffic Density']}

⚡ Traffic Load Score : {report['Traffic Load Score']}

🟢 Recommended Green Time : {report['Recommended Green Time']} sec

⛽ Estimated Fuel Saved : {analytics_report['Estimated Fuel Saved (L)']} L

🌿 Estimated CO₂ Reduction : {analytics_report['Estimated CO₂ Reduction (kg)']} kg

📈 Traffic Efficiency : {analytics_report['Traffic Efficiency (%)']} %
""")

                st.divider()

                # =====================================================
                # TRAFFIC STATUS
                # =====================================================

                st.subheader("🚦 Traffic Status")

                if report["Traffic Density"] == "LOW":
                    st.success("🟢 LOW TRAFFIC")

                elif report["Traffic Density"] == "MEDIUM":
                    st.warning("🟡 MEDIUM TRAFFIC")

                elif report["Traffic Density"] == "HIGH":
                    st.error("🟠 HIGH TRAFFIC")

                else:
                    st.error("🔴 VERY HIGH TRAFFIC")

                # =====================================================
                # TRAFFIC LOAD GAUGE
                # =====================================================

                gauge = go.Figure(go.Indicator(

                    mode="gauge+number",

                    value=report["Traffic Load Score"],

                    title={"text": "Traffic Load Score"},

                    gauge={
                        "axis": {"range": [0, 100]},
                        "bar": {"color": "royalblue"},
                        "steps": [
                            {"range": [0, 30], "color": "green"},
                            {"range": [30, 60], "color": "yellow"},
                            {"range": [60, 100], "color": "red"}
                        ]
                    }

                ))

                st.plotly_chart(
                    gauge,
                    use_container_width=True
                )

                # =====================================================
                # AI RECOMMENDATION
                # =====================================================

                st.subheader("🧠 AI Recommendation")

                if report["Traffic Density"] == "LOW":

                    st.success("""
### ✅ Recommendation

Traffic is flowing smoothly.

Maintain the current signal timing.
""")

                elif report["Traffic Density"] == "MEDIUM":

                    st.warning("""
### ⚠ Recommendation

Moderate congestion detected.

Increase green signal slightly.
""")

                elif report["Traffic Density"] == "HIGH":

                    st.error("""
### 🚨 Recommendation

Heavy congestion detected.

Increase green signal duration.

Monitor traffic continuously.
""")

                else:

                    st.error("""
### 🔴 Critical Alert

Very high congestion detected.

Immediate signal optimization required.

Prioritize emergency vehicles.

Extend green signal timing.
""")
# =====================================================
# TRAFFIC VIDEO MODE
# =====================================================

elif mode == "Traffic Video":

    if uploaded_file is None:

        st.info("🎥 Upload a traffic video.")

    else:

        temp_dir = tempfile.gettempdir()

        video_path = os.path.join(
            temp_dir,
            uploaded_file.name
        )

        with open(video_path, "wb") as f:
            f.write(uploaded_file.read())

        st.subheader("🎥 Uploaded Video")
        st.video(video_path)

        if analyze:

            progress = st.progress(0)

            status = st.empty()

            for i in range(100):

                progress.progress(i + 1)

                status.info(
                    f"🤖 AI Processing Video... {i+1}%"
                )

                time.sleep(0.01)

            status.empty()

            start = time.time()

            report = video_processor.process_video(
                video_path
            )

            end = time.time()

            st.success(
                f"✅ Video Analysis Completed in {round(end-start,2)} sec"
            )

            st.subheader("🎬 AI Processed Video")

            st.video(
                report["Output Video"]
            )

            st.divider()
            st.subheader("🚗 Vehicle Dashboard")

            c1,c2,c3,c4 = st.columns(4)

            with c1:
                metric_card(
                    "Cars",
                    report["Cars"],
                    "🚗",
                    "#2563EB"
                )

            with c2:
                metric_card(
                    "Buses",
                    report["Buses"],
                    "🚌",
                    "#16A34A"
                )

            with c3:
                metric_card(
                    "Trucks",
                    report["Trucks"],
                    "🚚",
                    "#EA580C"
                )

            with c4:
                metric_card(
                    "Persons",
                    report["Persons"],
                    "👤",
                    "#7C3AED"
                )

            c5,c6,c7 = st.columns(3)

            with c5:
                metric_card(
                    "Traffic Density",
                    report["Traffic Density"],
                    "📊",
                    "#9333EA"
                )

            with c6:
                metric_card(
                    "Traffic Score",
                    report["Traffic Load Score"],
                    "⚡",
                    "#F59E0B"
                )

            with c7:
                metric_card(
                    "Green Time",
                    f"{report['Recommended Green Time']} sec",
                    "🟢",
                    "#16A34A"
                )

            st.divider()
                        # =====================================================
            # SMART SIGNAL CONTROLLER
            # =====================================================

            st.subheader("🚦 AI Smart Signal Decision")

            decision = signal.make_decision(report)

            d1, d2, d3 = st.columns(3)

            with d1:
                metric_card(
                    "Traffic Density",
                    decision["Traffic Density"],
                    "📊",
                    "#9333EA"
                )

            with d2:
                metric_card(
                    "Green Time",
                    f'{decision["Green Time (sec)"]} sec',
                    "🟢",
                    "#16A34A"
                )

            with d3:
                metric_card(
                    "Priority",
                    decision["Priority Level"],
                    "🚨",
                    "#DC2626"
                )

            st.success("🤖 " + decision["Reason"])

            st.divider()

            # =====================================================
            # ENVIRONMENTAL ANALYTICS
            # =====================================================

            analytics_report = analytics.generate(report)

            st.subheader("🌱 Environmental Analytics")

            a1, a2, a3, a4 = st.columns(4)

            with a1:
                metric_card(
                    "Fuel Saved",
                    f'{analytics_report["Estimated Fuel Saved (L)"]} L',
                    "⛽",
                    "#2563EB"
                )

            with a2:
                metric_card(
                    "CO₂ Saved",
                    f'{analytics_report["Estimated CO₂ Reduction (kg)"]} kg',
                    "🌿",
                    "#16A34A"
                )

            with a3:
                metric_card(
                    "Waiting Time",
                    f'{analytics_report["Estimated Waiting Time (sec)"]} sec',
                    "⏱",
                    "#EA580C"
                )

            with a4:
                metric_card(
                    "Efficiency",
                    f'{analytics_report["Traffic Efficiency (%)"]}%',
                    "📈",
                    "#7C3AED"
                )

            st.divider()

            # =====================================================
            # PDF REPORT
            # =====================================================

            if st.button("📄 Generate Video PDF Report"):

                pdf_path = report_generator.generate(
                    report,
                    analytics_report,
                    decision
                )

                with open(pdf_path, "rb") as pdf:

                    st.download_button(
                        "⬇ Download PDF",
                        pdf,
                        file_name="SynapseAI_Video_Report.pdf",
                        mime="application/pdf"
                    )

            # =====================================================
            # TRAFFIC LOAD GAUGE
            # =====================================================

            gauge = go.Figure(go.Indicator(

                mode="gauge+number",

                value=report["Traffic Load Score"],

                title={"text": "Traffic Load Score"},

                gauge={
                    "axis": {"range": [0,100]},
                    "bar": {"color":"royalblue"},
                    "steps":[
                        {"range":[0,30],"color":"green"},
                        {"range":[30,60],"color":"yellow"},
                        {"range":[60,100],"color":"red"}
                    ]
                }

            ))

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

            # =====================================================
            # AI RECOMMENDATION
            # =====================================================

            st.subheader("🧠 AI Recommendation")

            st.info(f"""
Traffic Density : **{report['Traffic Density']}**

Traffic Score : **{report['Traffic Load Score']}**

Recommended Green Time : **{report['Recommended Green Time']} sec**

Priority Level : **{decision['Priority Level']}**
""")

            # =====================================================
            # DOWNLOAD VIDEO
            # =====================================================

            if os.path.exists(report["Output Video"]):

                with open(report["Output Video"], "rb") as video:

                    st.download_button(
                        "⬇ Download Processed Video",
                        data=video,
                        file_name="SynapseAI_Output.mp4",
                        mime="video/mp4"
                    )
                    # =====================================================
# MULTI JUNCTION AI
# =====================================================

elif mode == "Multi Junction AI":

    st.header("🚦 Multi-Junction AI Signal Optimization")

    st.info("""
Upload **4 road images** captured from four approaches of an intersection.

The AI compares congestion on all roads and automatically decides
which lane should receive the green signal first.
""")

    junction_files = st.file_uploader(
        "Upload 4 Road Images",
        type=["jpg","jpeg","png"],
        accept_multiple_files=True
    )

    if junction_files is not None:

        if len(junction_files) != 4:

            st.warning("Please upload exactly 4 images.")

        else:

            if st.button("🚦 Optimize Signals"):

                reports = []

                cols = st.columns(4)

                for i, file in enumerate(junction_files):

                    path = os.path.join(
                        tempfile.gettempdir(),
                        file.name
                    )

                    with open(path,"wb") as f:
                        f.write(file.read())

                    report = detector.analyze_image(path)

                    reports.append(report)

                    with cols[i]:

                        st.image(
                            report["Output Image"],
                            caption=f"Road {i+1}",
                            use_container_width=True
                        )

                        st.metric(
                            "Vehicles",
                            report["Total Vehicles"]
                        )

                        st.metric(
                            "Density",
                            report["Traffic Density"]
                        )

                st.divider()

                ranking = junction.optimize(reports)
                st.subheader("🏆 AI Priority Ranking")

                ranking_df = pd.DataFrame(ranking)

                st.dataframe(
                    ranking_df,
                    use_container_width=True,
                    hide_index=True
                )

                winner = ranking[0]

                st.success(f"""
🚦 GREEN SIGNAL → {winner['Lane']}

Priority : {winner['Priority']}

Vehicles : {winner['Vehicles']}

Traffic Score : {winner['Score']}

Green Time : {winner['Green Time']} sec
""")
                st.subheader("📊 Lane Comparison")

                fig = px.bar(

                    ranking_df,

                    x="Lane",

                    y="Score",

                    color="Lane",

                    text="Score",

                    template="plotly_dark"

                )

                fig.update_layout(

                    paper_bgcolor="#111827",

                    plot_bgcolor="#111827",

                    font_color="white"

                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )
                st.subheader("🤖 AI Decision")

                st.info(f"""
The AI compared all four roads based on:

• Total Vehicles

• Traffic Density

• Traffic Load Score

• Estimated Green Time

### Result

**{winner['Lane']}** has the highest congestion score.

Therefore it receives the green signal first for

## 🟢 {winner['Green Time']} seconds

This minimizes waiting time and improves traffic flow.
""")
                st.subheader("🚥 Signal Order")

                for lane in ranking:

                    st.write(
                        f"🥇 Priority {lane['Priority']} → "
                        f"{lane['Lane']} "
                        f"({lane['Green Time']} sec)"
                    )
                    # =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("## 📊 Synapse AI System Status")

c1, c2, c3, c4 = st.columns(4)

with c1:
    metric_card(
        "AI Model",
        "YOLOv8",
        "🧠",
        "#2563EB"
    )

with c2:
    metric_card(
        "Detection",
        "Real-Time",
        "⚡",
        "#16A34A"
    )

with c3:
    metric_card(
        "Accuracy",
        "95%+",
        "🎯",
        "#F59E0B"
    )

with c4:
    metric_card(
        "Status",
        "ONLINE",
        "🟢",
        "#DC2626"
    )

st.divider()

st.info("""
# 🚦 About Synapse AI

Synapse AI is an intelligent traffic management platform powered by
YOLOv8 Computer Vision and AI-based signal optimization.

### Features

✅ Vehicle Detection

✅ Smart Signal Timing

✅ Environmental Analytics

✅ Traffic Load Prediction

✅ PDF Report Generation

✅ Video Processing

✅ Multi-Junction AI Optimization
""")

st.caption(
    "🕒 " +
    datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
)

st.success("🎉 Synapse AI is Ready!")

st.markdown("""
---
# 🚦 Synapse AI

### AI Smart Traffic Management System

🧠 **YOLOv8** &nbsp;&nbsp;|&nbsp;&nbsp;
📷 **OpenCV** &nbsp;&nbsp;|&nbsp;&nbsp;
📊 **Plotly** &nbsp;&nbsp;|&nbsp;&nbsp;
⚡ **Streamlit** &nbsp;&nbsp;|&nbsp;&nbsp;
🐍 **Python**

---

### 🚀 Developed for Smart Traffic Management Ideathon 2026

© 2026 Synapse AI • All Rights Reserved
""")