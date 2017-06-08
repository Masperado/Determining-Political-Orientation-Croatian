import _pickle as cPickle
from sklearn.svm import SVC
from Vectorizer import vectorize
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from sklearn.model_selection import train_test_split,GridSearchCV


class MainWindow:
    def __init__(self,master):
        # zabranimo proširivanje glavnog prozora
        master.resizable(width=False, height=False)

        # Nađimo gdje će glavni prozor stajati na ekranu i pozicionirajmo ga tamo
        width = 1000  # Širina prozora u pikselima, namješteno uz brojne pokušaje
        height = 600  # Visina prozora u pikselima, namješteno uz brojne pokušaje
        ws = master.winfo_screenwidth()  # Visina ekrana u pikselima
        hs = master.winfo_screenheight()  # Širina ekrana u pikselima
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))  # Funckija za pozicioniranje

        self.textInput=ScrolledText(master, font = "Helvetica 20 bold", bg="red")
        self.textInput.place(x=0,y=0,width=1000,height=200)
        self.button=Button(master,text="Odredi orijentaciju", font = "Helvetica 20 bold", bg="white", command=self.odredi)
        self.button.place(x=0,y=200,width=1000, height=200)
        self.result=Label(master, bg="blue", font = "Helvetica 20 bold", text="Unesite prvi komentar")
        self.result.place(x=0, y=400, width=1000, height=200)

    def odredi(self):
        a=self.textInput.get(1.0,END)
        orijen=ml.predict(vectorize(a))
        print(orijen)
        if orijen==1:
            self.result.configure(text="Autor komentara je LIJEVE političke orijentacije.")
        elif orijen==2:
            self.result.configure(text="Autor komentara je NEUTRALNE političke orijentacije.")
        elif orijen==3:
            self.result.configure(text="Autor komentara je DESNE političke orijentacije.")


ml= SVC()
with open('modelK1.txt', 'rb') as dict_items_open:
    ml = cPickle.load(dict_items_open)
print(ml)
root=Tk()
root.title("Određivač političke orijentacije")
mainWindow=MainWindow(root)
root.mainloop()