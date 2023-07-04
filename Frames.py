from tkinter import Button, Frame, Label
from SuperFrame import SuperFrame, SplitVerticalFrame
import generate_listings, attribute_classes


class VehiclesPageFrame(SuperFrame):
    """NOT IMPLEMENTED"""

    def __init__(self, gamedata, *args, **kwargs):
        super().__init__(gamedata, *args, **kwargs)
        self.label()

    def label(self):
        Label(self, text="Wohoo Cars").pack()


class HomePageFrame(SuperFrame):
    def __init__(self, gamedata: dict, *args, **kwargs):
        super().__init__(gamedata, *args, **kwargs)
        self.create_top_frame()

    def create_top_frame(self):
        self.top_frame = Frame(self)
        self.top_frame.grid(row=0, column=0)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.create_top_left_frame()

    def create_top_left_frame(self):
        self.top_left_frame = Frame(self.top_frame)
        self.top_left_frame.grid(row=0, column=0)
        for i in range(0, 5):
            self.top_left_frame.grid_rowconfigure(i, weight=1)
        Label(self.top_left_frame, text=self.get_age_text()).grid(
            row=0, column=0, sticky="w"
        )
        Label(self.top_left_frame, text=self.get_job_title_text()).grid(
            row=1, column=0, sticky="w"
        )
        Label(self.top_left_frame, text=self.get_job_salary_text()).grid(
            row=2, column=0, sticky="w"
        )
        Label(self.top_left_frame, text=self.get_business_count_text()).grid(
            row=3, column=0, sticky="w"
        )
        Label(self.top_left_frame, text=self.get_property_count_text()).grid(
            row=4, column=0, sticky="w"
        )
        Label(self.top_left_frame, text=self.get_vehicle_count_text()).grid(
            row=5, column=0, sticky="w"
        )
        Label(self.top_left_frame, text=self.get_current_money_text()).grid(
            row=6, column=0, sticky="w"
        )
        Label(self.top_left_frame, text=self.get_current_total_wealth_text()).grid(
            row=7, column=0, sticky="W"
        )
        Label(self.top_left_frame, text=self.get_current_year_text()).grid(
            row=8, column=0, sticky="w"
        )


class JobPageFrame(SplitVerticalFrame):
    def __init__(self, gamedata: dict, *args, **kwargs):
        super().__init__(gamedata, *args, **kwargs)
        self.listings = generate_listings.GenerateJobListings()
        self.create_master_frames()
        self.populate_current_job_frame()
        self.populate_new_job_frame()

    def create_master_frames(self):
        self.current_job_frame, self.new_job_frame_outer = self.create_two_frames()
        for i in range(0, 5):
            self.current_job_frame.grid_rowconfigure(i, weight=1)

        for i in range(0, 2):
            self.current_job_frame.grid_columnconfigure(i, weight=1)

    def populate_current_job_frame(self):
        self.create_current_job_info_frame()
        self.populate_current_job_info_frame()

    def create_current_job_info_frame(self):
        self.current_job_info_frame = Frame(self.current_job_frame)
        self.current_job_info_frame.grid(row=0, column=1, columnspan=2, sticky="nsew")

    def populate_current_job_info_frame(self):
        Label(
            self.current_job_info_frame,
            text=self.get_job_title_text(),
            background="grey72",
        ).grid(row=0, column=1, sticky="NSEW")
        Label(
            self.current_job_info_frame,
            text=self.get_job_level_text(),
            background="gainsboro",
        ).grid(row=1, column=1, sticky="NSEW")
        Label(
            self.current_job_info_frame,
            text=self.get_job_salary_text(),
            background="grey72",
        ).grid(row=2, column=1, sticky="NSEW")
        Label(
            self.current_job_info_frame,
            text=self.get_job_performance_text(),
            background="gainsboro",
        ).grid(row=3, column=1, sticky="NSEW")
        Label(
            self.current_job_info_frame,
            text=self.get_job_year_joined_text(),
            background="grey72",
        ).grid(row=4, column=1, sticky="NSEW")
        Label(
            self.current_job_info_frame,
            text=self.get_job_years_in_service_text(),
            background="gainsboro",
        ).grid(row=0, column=2, sticky="NSEW")
        Label(
            self.current_job_info_frame,
            text=self.get_job_payrise_text(),
            background="grey72",
        ).grid(row=1, column=2, sticky="NSEW")
        Label(
            self.current_job_info_frame,
            text=self.get_job_bonus_text(),
            background="gainsboro",
        ).grid(row=2, column=2, sticky="NSEW")

    def populate_new_job_frame(self):
        self.new_job_frame_inner = self.return_scrollable_frame(
            self.new_job_frame_outer
        )

        for _ in range(10):
            self.create_job_listing(self.new_job_frame_inner)

    def create_job_listing(self, master_frame):
        job = self.listings.generate_job()
        job_frame = Frame(master_frame)
        job_frame.pack(fill="x")
        for i in range(0, 5):
            job_frame.grid_columnconfigure(i, weight=1)
        Label(job_frame, text=self.get_job_title_text(job)).grid(
            row=0, column=1, sticky="NSW"
        )
        Label(job_frame, text=self.get_job_level_text(job)).grid(
            row=0, column=2, sticky="NSW"
        )
        Label(job_frame, text=self.get_job_salary_text(job)).grid(
            row=0, column=3, sticky="NSW"
        )
        Button(
            job_frame, text="Apply For Job", command=lambda: self.apply_for_job(job)
        ).grid(row=0, column=4, sticky="NSE")

    def apply_for_job(self, job):
        self.gamedata.start_job(job)
        self.event_generate("<<reload-frame>>")


