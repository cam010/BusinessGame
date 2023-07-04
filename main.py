from tkinter import Tk, Frame, Button, Label, Event
import Frames, gamedata, SuperFrame
import json

HOMEPAGE = Frames.HomePageFrame
VEHICLEPAGE = Frames.VehiclesPageFrame
PROPERTYPAGE = Frames.PropertyPageFrame
BUSINESSPAGE = Frames.BusinessPageFrame
SETTINGSPAGE = Frames.SettingsPageFrame
JOBPAGE = Frames.JobPageFrame


class Main:
    def __init__(self) -> None:
        self.gamedata = gamedata.Gamedata()

        self.root = Tk()
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        self.root.title("Financial Sim")
        self.setup_window()

        self.current_frame = None
        self.load_frame(HOMEPAGE)
        
        self.root.bind("<<reload-frame>>", self.frame_reload_event)

        self.root.mainloop()
    
    def frame_reload_event(self, event: Event):
        if isinstance(event.widget, SuperFrame.SuperFrame):
            self.frame_reload()
        
    def frame_reload(self):
            current_frame = type(self.current_frame)
            self.load_frame(current_frame, override_anti_reload=True)

    def setup_window(self):
        self.contentframe = Frame(
            self.root, highlightbackground="black", highlightthickness=1
        )
        self.contentframe.place(relwidth=1, relheight=0.6)

        self.frame_nav_button_frame = Frame(
            self.root, highlightbackground="black", highlightthickness=1
        )
        self.frame_nav_button_frame.place(relwidth=1, relheight=0.4, rely=0.6)
        self.setup_frame_nav_buttons()

    def setup_frame_nav_buttons(self):
        y_padding = self.contentframe.winfo_height() / 10  # rel height 0.1
        x_padding = self.contentframe.winfo_width() / 10  # rel width 0.1
        BTN_HEIGHT = 0.2
        BTN_WIDTH = 0.35

        btnrow1_y = y_padding
        btnrow2_y = y_padding + BTN_HEIGHT + y_padding
        btnrow3_y = y_padding + BTN_HEIGHT + y_padding + BTN_HEIGHT + y_padding

        btncol1_x = x_padding
        btncol2_x = x_padding + BTN_WIDTH + x_padding

        self.home_button = Button(
            self.frame_nav_button_frame,
            text="Homepage",
            command=lambda: self.load_frame(HOMEPAGE),
        )
        self.home_button.place(
            relheight=BTN_HEIGHT, rely=btnrow1_y, relwidth=BTN_WIDTH, relx=btncol1_x
        )
        self.vehicle_page_button = Button(
            self.frame_nav_button_frame,
            text="Vehicle Page",
            command=lambda: self.load_frame(VEHICLEPAGE),
        )
        self.vehicle_page_button.place(
            relheight=BTN_HEIGHT, rely=btnrow1_y, relwidth=BTN_WIDTH, relx=btncol2_x
        )
        self.property_page_button = Button(
            self.frame_nav_button_frame,
            text="Property Page",
            command=lambda: self.load_frame(PROPERTYPAGE),
        )
        self.property_page_button.place(
            relheight=BTN_HEIGHT, rely=btnrow2_y, relwidth=BTN_WIDTH, relx=btncol1_x
        )
        self.business_page_button = Button(
            self.frame_nav_button_frame,
            text="Business Page",
            command=lambda: self.load_frame(BUSINESSPAGE),
        )
        self.business_page_button.place(
            relheight=BTN_HEIGHT, rely=btnrow2_y, relwidth=BTN_WIDTH, relx=btncol2_x
        )
        self.jobs_page_button = Button(
            self.frame_nav_button_frame,
            text="Job Page",
            command=lambda: self.load_frame(JOBPAGE),
        )
        self.jobs_page_button.place(
            relheight=BTN_HEIGHT, rely=btnrow3_y, relwidth=BTN_WIDTH, relx=btncol1_x
        )
        self.year_up_button = Button(
            self.frame_nav_button_frame,
            text="Advance Time",
            command=lambda: self.advance_time(),
        )
        self.year_up_button.place(
            relheight=BTN_HEIGHT, rely=btnrow3_y, relwidth=BTN_WIDTH, relx=btncol2_x
        )

    def load_frame(self, frame: Frame, override_anti_reload=False):
        if isinstance(self.current_frame, frame) and not override_anti_reload:
            return
        if self.current_frame is not None:
            self.destroy_frame()

        self.current_frame = frame(
            self.gamedata,
            master=self.contentframe,
            highlightbackground="black",
            highlightthickness=1,
        )
        # self.current_frame.grid(row=0, column=0)
        self.current_frame.pack(expand=True, fill="both")

    def destroy_frame(self):
        self.current_frame.forget()
        self.current_frame.destroy()
        self.current_frame = None

    def advance_time(self):
        self.gamedata.advance_time()
        self.frame_reload()


if __name__ == "__main__":
    Main()
