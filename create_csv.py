import pandas as pd
import os
import csv

dir = ''


def create_for(dataset):
    files = list()
    path = os.path.join(dir, dataset)
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)

    with open(dataset+'.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['file_path', 'class'])
        for file in files:
            writer.writerow([file, int(file[0])])


create_for('train')
create_for('val')