import threading
from .settings import *
from .handler import *
from .fetcher import *

class AddRowThread(threading.Thread):
    def __init__(self, dataset, thread, rows, parameters):
        threading.Thread.__init__(self)
        self.dataset = dataset
        self.thread = thread
        self.rows = rows
        self.parameters = parameters

    def fetch_row(self):
        for data in self.dataset:
            object = {}
            if self.parameters == "1":
                object.update({'execution_parameters': EXECUTION_PARAMETERS_1})
            elif self.parameters == "2":
                object.update({'execution_parameters': EXECUTION_PARAMETERS_2})
            elif self.parameters == "3":
                object.update({'execution_parameters': EXECUTION_PARAMETERS_3})
            object.update({'data': [data]})
            row = ["thread-" + str(self.thread), len(self.rows) + 1]
            row.extend([fetch_data(object) for _ in range(5)])
            self.rows.append(row)

    def run(self):
        self.fetch_row()

def run(archive, threads, parameters):
    rows = []
    active_threads = []

    for i in range(int(threads)):
        thread = i + 1
        dataset = read_file(archive)
        t = AddRowThread(dataset, thread, rows, parameters)
        t.start()
        active_threads.append(t)

    for t in active_threads:
        t.join()

    write_file(threads, archive, rows, parameters)
