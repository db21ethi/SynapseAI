# =====================================================
# SYNAPSE AI
# Multi Junction Signal Optimizer
# =====================================================

import pandas as pd


class JunctionController:

    def __init__(self):

        print("✓ Junction Controller Ready")

        # Weight of each vehicle type
        self.weights = {

            "Cars": 1,

            "Motorcycles": 0.6,

            "Bicycles": 0.4,

            "Buses": 3,

            "Trucks": 4

        }
            # =====================================================
    # CALCULATE LANE SCORE
    # =====================================================

    def calculate_score(self, report):

        score = 0

        score += report["Cars"] * self.weights["Cars"]
        score += report["Motorcycles"] * self.weights["Motorcycles"]
        score += report["Bicycles"] * self.weights["Bicycles"]
        score += report["Buses"] * self.weights["Buses"]
        score += report["Trucks"] * self.weights["Trucks"]

        # Bonus for already-computed traffic load
        score += report["Traffic Load Score"]

        # Heavy traffic bonus
        if report["Traffic Density"] == "HIGH":
            score += 10

        elif report["Traffic Density"] == "VERY HIGH":
            score += 20

        # Future support for emergency vehicles
        if report.get("Emergency Vehicle", False):
            score += 100

        return round(score, 2)
            # =====================================================
    # OPTIMIZE SIGNALS
    # =====================================================

    def optimize(self, reports):

        ranking = []

        for index, report in enumerate(reports):

            score = self.calculate_score(report)

            ranking.append({

                "Lane": f"Road {index + 1}",

                "Vehicles": report["Total Vehicles"],

                "Score": score,

                "Traffic Density": report["Traffic Density"],

                "Green Time": report["Recommended Green Time"]

            })

        # Highest score gets highest priority
        ranking.sort(
            key=lambda lane: lane["Score"],
            reverse=True
        )

        # Assign priorities
        for i, lane in enumerate(ranking):

            lane["Priority"] = i + 1

        return ranking
            # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    def display_ranking(self, ranking):

        print("\n" + "=" * 60)
        print("      SYNAPSE AI - JUNCTION OPTIMIZATION")
        print("=" * 60)

        for lane in ranking:

            print(
                f"Priority {lane['Priority']} | "
                f"{lane['Lane']} | "
                f"Vehicles: {lane['Vehicles']} | "
                f"Score: {lane['Score']} | "
                f"Density: {lane['Traffic Density']} | "
                f"Green Time: {lane['Green Time']} sec"
            )

        print("=" * 60)


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    controller = JunctionController()

    sample_reports = [

        {
            "Cars": 20,
            "Buses": 2,
            "Trucks": 1,
            "Motorcycles": 8,
            "Bicycles": 3,
            "Traffic Load Score": 46,
            "Traffic Density": "HIGH",
            "Recommended Green Time": 45,
            "Total Vehicles": 34,
            "Emergency Vehicle": False
        },

        {
            "Cars": 10,
            "Buses": 1,
            "Trucks": 0,
            "Motorcycles": 5,
            "Bicycles": 2,
            "Traffic Load Score": 22,
            "Traffic Density": "LOW",
            "Recommended Green Time": 20,
            "Total Vehicles": 18,
            "Emergency Vehicle": False
        },

        {
            "Cars": 25,
            "Buses": 3,
            "Trucks": 2,
            "Motorcycles": 10,
            "Bicycles": 4,
            "Traffic Load Score": 70,
            "Traffic Density": "VERY HIGH",
            "Recommended Green Time": 60,
            "Total Vehicles": 44,
            "Emergency Vehicle": False
        },

        {
            "Cars": 15,
            "Buses": 1,
            "Trucks": 1,
            "Motorcycles": 6,
            "Bicycles": 1,
            "Traffic Load Score": 35,
            "Traffic Density": "MEDIUM",
            "Recommended Green Time": 30,
            "Total Vehicles": 24,
            "Emergency Vehicle": False
        }

    ]

    ranking = controller.optimize(sample_reports)

    controller.display_ranking(ranking)