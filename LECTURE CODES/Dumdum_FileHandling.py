import os
import time
from os import makedirs
import csv
import gspread

'''
#print(os.listdir(os.getcwd()))
#print(os.getcwd())

basepath = os.path.dirname(os.path.abspath(__file__))
#print(basepath)


with open("NewFile.txt", "w", newline='') as file:
    file.write(str(time.time()))
    print("New file created:", file.name)

time.sleep(10)

for root, dirs, files in os.walk(basepath):
    for filename in files :
        if filename == "NewFile.txt":
            filepath = os.path.join(root, filename)
            print("found it, name:", filename)
            print("the directory:", root)
            time.sleep(5)
            os.remove(filepath)
            print("removed:", filename)
            break

csv_data = []

# ---------------- READ CSV ----------------
with open(CSV_PATH, mode='r', newline='') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)
        csv_data.append(row)

print("--------------------------------------")
print(csv_data)        # list of lists
print(csv_data[2])     # third row

# NAME is column index 1
# ADDRESS is column index 5

csv_new_data = []

for row in csv_data[1:]:   # skip header
    if len(row) == 6:
        csv_new_data.append([row[1], row[5]])


print(csv_new_data)

# ---------------- WRITE CSV ----------------
with open(os.path.join(CSV_FOLDER, "WRITE_CSV.csv"), mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["NAME", "ADDRESS"])   # optional header
    writer.writerows(csv_new_data)
'''


import os                                   # OS utilities for file paths
import gspread                              # Google Sheets library
from oauth2client.service_account import ServiceAccountCredentials  # Service account auth
from googleapiclient.errors import HttpError  # Google API error handling
from gspread.utils import ValueInputOption    # Input option constants


BASE_PATH = os.path.dirname(os.path.abspath(__file__))  # Directory where this script is located

CSV_FOLDER = os.path.join(BASE_PATH, "CSV")             # Path to CSV folder
CSV_PATH = os.path.join(CSV_FOLDER, "myfirstCSV.csv")   # Full path to CSV file

RESOURCE_FOLDER = os.path.join(BASE_PATH, "CSV")        # Folder containing credentials JSON

SERVICE_KEY = os.path.join(
    RESOURCE_FOLDER,
    "dumdumproject-6b6f1ad2511c.json"                    # Service account key file
)

credential = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_KEY,
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",  # Sheet read/write
        "https://www.googleapis.com/auth/drive"          # File access & metadata
    ]
)

client = gspread.authorize(credential)                  # Authorize gspread client
sheet_url = "https://docs.google.com/spreadsheets/d/12u_J4N_xZowE3uHtK5Y4w2flpIsi37zAzevTuw3lAH4/edit?gid=0#gid=0"
gs_instance = client.open_by_url(sheet_url)              # Open spreadsheet using URL (no Drive scope)
sheet_instance = gs_instance.get_worksheet(0)            # Access first worksheet by index
googlesheet_data_tab0 = sheet_instance.get_all_values()

print(googlesheet_data_tab0)                             # Display retrieved data
new_row_data = [4, "Red Red", "BSECE", "1st", 4, "Antipolo City"]
sheet_instance.append_row(new_row_data)


