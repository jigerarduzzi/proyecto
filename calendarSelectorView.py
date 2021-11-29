from calendar import calendar
from tkinter import *
from tkcalendar import *
from datetime import datetime
from clasificador import Downloader

selected_dates = []

root = Tk()
root.title('Seleccione las BORAS que desea descargar')
root.geometry("600x500")

#Set current date and set default selected date
present = datetime.now()
cal = Calendar(root, selectmode='day', year=int(present.strftime("%Y")), month=int(present.strftime("%m")), day=int(present.strftime("%d")), date_pattern="d/m/Y")
cal.pack(pady=20)

#Handle dates
def grab_date():
    selected_date = cal.get_date()
    can_be_added = True
    aux=datetime.strptime(str(selected_date), "%d/%m/%Y")
   # if (selected_date not in selected_dates) and (aux.weekday() < 5) and (datetime.strptime(str(selected_date), "%d/%m/%Y")<=datetime.strptime(present.strftime("%d-%m-%Y"),"%d-%m-%Y")):
    #    selected_dates.append(selected_date)
     #   my_label.config(text=selected_dates)

    #Verify if selected date is not weekend
    if (aux.weekday() < 5):
        alert_weekend_label.config(text="")
    else: 
        alert_weekend_label.config(text="*fin de semana")
        can_be_added = False

    #Verify if selected date is not future date
    if(datetime.strptime(str(selected_date), "%d/%m/%Y")<=datetime.strptime(present.strftime("%d-%m-%Y"),"%d-%m-%Y")):
        alert_future_date_label.config(text="")
    else: 
        alert_future_date_label.config(text="*fecha futura") 
        can_be_added = False

    #Add to array if it is possible
    if(can_be_added) and (selected_date not in selected_dates):
        selected_dates.append(selected_date)
        my_label.config(text=selected_dates)    

def handle_downloads():
    if len(selected_dates) > 0 :
        downloader = Downloader
        downloader.downloadFiles(selected_dates)

alert_weekend_label=Label(root,text="")
alert_weekend_label.pack(pady=10)
alert_future_date_label=Label(root,text="")
alert_future_date_label.pack(pady=10)


select_date_button=Button (root, text="Seleccionar", command=grab_date)
select_date_button.pack(pady=20)

my_label=Label(root,text="")
my_label.pack(pady=20)

download_button=Button (root, text="Descargar", command=handle_downloads)
download_button.pack(pady=20)

root.mainloop()