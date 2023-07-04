from random import randint, uniform, normalvariate
from event_popup import Popup

class Business:
    def __init__(self, name, industry, starting_capital):
        self.years_owned = 0
        self.name = name
        self.industry = industry
        self.capital = starting_capital
        self.generate_starting_finances()
        self.calculate_purchase_price()
        
    def start_ownership(self, current_year):
        self.year_started = current_year

    def advance_time(self):
        self.years_owned += 1
        self.regenerate_finances()
        self.calculate_purchase_price()

    def generate_finances(self):
        self.generate_outgoings()
        self.calculate_profit()
        self.add_capital(self.profit)

    def generate_starting_finances(self):
        min_incomings, max_incomings = self.capital * 0.5, self.capital * 1.5
        self.incomings = round(uniform(min_incomings, max_incomings), 2)
        self.generate_finances()

    def regenerate_finances(self):
        self.regenerate_incomings()
        self.generate_finances()

    def generate_outgoings(self):
        # min_outgoings, max_outgoings = 80, 120 # percentage
        multiplier = normalvariate(1, 0.2)
        print(multiplier, "attribute_classes ln 38")
        self.outgoings = self.incomings * multiplier

    def regenerate_incomings(self):
        min_multiplier, max_multiplier = 80, 120 # percentage
        multiplier = randint(min_multiplier, max_multiplier) / 100
        print(multiplier, "attribute_classes ln 44")
        self.incomings *= multiplier

    def calculate_profit(self):
        self.profit = self.incomings - self.outgoings

    def add_capital(self, value_toadd):
        self.capital += value_toadd
        if self.capital <= 0:
            Popup("Business Bankrupt")
            self.capital = 100_000
    
    def calculate_purchase_price(self):
        self.purchase_price = (self.capital * self.incomings) / self.outgoings


class Job:
    def __init__(self, title, level, salary, max_salary):
        self.title = title
        self.level = level
        self.salary = salary
        self.years_in_service = 0
        self.max_salary = max_salary
        self.performance = "n/a"
        self.payrise = 0
        self.bonus = 0
        
        self.popup_log = {
            "Max Salary Reached": False
        }
    
    def start_job(self, current_year):
        self.year_started = current_year

    def start_next_year(self):
        self.generate_payrise()

    def finish_year(self):
        self.years_in_service += 1
        self.calculate_yearly_performance()

    def calculate_yearly_performance(self):
        self.performance = randint(1, 10)

    def get_yearly_income(self):
        min_bonus, max_bonus = self.salary * 0.01, self.salary * 0.04
        if randint(1, 10) + 2 <= self.performance:
            self.bonus = round(uniform(min_bonus, max_bonus), 2)
        else:
            self.bonus = 0

        self.bonus = round(self.bonus, 2)

        return self.salary + self.bonus

    def generate_payrise(self):
        payrise = self.salary * 0.005  # default is 0.5%
        if randint(1, 10) <= self.performance:
            self.payrise = payrise * self.performance
            self.payrise = round(self.payrise, 2)
        else:
            self.payrise = 0

        self.salary += self.payrise
        if self.salary >= self.max_salary:
            self.salary = self.max_salary
            self.payrise = 0
            if not self.popup_log["Max Salary Reached"]:
                self.popup_log["Max Salary Reached"] = True
                Popup("Max Salary For Current Job Reached!\nYou Will Recieve No More Payrises For This Job!")
        self.salary = round(self.salary, 2)

class Property:
    def __init__(self, address, type, bedrooms, bathrooms) -> None:
        self.address = address
        self.type = type
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        
        self.expenses = 20000
        self.years_owned = 0
        self.current_value = 200000
        self.initial_purchase_price = 0

    def start_ownership(self, current_yeaer):
        self.year_purchased = current_yeaer
    
    def advance_time(self):
        self.years_owned += 1
        self.regenerate_expenses()
        self.regenerate_value()
    
    def regenerate_expenses(self):
        min_multiplier, max_multiplier = 90, 110 # This is a percentage number
        multiplier = randint(min_multiplier, max_multiplier)
        self.expenses = self.expenses * (multiplier / 100)
    
    def regenerate_value(self):
        min_multiplier, max_multiplier = 90, 110 # This is a percentage number
        multiplier = randint(min_multiplier, max_multiplier)
        self.current_value = self.current_value * (multiplier / 100)