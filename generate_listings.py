import json
from random import choice, randint, gammavariate
import attribute_classes

with open("jobs.json", "r") as f:
    JOBSLIST = json.load(f)["jobs"]
with open("businesses.json", "r") as f:
    BUSINESSLIST = json.load(f)["industries"]
with open("properties.json", "r") as f:
    data = json.load(f)
    ADDRESSLIST = data["addresses"]
    PROPERTYTYPES = data["property_types"]


class GenerateJobListings:
    def __init__(self):
        self.jobslist = JOBSLIST

    def generate_job(self, level=None):
        # job format:
        # {title str, level str, salary int, max_salary int}
        # TODO generate jobs by level
        job = choice(self.jobslist)
        # dict(job) necessary to stop altering of jobslist due to variable pointing!
        job = dict(job)  
        salary_skewer = randint(80, 120) / 100
        job["salary"] = round(job["salary"] * salary_skewer, 2)
        
        max_salary_skewer = randint(80, 120) / 100
        job["max_salary"] = round(job["max_salary"] * max_salary_skewer, 2)
        
        return attribute_classes.Job(*job.values())

class GenerateBusinessListing:
    def __init__(self):
        # BUSINESSLIST FORMAT:
        # [
        #   {
        #       "industry": str,
        #       "business_names": list
        # }, (continues with these dicts in a list)
        # ]
        self.businesslist = BUSINESSLIST
    
    def generate_business(self):
        _choice = choice(self.businesslist)
        name = choice(_choice["business_names"])
        industry = _choice["industry"]
        capital = self.generate_starting_capital()
        business = attribute_classes.Business(name, industry, capital)
        return business
    
    def generate_starting_capital(self):
        return randint(10_000, 1_000_000)
        
class GeneratePropertyListing:
    def __init__(self):
        self.address_list = ADDRESSLIST
        self.property_types = PROPERTYTYPES
    
    def generate_property(self):
        address = choice(self.address_list)
        _choice = choice(self.property_types)
        property_type = _choice[0]
        property_price = self.generate_property_price(_choice[1])
        expenses = self.generate_expenses(property_price)
        bedrooms, bathrooms = gammavariate(1, 10), gammavariate(1, 10) # see sources folder
        
        property = attribute_classes.Property(address, property_type, bedrooms, bathrooms, expenses)
        return property
    
    def generate_property_price(self, initial_price):
        min_multiplier, max_multiplier = 80, 120 # percentage_price
        multiplier = randint(min_multiplier, max_multiplier) / 100
        return initial_price * multiplier
    
    def generate_expenses(self, property_price):
        min_expenses, max_expenses = 5, 15 # percenatge of property price
        expenses_percentage = randint(min_expenses, max_expenses) / 100
        return property_price * expenses_percentage