class PropertyPageFrame(SplitVerticalFrame):
    def __init__(self, gamedata: dict, *args, **kwargs):
        super().__init__(gamedata, *args, **kwargs)
        self.create_master_frames()
        self.create_existing_properties_frame_inner()
        self.populate_existing_properties_frame_inner()

    def create_master_frames(self):
        (
            self.existing_properties_frame_outer,
            self.new_properties_frame_outer,
        ) = self.create_two_frames()

    def create_existing_properties_frame_inner(self):
        self.current_properties = self.get_all_properties()
        if len(self.current_properties) > 0:
            self.existing_properties_frame_inner = self.return_scrollable_frame(
                self.existing_properties_frame_outer
            )
        else:
            self.existing_properties_frame_inner = Frame(
                self.existing_properties_frame_outer
            )
            self.existing_properties_frame_inner.pack(anchor="center")

    def populate_existing_properties_frame_inner(self):
        if len(self.current_properties) == 0:
            Label(
                self.existing_properties_frame_inner,
                text="You Have No Properties!\nPurchase One Below Now!",
            ).pack(anchor="center")
        else:
            for x in self.current_properties:
                self.create_existing_property_info_frame(
                    self.existing_properties_frame_inner, x
                )

    def create_existing_property_info_frame(
        self, master_frame, property: attribute_classes.Property
    ):
        frame = Frame(master_frame)
        frame.pack(fill="x")
        text_info_frame = self.create_existing_property_info_text_frame(frame, property)
        text_info_frame.pack(fill="x")

    def create_existing_property_info_text_frame(
        self, master_frame, property: attribute_classes.Property
    ):
        """This function returns a frame with all the text info for a current existing property for listing in the PropertyPageFrame including:
        - Address
        - Years Owned
        - Current Price
        - Expenses last year
        """
        frame = Frame(master_frame)
        for i in range(0, 4):
            frame.grid_columnconfigure(i, weight=1)
        Label(frame, text=self.get_property_address_text(property)).grid(
            row=0, column=0, sticky="nsw"
        )
        Label(frame, text=self.get_property_years_owned_text(property)).grid(
            row=0, column=1, sticky="nsw"
        )
        Label(frame, text=self.get_property_current_value_text(property)).grid(
            row=0, column=2, sticky="nsw"
        )
        Label(frame, text=self.get_property_expenses_text(property)).grid(
            row=0, column=3, sticky="nsw"
        )
        return frame

    def create_new_properties_frame_inner(self):
        self.new_properties_frame_inner = self.return_scrollable_frame(
            self.new_properties_frame_outer
        )

    def populate_new_properties_frame_inner(self):
        for _ in range(10):
            property = generate_listings.GeneratePropertyListing().generate_property()


