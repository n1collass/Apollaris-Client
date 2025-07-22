
class instalation_parameters():
    lat = None      # Latitude
    lon = None      # Longitude
    alt = 10        # Altitude
    hum = 90        # Humidity
    
    # Area of the instalation
    area = None
    
    # For advanced calculus like the distance between the array of modules
    # we need the lengh and width of the area of instalation
    leng = None
    widt = None
    
    def __init__(self, lat, lon, alt, area, leng, widt):
        # This is fed by the controller, don't worry
        self.lat = lat
        self.lon = lon
        self.alt = alt
        
        self.area = area
        self.leng = leng
        self.widt - widt

        self.calculate_area()
        pass
    
    def calculate_area(self):
        # Only calculate the area if the user is specifing a leng and a widt
        if(self.leng != None & self.widt != None):
            self.area = self.leng * self.widt

class ambient_parameters():
    # General ambient parameters
    hum = None
    
    # Temperature parameters
    # Collection Montly
    avg_montly_temp = list()
    max_montly_temp = list()
    min_montly_temp = list()
    
    # Collection Annual
    avg_annual_temp = None
    max_annual_temp = None
    min_annual_temp = None
    
    def __init__(self, params):
        self.params = params
        pass
        
class solar_parameters():
    def __init__(self, params):
        self.params = params
        pass
    
    def optimum_inclination(self):
        # A new formula to calculate the optimum inclination is going to be included in the future
        return self.params.lat
    
    def azimuth(self):
        # Considering for now that the pv modules are facing north
        return 0

    def minimum_solar_elevation_angle(self):
        return 90 - abs(self.params.lat + 23,45)
    
    def annual_diary_avg_irradiance():
        return 1000