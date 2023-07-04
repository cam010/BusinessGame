from tkinter import Canvas, Frame, Scrollbar
import gamedata, attribute_classes


class SuperFrame(Frame):
    def __init__(self, gamedata: gamedata.Gamedata, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gamedata = gamedata

    # current_player_attributes
    def format_currency(self, money):
        return self.gamedata.format_curreny(money)

    def get_age_text(self):
        return "Age: {}".format(self.gamedata.age)

    def get_current_money(self):
        """NOTE returns money as non formatted integer, use self.format_currency(money) to format for text"""
        return self.gamedata.money

    def get_current_money_text(self):
        return "Money: {}".format(self.format_currency(self.get_current_money()))
    
    def get_current_total_wealth(self):
        wealth = self.get_current_money()
        for x in self.get_all_businesses():
            print(self.get_business_capital(x), x.incomings, x.outgoings)
            wealth += self.get_business_capital(x)
        for x in self.get_all_properties():
            wealth += self.get_property_current_value(x)
        return wealth
    
    def get_current_total_wealth_text(self):
        return "Total Wealth: {}".format(self.format_currency(self.get_current_total_wealth()))

    def get_job_title_text(self, job=None):
        if job is None:
            job = self.gamedata.current_job
        return "Job Title: {}".format(job.title)

    def get_job_level_text(self, job=None):
        if job is None:
            job = self.gamedata.current_job
        return "Job Level: {}".format(job.level)

    def get_job_year_joined(self):
        return self.gamedata.current_job.year_started

    def get_job_year_joined_text(self):
        return "Year Joined: {}".format(self.gamedata.current_job.year_started)

    def get_job_years_in_service_text(self):
        return "Years In Service: {}".format(self.gamedata.current_job.years_in_service)

    def get_job_salary(self, job=None):
        if job is None:
            job = self.gamedata.current_job
        return job.salary

    def get_job_salary_text(self, job=None):
        return "Salary: {}".format(self.format_currency(self.get_job_salary(job)))

    def get_job_performance_text(self):
        return "Performance: {}".format(self.gamedata.current_job.performance)

    def get_job_payrise_text(self):
        return "Last Year's Payrise: {}".format(
            self.format_currency(self.gamedata.current_job.payrise)
        )

    def get_job_bonus_text(self):
        return "Last Year's Bonus: {}".format(
            self.format_currency(self.gamedata.current_job.bonus)
        )

    def get_business_count_text(self):
        return "Businesses: {}".format(len(self.gamedata.businesses))

    def get_all_businesses_generator(self):
        for x in self.gamedata.businesses:
            yield x

    def get_all_businesses(self):
        return self.gamedata.businesses

    def get_business(self, i):
        return self.gamedata.businesses[i]

    def get_business_name(self, business: attribute_classes.Business):
        return business.name

    def get_business_name_text(self, business):
        return "Name: {}".format(self.get_business_name(business))

    def get_business_industry(self, business: attribute_classes.Business):
        return business.industry

    def get_business_industry_text(self, business):
        return "Industry: {}".format(self.get_business_industry(business))

    def get_business_years_owned(self, business: attribute_classes.Business):
        return business.years_owned

    def get_business_years_owned_text(self, business):
        return "Years Owned: {}".format(self.get_business_years_owned(business))

    def get_business_profit(self, business: attribute_classes.Business):
        return business.profit

    def get_business_profit_text(self, business):
        return "Profit: {}".format(
            self.format_currency(self.get_business_profit(business))
        )

    def get_business_capital(self, business: attribute_classes.Business):
        return business.capital

    def get_business_capital_text(self, business: attribute_classes.Business):
        return "Available capital: {}".format(self.get_business_capital(business))

    def get_business_purchase_price(self, business: attribute_classes.Business):
        return business.purchase_price

    def get_business_purchase_price_text(self, business: attribute_classes.Business):
        return "Purchase Price: {}".format(
            self.format_currency(self.get_business_purchase_price(business))
        )

    def get_all_properties(self):
       return self.gamedata.properties

    def get_property_address_text(self, property: attribute_classes.Property):
        return "Address: {}".format(property.address)
    
    def get_property_years_owned_text(self, property: attribute_classes.Property):
        return "Years owned: {}".format(self.get_property_years_owned(property))

    def get_property_years_owned(self, property: attribute_classes.Property):
        return property.years_owned

    def get_property_current_value(self, property: attribute_classes.Property):
        return property.current_value

    def get_property_current_value_text(self, property: attribute_classes.Property):
        return "Current Value: {}".format(self.format_currency(self.get_property_current_value(property)))
    
    def get_property_expenses(self, property: attribute_classes.Property):
        return property.expenses

    def get_property_expenses_text(self, property):
        return "Last Year's Expenses: {}".format(self.format_currency(self.get_property_expenses(property)))
    
    def get_property_count(self):
        return len(self.gamedata.properties)
    
    def get_property_count_text(self):
        return "Properties: {}".format(self.get_property_count())

    def get_vehicle_count_text(self):
        return "Vehicles: {}".format(len(self.gamedata.vehicles))

    # current environment attributes
    def get_current_year(self):
        return self.gamedata.year

    def get_current_year_text(self):
        return "Year: {}".format(self.get_current_year())

    # other frame methods
    def return_scrollable_frame(self, master_frame):
        canvas = Canvas(master_frame, borderwidth=0, background="#ffffff")
        inner_frame = Frame(canvas)
        scrollbar = Scrollbar(master_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        window = canvas.create_window(
            canvas.winfo_width(), 0,
            window=inner_frame,
            anchor="nw",
            tags="self.new_job_frame",
        )

        inner_frame.bind(
            "<Configure>",
            lambda event, canvas=canvas: self.scrollable_frame_configure(event, canvas),
        )
        canvas.bind(
            "<Configure>",
            lambda event, canvas_frame=window, canvas=canvas: self.on_canvas_configure(
                event, canvas_frame, canvas
            ),
        )
        return inner_frame

    def scrollable_frame_configure(self, event, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_canvas_configure(self, event, canvas_frame, canvas):
        canvas.itemconfigure(canvas_frame, width=canvas.winfo_width())


class SplitVerticalFrame(SuperFrame):
    def __init__(self, gamedata: gamedata.Gamedata, *args, **kwargs):
        super().__init__(gamedata, *args, **kwargs)

    def create_two_frames(self):
        top_frame = self._create_top_frame()
        bottom_frame = self._create_bottom_frame()
        return top_frame, bottom_frame

    def _create_top_frame(self):
        top_frame = Frame(self, highlightthickness=1, highlightbackground="black")
        top_frame.place(relheight=0.4, relwidth=1)
        return top_frame

    def _create_bottom_frame(self):
        bottom_frame = Frame(self, highlightthickness=1, highlightbackground="black")
        bottom_frame.place(relheight=0.6, relwidth=1, rely=0.4)
        return bottom_frame
