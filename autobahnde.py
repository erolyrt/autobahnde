from tkinter import *
import requests
import json

autobahn = Tk()
autobahn.geometry("600x600")
autobahn.title('Autobahn.de')

url = 'https://verkehr.autobahn.de/o/autobahn/{}/services/closure'

def getAutobahn(nr):
    data = requests.get(url.format(nr)).json()
    closures = data['closure']
    titles = []
    descriptions = []
    if data:
        for item in closures:
            title = item["title"]            
            description = item["description"][5]
            descriptions.append(description)
            titles.append(title)
        zipped_list = list(zip(titles, descriptions))
        def writing(sth):
            for i in range(len(sth)):
                print(sth[i])
                print("---------*********")
        a = writing(zipped_list)
    return (a)

def main():
    autobahn_number = autobahnEntry.get()
    incident = getAutobahn(autobahn_number)
    if incident:
        incidentLabel['text'] = f" Olay {incident[0]}"

autobahnEntry = Entry(autobahn, justify='center')
autobahnEntry.pack(fill=BOTH,ipady=10, padx=18, pady=5)

searchButton = Button(autobahn, text='Search', font=('Arial', 15), command=main)
searchButton.pack(fill=BOTH, ipady=10, padx=20)

incidentLabel = Label(autobahn, font=('Arial', 10))
incidentLabel.pack()


autobahn.mainloop()