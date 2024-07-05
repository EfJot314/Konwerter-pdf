import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image


class Application():
    def __init__(self):
        #variables
        self.paths = []
        self.im = []

        #window
        self.root = tk.Tk()
        self.root.title("Konwerter PDF")
        self.root.geometry('700x600')

        self.scroll = tk.Scrollbar(self.root)

        self.textbox = tk.Text(self.root, width = 80, 
                               height = 10, yscrollcommand = self.scroll.set)

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

        #run application
        self.root.mainloop()


    def openfile(self):
        #get file
        file_name = fd.askopenfilename()
        self.paths.append(file_name)
        #show chosen files
        self.textbox.insert(tk.END, file_name)
        self.textbox.insert(tk.END, "\n")

   
    def convert(self):
        # "Save As" window
        save_path = fd.asksaveasfilename(filetypes=[("Plik PDF","*.pdf")], defaultextension = "*.pdf")
        #concat images to one .pdf file
        n = len(self.paths)
        if n > 0:
            first = Image.open(self.paths[0])
            first = first.convert('RGB')
            for i in range(1, n):
                self.im.append(Image.open(self.paths[i]))
                self.im[i-1] = self.im[i-1].convert('RGB')
        #save
        first.save(save_path, save_all=True, append_images = self.im)

        #UI
        self.end_label = tk.Label(self.root, text = "Pliki zostały skonwertowane do formatu .pdf !")
        self.end_label.pack()
        self.textbox.delete("1.0","end")

        #clear variables
        self.paths = []
        self.im = []
        


apk = Application()