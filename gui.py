import customtkinter
from CTkDatePicker import CTkDatePicker
from CTkMessagebox import CTkMessagebox
from utils import get_icals, generate_table

class UpdateIcalsWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Update iCals")
        self.geometry("500x150")

        self.label = customtkinter.CTkLabel(self, text="Entrez l'URL tc-net")
        self.label.pack(pady=(10,0))
        #create an entry to enter the tc-net link
        self.url_entry = customtkinter.CTkEntry(self, width=400)
        self.url_entry.pack(pady=10)
        #create a button to update the icals
        self.update_button = customtkinter.CTkButton(self, text="Download iCals", command=self.download_icals)
        self.update_button.pack(pady=10)

    def download_icals(self):
        link = self.url_entry.get()
        if get_icals(link):
            CTkMessagebox(title="Info", message="Les iCals ont été téléchargés avec succès!", icon="check")
        else:
            CTkMessagebox(title="Error", message="Une erreur s'est produite lors du téléchargement des iCals.", icon="cancel")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("TC Room Finder ")
        self.toplevel_window = None

        #create a title at the top with modern font
        self.title_label = customtkinter.CTkLabel(self, text="TC Room Finder", font=("Arial", 24))
        self.title_label.pack(pady=20)
        
        #crate a frame for the setup part
        self.setup_frame = customtkinter.CTkFrame(self)
        self.setup_frame.pack(pady=20)
        #create a label to explain the datepicker
        self.date_label = customtkinter.CTkLabel(self.setup_frame, text="Sélectionnez une date")
        self.date_label.pack(padx=60, pady=(20,0))
        #créer un champ pour entrer la date avec datepicker
        self.date_picker = CTkDatePicker(self.setup_frame)
        self.date_picker.set_date_format("%d/%m/%Y")
        self.date_picker.set_allow_manual_input(False)
        self.date_picker.pack(pady=(0,20), after=self.date_label)
        #entrer l'heure de début avec une combobox
        self.begin_label = customtkinter.CTkLabel(self.setup_frame, text="Heure de début")
        self.begin_label.pack()
        self.begin_combobox = customtkinter.CTkComboBox(self.setup_frame, values=["08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00"])
        self.begin_combobox.pack(pady=(0,20), after=self.begin_label)
        #entrer la durée en heures et minutes (hh:mm) avec une combobox
        self.span_label = customtkinter.CTkLabel(self.setup_frame, text="Durée")
        self.span_label.pack()
        self.span_combobox = customtkinter.CTkComboBox(self.setup_frame, values=["00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00"])
        self.span_combobox.pack(pady=(0,20), after=self.span_label)

        #create a frame for buttons
        self.button_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(anchor="center", padx=30, pady=20)

        self.update_button = customtkinter.CTkButton(self.button_frame, text="Update iCals", command=self.update_icals_click)
        self.update_button.pack(side="left", padx=10)

        self.find_room_button = customtkinter.CTkButton(self.button_frame, text="Trouver ma salle", command=self.button_click)
        self.find_room_button.pack(side="left", padx=10)

    # add methods to app

    def update_icals_click(self):
        print("Update iCals !")
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = UpdateIcalsWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def button_click(self):
        print("button click")
        self.setup_frame.pack_forget()
        self.button_frame.pack_forget()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
app = App()
app.mainloop()