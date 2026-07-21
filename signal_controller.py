# =====================================================
# SYNAPSE AI
# Smart Signal Controller
# =====================================================

from config import *


class SmartSignalController:

    def __init__(self):

        print("✓ Smart Signal Controller Ready")
            # =====================================================
    # AI SIGNAL DECISION
    # =====================================================

    def make_decision(self, report):

        density = report["Traffic Density"]

        score = report["Traffic Load Score"]

        green_time = report["Recommended Green Time"]

        emergency = report.get("Emergency Vehicle", False)

        # -------------------------------------
        # Emergency Override
        # -------------------------------------

        if emergency:

            return {

                "Traffic Density": density,

                "Green Time (sec)": 90,

                "Priority Level": "EMERGENCY",

                "Optimization Score": 100,

                "Reason":
                    "Emergency vehicle detected. "
                    "Immediate green signal granted.",

                "Recommended Action":
                    "Override all other lanes."

            }

        # -------------------------------------
        # LOW TRAFFIC
        # -------------------------------------

        if density == "LOW":

            priority = "LOW"

            optimization = 95

            reason = (
                "Traffic flow is smooth. "
                "Maintain the current signal timing."
            )

            action = (
                "Normal operation."
            )

        # -------------------------------------
        # MEDIUM TRAFFIC
        # -------------------------------------

        elif density == "MEDIUM":

            priority = "MEDIUM"

            optimization = 80

            reason = (
                "Moderate congestion detected. "
                "Slightly increase green signal duration."
            )

            action = (
                "Monitor traffic continuously."
            )

        # -------------------------------------
        # HIGH TRAFFIC
        # -------------------------------------

        elif density == "HIGH":

            priority = "HIGH"

            optimization = 60

            reason = (
                "Heavy traffic detected. "
                "Increase green signal duration "
                "to reduce queue length."
            )

            action = (
                "Prioritize this lane."
            )

        # -------------------------------------
        # VERY HIGH TRAFFIC
        # -------------------------------------

        else:

            priority = "CRITICAL"

            optimization = 40

            reason = (
                "Severe congestion detected. "
                "Immediate optimization required."
            )

            action = (
                "Allocate maximum green time."
            )

        return {

            "Traffic Density": density,

            "Green Time (sec)": green_time,

            "Priority Level": priority,

            "Optimization Score": optimization,

            "Reason": reason,

            "Recommended Action": action

        }
            # =====================================================
    # AI DECISION SUMMARY
    # =====================================================

    def decision_summary(self, report):

        decision = self.make_decision(report)

        summary = f"""
===============================
     SYNAPSE AI DECISION
===============================

Traffic Density : {decision['Traffic Density']}

Traffic Score   : {report['Traffic Load Score']}

Priority Level  : {decision['Priority Level']}

Green Time      : {decision['Green Time (sec)']} sec

Optimization    : {decision['Optimization Score']} %

Reason
------
{decision['Reason']}

Recommended Action
------------------
{decision['Recommended Action']}

===============================
"""

        return summary