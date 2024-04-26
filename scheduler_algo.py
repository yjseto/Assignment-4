# scheduler_algo.py

def SPN(**kwargs):
    # Assuming kwargs contain data for processes A, B, C, D
    processes = sorted(kwargs.values(), key=lambda x: x["processing_time"])

    # Prepare a string to store the results
    result_text = "SPN Results:\n"

    # Execute processes in order
    for process in processes:
        result_text += "Executing process: {}\n".format(process["process_name"])
        while process["processing_time"] > 0:
            process["processing_time"] -= 1  # Simulate execution by decrementing processing time
            result_text += "Remaining processing time for {}: {}\n".format(process["process_name"], process["processing_time"])
            result_text += "\n"

    # Display results in the text widget
    view = self.controller.view
    view.results_text_widget.config(state=NORMAL)
    view.results_text_widget.delete("1.0", END)  # Clear previous results
    view.results_text_widget.insert(END, result_text)
    view.results_text_widget.config(state=DISABLED)
