from tkinter import *
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.mWindow = tkinter.Tk()
        self.mFrame = Frame(self.mWindow, width=300, height=65)

# yesBtn = tkinter.Button(top_frame, text = "YES", fg = "green").pack()
# tkinter.Label(window, text = "Welcome to your SABER command line! Say one of these commands to see something cool. Waiting for commands...", fg = "white", bg = "black").pack(fill = "x")
        
    def ErrorWindow(self,message):
        self.mWindow.title("ERROR")
        x = self.mWindow.winfo_screenwidth()
        y = self.mWindow.winfo_screenheight()
        self.mWindow.geometry("300x165+{0}+{1}".format(int(x/2 - 150),int(y/2 - 100)))
        tkinter.Label(self.mWindow, text = message, fg = "black", bg = "white").pack(fill = "x", pady = 20, ipady = 10)
        tkinter.Button(self.mWindow, text = "Ok", bg = "blue" , command = self.mWindow.quit).pack(ipadx = 20)
        def end(aaa):
            #self.mWindow.destory()
            self.mWindow.quit()

        self.mWindow.bind("<Return>", end)
        self.mFrame.pack()
        
        
        self.mWindow.mainloop()
        #while True:
        #    self.mWindow.update()

    def StringMessage(self,message):
        self.mWindow.title("MESSAGE")
        x = self.mWindow.winfo_screenwidth()
        y = self.mWindow.winfo_screenheight()
        self.mWindow.geometry("300x165+{0}+{1}".format(int(x/2 - 150),int(y/2 - 100)))
        tkinter.Label(self.mWindow, text = message, fg = "black", bg = "white").pack(fill = "x", pady = 20, ipady = 10)
        tkinter.Button(self.mWindow, text = "Ok", bg = "blue" , command = self.mWindow.quit).pack(ipadx = 20)
        def end(aaa):
            #self.mWindow.destory()
            self.mWindow.quit()

        self.mWindow.bind("<Return>", end)
        self.mFrame.pack()
        
        
        self.mWindow.mainloop()

    def YesNo(self,message):
        self.mWindow.title("QUESTION")
        x = self.mWindow.winfo_screenwidth()
        y = self.mWindow.winfo_screenheight()
        self.mWindow.geometry("300x165+{0}+{1}".format(int(x/2 - 150),int(y/2 - 100)))
        self.retval = False
        def endYes():
            self.retval = True
            self.mWindow.quit()
        def endNo():
            self.retval = False
            self.mWindow.quit()
        tkinter.Label(self.mWindow, text = message, fg = "black", bg = "white").pack(fill = "x", pady = 20, ipady = 10)
        tkinter.Button(self.mWindow, text = "Yes", bg = "green" , command = endYes).pack(ipadx = 20, padx = 50, side = LEFT)
        tkinter.Button(self.mWindow, text = "No", bg = "green" , command = endNo).pack(ipadx = 20, padx = 20, side = LEFT)
        self.mFrame.pack()

        self.mWindow.mainloop()
        return self.retval            

def main():
    new = GUI()
    new.YesNo("You done effed up?")

#main()
