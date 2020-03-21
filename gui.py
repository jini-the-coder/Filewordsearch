from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class Gui:
    def __init__(self):
        self.filename = ""
        self.i = 0
        self.press = 0
        self.setupUI()

    def setupUI(self):
        self.root = Tk()
        self.root.title("Word search engine")

        self.mainFrame = Frame(self.root)
        self.mainFrame.pack(fill=BOTH, expand=0)

        label1 = Label(self.mainFrame, text="Word Search Engine", font="fangsongti 30 bold")
        label1.grid(row=0, column=0)

        label2 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label2.grid(row=1, column=0)

        label3 = Label(self.mainFrame, text="Enter the input file", font="fangsongti 20 bold")
        label3.grid(row=2, column=0)

        label4 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label4.grid(row=3, column=0)

        button1 = Button(self.mainFrame, text='BROWSE', font="fangsongti 15 bold", command=self.filedialog)
        button1.grid(row=4, column=0)

        label5 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label5.grid(row=5, column=0)

        label7 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label7.grid(row=7, column=0)

        label8 = Label(self.mainFrame, text="Enter search word", font="fangsongti 20 bold")
        label8.grid(row=8, column=0)

        label9 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label9.grid(row=9, column=0)

        self.entry = Entry(self.mainFrame, font="fangsongti 15 bold")  # word taken as input for search
        self.entry.grid(row=10, column=0, padx=10)

        label10 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label10.grid(row=11, column=0)

        button2 = Button(self.mainFrame, text='SEARCH', font="fangsongti 15 bold", command=self.status)
        button2.grid(row=12, column=0)

        label11 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label11.grid(row=13, column=0)

        self.text = Text(self.mainFrame, height=1, width=15)   # display time
        self.text.config(font=("fangsongti", 15))
        self.text.grid(row=14, column=0, padx=10)

        label12 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label12.grid(row=15, column=0)

        button4 = Button(self.mainFrame, text='CLOSE', font="fangsongti 15 bold", command=self.close)
        button4.grid(row=16, column=0)

        label13 = Label(self.mainFrame, text="", font="fangsongti 20 bold")
        label13.grid(row=17, column=0)

    def close(self):
        self.root.destroy()

    def status(self):
        a = self.entry.get().upper()
        if(self.filename == ""):
            messagebox.showinfo("Opps !!!", "Please enter the input file")
        elif(a==""):
            messagebox.showinfo("Opps !!!", "Please enter the word to be searched")
        else:
            file1 = open(self.filename, "r")
            list = file1.readlines()
            while (self.i < len(list)):
                lists = list[self.i].upper().split(" ")
                lists[len(lists)-1]=lists[len(lists)-1].split("\n")[0]
                if a in lists:
                    self.text.delete("1.0", END)
                    self.text.insert(END, self.i+1)
                    self.press=1
                    self.i += 1
                    break
                self.i+=1
            if(self.i == len(list) and self.press==1):
                messagebox.showinfo("Opps !!!", "End of file")
                self.i=0
            elif(self.i == len(list) and self.press==0):
                self.text.delete("1.0", END)
                self.text.insert(END, "NOT FOUND")
            file1.close()


    def filedialog(self):
        self.filename = ""
        self.press = 0
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("all files", "*.*"),("jpeg files", "*.jpg")))
        label6 = Label(self.mainFrame, text=self.filename)
        label6.grid(row=6, column=0)

if __name__ == '__main__':
    g = Gui()
    mainloop()

