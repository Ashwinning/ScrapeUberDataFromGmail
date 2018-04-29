import gmail
from Settings import *
from Scraper import *
import os
from bs4 import BeautifulSoup
import csv

filenames = os.listdir('emails')

reciepts = []

for filename in filenames:
    with open('emails/'+filename, 'r') as file:
        print 'reading: ' + 'emails/'+filename
        soup = BeautifulSoup(file)
        details = GetDetails(soup)
        print details
        reciepts.append(details)


def export_dict_list_to_csv(data, filename):
    with open(filename, 'wb') as f:
        # Assuming that all dictionaries in the list have the same keys.
        headers = sorted([k for k, v in data[0].items()])
        csv_data = [headers]
        for d in data:
            csv_data.append([d[h].encode('utf8') for h in headers])
        writer = csv.writer(f)
        writer.writerows(csv_data)

export_dict_list_to_csv(reciepts, 'uber-commute-data.csv')