class BusinessPageFrame(SplitVerticalFrame):
    def __init__(self, gamedata: dict, *args, **kwargs):
        super().__init__(gamedata, *args, **kwargs)
        self.create_master_frames()
        self.create_existing_business_frame_inner()
        self.populate_existing_business_frame_inner()
        self.create_new_business_frame_inner()
        self.populate_new_business_frame_inner()

    def create_master_frames(self):
        (
            self.existing_businesses_frame_outer,
            self.new_businesses_frame_outer,
        ) = self.create_two_frames()

    def create_existing_business_frame_inner(self):
        self.current_businesses = self.get_all_businesses()
        if len(self.current_businesses) > 0:
            self.existing_business_frame_inner = self.return_scrollable_frame(
                self.existing_businesses_frame_outer
            )
        else:
            self.existing_business_frame_inner = Frame(
                self.existing_businesses_frame_outer
            )
            self.existing_business_frame_inner.pack(anchor="center")

    def populate_existing_business_frame_inner(self):
        if len(self.current_businesses) == 0:
            Label(
                self.existing_business_frame_inner,
                text="You Have No Businesses!\nPurchase One Below Now!",
            ).pack(anchor="center")
        else:
            for x in self.current_businesses:
                self.create_existing_business_info_frame(
                    self.existing_business_frame_inner, x
                )

    def create_existing_business_info_frame(
        self, master_frame, business: attribute_classes.Business
    ):
        frame = Frame(master_frame)
        frame.pack(fill="x")
        text_info_frame = self.create_existing_business_info_text_frame(frame, business)
        text_info_frame.pack(fill="x")

    def create_existing_business_info_text_frame(
        self, master_frame, business: attribute_classes.Business
    ):
        """This function returns a frame with all the text info for a current existing business for listing in the BusinessPageFrame including:
        - Name
        - Industry
        - Years Owned
        - Profit
        """
        frame = Frame(master_frame)
        for i in range(0, 4):
            frame.grid_columnconfigure(i, weight=1)
        Label(frame, text=self.get_business_name_text(business)).grid(
            row=0, column=0, sticky="nsw"
        )
        Label(frame, text=self.get_business_industry_text(business)).grid(
            row=0, column=1, sticky="nsw"
        )
        Label(frame, text=self.get_business_years_owned_text(business)).grid(
            row=0, column=2, sticky="nsw"
        )
        Label(frame, text=self.get_business_profit_text(business)).grid(
            row=0, column=3, sticky="nsw"
        )
        return frame

    def create_new_business_frame_inner(self):
        self.new_businesses_frame_inner = self.return_scrollable_frame(
            self.new_businesses_frame_outer
        )

    def populate_new_business_frame_inner(self):
        for _ in range(10):
            business = generate_listings.GenerateBusinessListing().generate_business()
            self.create_new_business_info_frame(
                self.new_businesses_frame_inner, business
            )

    def create_new_business_info_frame(
        self, master_frame, business: attribute_classes.Business
    ):
        frame = Frame(master_frame)
        frame.pack(fill="x")
        # for i in range(0, 2):
        frame.grid_columnconfigure(0, weight=5)
        frame.grid_columnconfigure(1, weight=1)
        # TODO icon info frame
        text_info_frame = self.create_new_business_info_text_frame(frame, business)
        text_info_frame.grid(row=0, column=0, sticky="nsew")
        purchase_business_button = Button(
            frame,
            text="Purchase Business",
            command=lambda: self.purchase_business(business),
        )
        purchase_business_button.grid(row=0, column=1, sticky="nse")

    def purchase_business(self, business: attribute_classes.Business):
        if self.gamedata.add_business(business):
            self.event_generate("<<reload-frame>>")

    def create_new_business_info_text_frame(
        self, master_frame, business: attribute_classes.Business
    ):
        frame = Frame(master_frame)
        for i in range(0, 3):
            frame.grid_columnconfigure(i, weight=1)
        Label(frame, text=self.get_business_name_text(business)).grid(
            row=0, column=0, sticky="ns"
        )
        Label(frame, text=self.get_business_industry_text(business)).grid(
            row=0, column=1, sticky="ns"
        )
        Label(frame, text=self.get_business_purchase_price_text(business)).grid(
            row=0, column=2, sticky="ns"
        )
        return frame


class SettingsPageFrame(SuperFrame):
    """NOT IMPLEMENTED"""

    def __init__(self, gamedata: dict, *args, **kwargs):
        super().__init__(gamedata, *args, **kwargs)
        self.label()

    def label(self):
        Label(self, text="Wohoo Settings").pack()
