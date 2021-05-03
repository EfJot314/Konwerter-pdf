import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image

class Application():
    def __init__(self):
        self.path = []
        self.im = []

        self.root = tk.Tk()
        self.root.title("Konwerter PDF")
        self.root.geometry('700x600')

        self.przew = tk.Scrollbar(self.root)

        self.textbox = tk.Text(self.root, width = 80, 
                               height = 10, yscrollcommand = self.przew.set)

        self.label1 = tk.Label(self.root, text = "Konwerter PDF", font = ("Times New Roman", 25))
        self.label2 = tk.Label(self.root, text = "Wybrane pliki:")

        self.button1 = tk.Button(self.root, text = "Wybierz plik", width=20)
        self.button2 = tk.Button(self.root, text = "Konwertuj", width=20)

        self.button1.config(command = lambda: self.openfile())
        self.button2.config(command = lambda: self.convert())
        
        

        self.label1.pack()
        self.button1.pack()
        self.label2.pack()
        self.textbox.pack()
        self.button2.pack()

        self.root.mainloop()

    def openfile(self):
        var = fd.askopenfilename()
        self.path.append(var)
        self.textbox.insert(tk.END, var)
        self.textbox.insert(tk.END, "\n")

   
        

    def convert(self, PATH = None):
        self.save = fd.asksaveasfilename(filetypes=[("Plik PDF","*.pdf")], defaultextension = "*.pdf")
        for i in range(len(self.path)):
            if i == 0:
                first = Image.open(self.path[i])
                first = first.convert('RGB')
            else:
                self.im.append(Image.open(self.path[i]))
                self.im[i-1] = self.im[i-1].convert('RGB')
        if PATH == None:
            PATH = self.save

        first.save(PATH, save_all=True, append_images = self.im)

        self.end_label = tk.Label(self.root, text = "Pliki zostały skonwertowane do formatu .pdf !")
        self.end_label.pack()
        self.path = []
        self.im = []
        self.textbox.delete("1.0","end")


apk = Application()