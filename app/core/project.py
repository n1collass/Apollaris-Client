from app.core.decision_engine import selection
from demand import demand
from app.core.instalation import instalation_parameters
from app.core.instalation import solar_parameters

class Project():
    def __init__():
        pass
    
    def make_selection(self):
        params = instalation_parameters(
            lat=23,
            lon=22,
            alt=21
        )
                
        selection(params)
        