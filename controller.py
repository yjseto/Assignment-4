# controller.py

from scheduler_algo import SPN

class Controller:
    def __init__(self, view):
        self.view = view

    def submit_data(self, process_name, **kwargs):
        if process_name == "Shortest Processing Next":
            SPN(**kwargs)
        else:
            print("Invalid option selected")
