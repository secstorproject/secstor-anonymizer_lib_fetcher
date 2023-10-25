import json
import os.path
import csv
from .settings import RESULTS_PATH

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf8') as reader:
            data = reader.read()
    else:
        raise FileNotFoundError(f"{filename} was not found!")

    return json.loads(data)

def write_file(thread_count, archive, rows, parameters):
    file_base = os.path.basename(archive).split(".")[0]
    thread_label = f"{thread_count}_threads" if int(thread_count) > 1 else f"{thread_count}_thread"
    filename = f"anonimized_data_{thread_label}_{file_base}_parameters_{parameters}.csv"
    path = os.path.join(RESULTS_PATH, f"{filename}")
    header = ["thread", "registro", "tempo1", "tempo2", "tempo3", "tempo4", "tempo5"]

    with open(path, 'w', newline='', encoding='utf8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerows(rows)
