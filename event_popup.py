from tkinter import messagebox, Tk

class Popup:
    def __init__(self, message, title="Notification!"):
        self.title = title
        self.message = message
        self.root = Tk()
        self.root.withdraw()
        
        self.create_popup()
        
        self.root.mainloop()
    
    def create_popup(self):
        messagebox.showinfo(title=self.title, message=self.message)