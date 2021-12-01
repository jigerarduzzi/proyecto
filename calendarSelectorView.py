from calendar import calendar
from tkinter import *
from tkcalendar import *
from datetime import datetime
from downloader import Downloader
from  tkinter import ttk

class CalendarSelector(object):

    def __init__(self):
        super(CalendarSelector, self).__init__()
        self.iniciarInterfaz()
        pass

    def iniciarInterfaz(self):

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

            #Verify if selected date is not weekend
            if (aux.weekday() < 5):
                if "*No se puede seleccionar fines de semana" in alert_array:
                    alert_array.remove("*No se puede seleccionar fines de semana")
            else: 
                if "*No se puede seleccionar fines de semana" not in alert_array:
                    alert_array.append("*No se puede seleccionar fines de semana")
                can_be_added = False

            #Verify if selected date is not future date
            if(datetime.strptime(str(selected_date), "%d/%m/%Y")<=datetime.strptime(present.strftime("%d-%m-%Y"),"%d-%m-%Y")):
                if "*No se puede seleccionar una fecha futura" in alert_array:
                    alert_array.remove("*No se puede seleccionar una fecha futura")
            else:
                if "*No se puede seleccionar una fecha futura" not in alert_array:
                    alert_array.append("*No se puede seleccionar una fecha futura") 
                can_be_added = False
                
            #Show alerts
            alert_string="" 
            for x in alert_array:
                #String to print alerts correctly
                alert_string=alert_string+"\n"+str(x)
            alert_label.config(text=alert_string)

            #Add to array if it is possible
            if(can_be_added) and (selected_date not in selected_dates):
                selected_dates.append(selected_date)
                my_label.config(text=selected_dates)    

        def handle_downloads():
            if len(selected_dates) > 0 :
                downloader = Downloader
                downloader.downloadFiles(selected_dates)
        
        alert_array=[]

        alert_label=Label(root,text="", fg="red")
        alert_label.pack(pady=10)


        select_date_button=Button (root, text="Seleccionar", command=grab_date)
        select_date_button.pack(pady=20)

        my_label=Label(root,text="")
        my_label.pack(pady=20)


        download_button=Button (root, text="Descargar", command=handle_downloads)
        download_button.pack(pady=20)

        root.mainloop()