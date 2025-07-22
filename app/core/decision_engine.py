from instalation import ambient_parameters
from instalation import solar_parameters

from app.models.module import Module

import math

# The core of the selection criterion, the decision engine
class decision_engine():
    def __init__(self, params):
        self.params = params
        self.ambient_params = ambient_parameters(params)
        self.solar_params = solar_parameters(params, self.ambient_params)
        pass
    
    # Calculate the estimated required power for the PV system
    def estimated_power_required(self):
        inverter_ef = 90/100
        capacity_factor = 80/100
        istc = 1
    
        return self.annual_avg * istc / (inverter_ef * (30 * self.solar_params.annual_diary_avg_irradiance()) * capacity_factor)
    
    # Filter only the modules that satisfies the needs of area and temperature
    def viable_modules_roof(self):
        # First, we need to calculate the production necessary per meter
        required_wpm = self.estimated_power_required / self.params.area
        
        modules_viable = []

        # Next, only choose modules that require the watts per metter and temperature factors   
        for module in Module.query.all():
            if module.wpm >= required_wpm and module.max_temp > self.ambient_params.max_annual_temp and module.min_temp < self.ambient_params.min_annual_temp: 
                modules_viable.append(module)

        if modules_viable is None:
            # Throw an error
            return 'None'
    
        return modules_viable

    # That method is under development, don't use it
    def viable_modules_floor(self, area):
        # First, each module will have a distance between it because of the inclination angle
        # For optimization, I will use an average value of lenght for the modules
        avg_leng = 2
        
        distance = (avg_leng * math.sin(self.solar_conditions.optimum_inclination) * math.cos(self.solar_conditions.azimuth)) / math.tan(self.solar_conditions.minimum_solar_elevation_angle)