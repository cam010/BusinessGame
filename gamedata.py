import attribute_classes
from locale import currency, setlocale, LC_ALL
from event_popup import Popup

setlocale(LC_ALL, "en_GB") # set local to GB. Used to format currency

class Gamedata:
    def __init__(self):
        self.current_environment_attributes()
        self.current_player_attributes()
        self.vehicles = []
        
        # preset some values
        starter_job = attribute_classes.Job("Parents' allowance", "unemployed", 60, 80)
        self.start_job(starter_job)
        
        sample_business = attribute_classes.Business("Sample Name", "Sample Industry", 100_000)
        sample_business.purchase_price = 0
        self.add_business(sample_business)
        
        sample_property = attribute_classes.Property("address", "flat", 5, 5)
        self.add_property(sample_property)
    
    def format_curreny(self, money):
        return currency(money, grouping=True)
    
    def current_environment_attributes(self):
        self.year = 2023
    
    def advance_time(self):
        self.year += 1
        self.age += 1
        self.advance_time_job()
        self.advance_time_business()
        self.advance_time_property()
    
    def advance_time_job(self):
        self.current_job.finish_year()
        self.money += self.current_job.get_yearly_income()
        self.money = self.money
        self.current_job.start_next_year()
    
    def advance_time_property(self):
        for x in self.properties:
            x.advance_time()
    
    def advance_time_business(self):
        for x in self.businesses:
            x.advance_time()
    
    def current_player_attributes(self):
        self.money = 0
        self.age = 18
        self.businesses = []
        self.properties = []
    
    def start_job(self, job: attribute_classes.Job):
        self.current_job = job
        self.current_job.start_job(self.year)
    
    def add_business(self, business: attribute_classes.Business):
        if self.check_sufficient_funds_to_purchase(business.purchase_price, self.money):
            self.businesses.append(business)
            business.start_ownership(self.year)
            self.money -= business.purchase_price
            return True
        else:
            Popup("Insufficient Funds to Buy Business")
        return False

    def add_property(self, property: attribute_classes.Property):
        if self.check_sufficient_funds_to_purchase(property.initial_purchase_price, self.money):
            self.properties.append(property)
            # property.start_ownership(self.year)
            self.money -= property.initial_purchase_price
            return True
        else:
            Popup("Insufficient Funds to Buy Business")
        return False
    
    def check_sufficient_funds_to_purchase(self, purchase_price, money):
        return True if money >= purchase_price else False
        