import math as math

class demand():
    def __init__(self, instalation):
        self.instalation = instalation
        pass
    
    
    # Annual demand average in kWh
    def annual_avg():
        return 300
    
    # Estimated required power for the PV system
    def estimated_power_required(self):
        inverter_ef = 90/100
        capacity_factor = 80/100
        istc = 1
    
        return self.annual_avg * istc / (inverter_ef * (30 * solar_conditions.annual_diary_avg_irradiance()) * capacity_factor)