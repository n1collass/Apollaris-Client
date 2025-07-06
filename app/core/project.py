from selection import selection
from demand import demand
from instalation_parameters import instalation_parameters
from instalation_parameters import solar_parameters

class Project():
    def __init__():
        pass
    
    def make_selection(self):
        instalation = instalation_parameters
        
        solar_conditions = solar_parameters(instalation)
        
        project_demand = demand(instalation, solar_conditions)
        
        selection(instalation, solar_conditions, project_demand)
        