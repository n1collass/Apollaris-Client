# Arquivo para calcular e inserir os parametros da instalação

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
    
    def __init__(self, lat, lon):
        self.calculate_area()
        pass
    
    def demand(self):
        pass
    
    # For avoiding errors, we need to perform validations of the data
    def validate_data(self):
        if(self.lat == None or self.lon == None):
            return 0
        
        # Validate area and dimensions of the instalation area
        if((self.leng == None or self.widt == None) and self.area == None):
            return 0
    
    def calculate_area(self):
        if(self.leng != None & self.widt != None):
            self.area = self.leng * self.widt
        
class solar_parameters():
    def __init__(self, instalation):
        self.instalation = instalation
        pass
    
    def optimum_inclination(self):
        # A new formula to calculate the optimum inclination is going to be included in the future
        return self.instalation.lat
    
    def azimuth(self):
        # Considering for now that the pv modules are facing north
        return 0
    
    def minimum_solar_elevation_angle(self):
        return 90 - abs(self.instalation.lat + 23,45)
    
    def annual_diary_avg_irradiance():
        return 1000