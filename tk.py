import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nom_label = tk.Label(self, text="Nom")
        self.nom_label.pack(side="top")
        self.nom_entry = tk.Entry(self)
        self.nom_entry.pack(side="top")

        self.dateNaissance_label = tk.Label(self, text="Date de Naissance")
        self.dateNaissance_label.pack(side="top")
        self.dateNaissance_entry = tk.Entry(self)
        self.dateNaissance_entry.pack(side="top")

        self.dateEmbauche_label = tk.Label(self, text="Date d'Embauche")
        self.dateEmbauche_label.pack(side="top")
        self.dateEmbauche_entry = tk.Entry(self)
        self.dateEmbauche_entry.pack(side="top")

        self.salaireBase_label = tk.Label(self, text="Salaire de Base")
        self.salaireBase_label.pack(side="top")
        self.salaireBase_entry = tk.Entry(self)
        self.salaireBase_entry.pack(side="top")

        self.submit_button = tk.Button(self)
        self.submit_button["text"] = "Submit"
        self.submit_button["command"] = self.submit
        self.submit_button.pack(side="top")

    def submit(self):
        nom = self.nom_entry.get()
        dateNaissance = datetime.strptime(self.dateNaissance_entry.get(), "%Y-%m-%d")
        dateEmbauche = datetime.strptime(self.dateEmbauche_entry.get(), "%Y-%m-%d")
        salaireBase = float(self.salaireBase_entry.get())
        # Create an instance of Employe, Formateur, or Agent here
        # For example: employe = Employe(nom, dateNaissance, dateEmbauche, salaireBase)
        messagebox.showinfo("Success", "Employee created successfully!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
