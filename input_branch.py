import requests
from pprint import pprint
import json
import pandas as pd
import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog 
from PyQt5.QtCore import Qt

###### Issues to work on ######
#Why is ico not working?
# get pyinstaller to work ( Some required 
# modules, shared libs or data files are not frozen (packaged, bundled) into the resulting exec)
#Loading module hook 'hook-PyQt5.p
# open csv

root = tk.Tk()
root.geometry("600x600")

root.title("Label Generator")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='images/trash_sml.png'))
#root.iconbitmap("images/hnet.com-image.ico")

#save user input 
def save_info():
    release_id_save = id_text.get(1.0, END)
    print(release_id_save)
    file = open("release.txt", "w")
    file.write(str(release_id_save))
    file.close()


#open csv
def open_csv():
    os.remove("release.txt")
    csv =filedialog.askopenfilename()
    os.system(csv)

#Label Generator
def run_label():
    with open('release.txt') as f:
         file = f.read()
    # convert string to list of release ids
    record_list = file.split()

    # define url to request release id informtion
    app_url = 'https://api.discogs.com/releases/'

    # create a DataFrame to put release ids into
    master_df = pd.DataFrame()

    # for each release id in record list
    for record_id in record_list:
        record_id = str(record_id)

        # full request url
        url = ''.join([app_url, record_id])

        # discogs response (json formatted)
        resp = requests.get(url)

        #  convert response to json object
        resp_json = json.loads(resp.text)

        # artist
        artist = resp_json['artists'][0]['name']

        # title
        title = resp_json['title']

        # label
        label = resp_json['labels'][0]['name']

        # format
        format_type = resp_json['formats'][0]['descriptions'][0]

        # year of release
        year = str(resp_json['year'])

        # country
        country = resp_json['country']

        # put data in dictionary
        record_data = {'record_id':[record_id],
                  'artist': [artist],
                  'title': [title],
                  'label': [label],
                  'format': [format_type],
                  'year': [year],
                  'country': [country]}
     
         # convert dictionary into DataFrame
        df = pd.DataFrame.from_dict(record_data)
        #     if the master data fram is empty
        if master_df.empty:
        #         turn the release id df to the master
            master_df = df
    
        else:
        #         if the master df exists, add the relase df to the master df
            master_df = pd.concat([master_df, df])
        
        master_df.to_csv('test.csv')



heading = Label(text="Enter the release id's bellow", bg ='#3492eb', fg='white', font='10', width='600', height='3')
heading.pack()

#text box 
id_text = Text(root)
id_text.pack()

button_frame = Frame(root)
button_frame.pack()

save_releases =tk.Button(root, text="Upload Id's", fg="white", bg="#3492eb", command= save_info)
save_releases.pack(fill = X)


findIDS =tk.Button(root, text="Run Generator", fg="white", bg="#3492eb", command= run_label)
findIDS.pack(fill = X)

openCSV =tk.Button(root, text="Create CSV", fg="white", bg="#3492eb", command= open_csv)
openCSV.pack(fill = X)

root.mainloop()