# =====================================================
# SYNAPSE AI
# Traffic Analytics Engine
# =====================================================

class TrafficAnalytics:

    def __init__(self):

        print("✓ Traffic Analytics Ready")

        # Estimated fuel consumption while waiting
        self.fuel_per_second = 0.00035

        # Average CO₂ emission per litre of fuel
        self.co2_per_litre = 2.31

        # Maximum waiting time used for efficiency calculation
        self.max_wait_time = 60
            # =====================================================
    # FUEL SAVINGS
    # =====================================================

    def estimate_fuel_saved(self, green_time):

        fuel = green_time * self.fuel_per_second

        return round(fuel, 3)


    # =====================================================
    # CO₂ REDUCTION
    # =====================================================

    def estimate_co2_reduction(self, fuel_saved):

        co2 = fuel_saved * self.co2_per_litre

        return round(co2, 3)


    # =====================================================
    # WAITING TIME
    # =====================================================

    def estimate_waiting_time(self, report):

        density = report["Traffic Density"]

        if density == "LOW":
            return 10

        elif density == "MEDIUM":
            return 20

        elif density == "HIGH":
            return 35

        return 50


    # =====================================================
    # TRAFFIC EFFICIENCY
    # =====================================================

    def calculate_efficiency(self, waiting_time):

        efficiency = 100 - (
            waiting_time / self.max_wait_time
        ) * 100

        efficiency = max(0, min(100, efficiency))

        return round(efficiency, 1)


    # =====================================================
    # CONGESTION INDEX
    # =====================================================

    def congestion_index(self, score):

        index = min(score, 100)

        return round(index, 1)


    # =====================================================
    # SUSTAINABILITY SCORE
    # =====================================================

    def sustainability_score(self, efficiency, co2_saved):

        score = efficiency + (co2_saved * 5)

        score = min(score, 100)

        return round(score, 1)
            # =====================================================
    # GENERATE ANALYTICS REPORT
    # =====================================================

    def generate(self, report):

        # -----------------------------------
        # Base Values
        # -----------------------------------

        green_time = report["Recommended Green Time"]

        traffic_score = report["Traffic Load Score"]

        total_vehicles = report["Total Vehicles"]

        waiting_time = self.estimate_waiting_time(report)

        # -----------------------------------
        # Fuel & CO₂
        # -----------------------------------

        fuel_saved = self.estimate_fuel_saved(green_time)

        co2_saved = self.estimate_co2_reduction(fuel_saved)

        # -----------------------------------
        # Efficiency
        # -----------------------------------

        efficiency = self.calculate_efficiency(waiting_time)

        congestion = self.congestion_index(traffic_score)

        sustainability = self.sustainability_score(
            efficiency,
            co2_saved
        )

        # -----------------------------------
        # AI Performance Rating
        # -----------------------------------

        if efficiency >= 90:
            rating = "Excellent"

        elif efficiency >= 75:
            rating = "Good"

        elif efficiency >= 60:
            rating = "Average"

        else:
            rating = "Poor"

        # -----------------------------------
        # Smart City Index
        # -----------------------------------

        smart_city_index = round(

            (efficiency + sustainability) / 2,

            1

        )

        # -----------------------------------
        # Average Delay Per Vehicle
        # -----------------------------------

        if total_vehicles == 0:

            delay_per_vehicle = 0

        else:

            delay_per_vehicle = round(

                waiting_time / total_vehicles,

                2

            )

        # -----------------------------------
        # Final Analytics Report
        # -----------------------------------

        analytics = {

            "Estimated Fuel Saved (L)": fuel_saved,

            "Estimated CO₂ Reduction (kg)": co2_saved,

            "Estimated Waiting Time (sec)": waiting_time,

            "Traffic Efficiency (%)": efficiency,

            "Congestion Index": congestion,

            "Average Delay Per Vehicle (sec)": delay_per_vehicle,

            "Sustainability Score": sustainability,

            "Smart City Index": smart_city_index,

            "AI Performance Rating": rating

        }

        return analytics
        # =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    analytics = TrafficAnalytics()

    sample_report = {

        "Cars": 24,

        "Buses": 3,

        "Trucks": 2,

        "Motorcycles": 12,

        "Bicycles": 4,

        "Persons": 15,

        "Total Vehicles": 45,

        "Traffic Load Score": 78,

        "Traffic Density": "HIGH",

        "Recommended Green Time": 45

    }

    report = analytics.generate(sample_report)

    print("\n" + "=" * 60)
    print("          SYNAPSE AI ANALYTICS REPORT")
    print("=" * 60)

    for key, value in report.items():
        print(f"{key:<35}: {value}")

    print("=" * 60)
    print("✓ Analytics Engine Working Successfully")