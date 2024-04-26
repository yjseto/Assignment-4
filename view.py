# view.py

from tkinter import *
from controller import Controller

class View:
    def __init__(self, master):
        self.master = master
        self.controller = Controller(self)

        self.scheduler_options = [
            "Round Robin",
            "Shortest Processing Next",
            "Shortest Remaining Time",
            "Highest Response Ratio Next"
        ]

        self.process_name_entry = StringVar(master)
        self.process_name_entry.set(self.scheduler_options[0])

        self.create_widgets()

    def create_widgets(self):
        # Drop down menu for scheduler options
        w = OptionMenu(self.master, self.process_name_entry, *self.scheduler_options)
        w.grid()

        # Create labels
        Label(self.master, text="Process Name:").grid(row=1, column=0)
        Label(self.master, text="Arrival Time:").grid(row=1, column=1)
        Label(self.master, text="Processing Time:").grid(row=1, column=2)

        labels = ["A", "B", "C", "D"]
        for i, label in enumerate(labels, start=2):
            Label(self.master, text=label + ":").grid(row=i, column=0)
            Entry(self.master).grid(row=i, column=1)
            Entry(self.master).grid(row=i, column=2)

        # Create a text widget for displaying results
        Label(self.master, text="Results:").grid(row=6, column=0)
        self.results_text_widget = Text(self.master, height=5, width=35)
        self.results_text_widget.grid(row=6, column=1, columnspan=2)

        # Create a submit button
        Button(self.master, text="Submit", command=self.submit_data).grid()

    def get_data(self):
        process_name = self.process_name_entry.get()
        data = {}
        for label in ["A", "B", "C", "D"]:
            arrival_time = int(self.master.grid_slaves(row=label).cget("textvariable").get())
            processing_time = int(self.master.grid_slaves(row=label, column=2)[0].cget("textvariable").get())
            data[label] = {"process_name": label, "arrival_time": arrival_time, "processing_time": processing_time}
        return process_name, data

    def submit_data(self):
        process_name, data = self.get_data()
        self.controller.submit_data(process_name, **data)
