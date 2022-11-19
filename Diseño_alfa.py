import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_406=tk.Button(root)
        GButton_406["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_406["font"] = ft
        GButton_406["fg"] = "#e02323"
        GButton_406["justify"] = "center"
        GButton_406["text"] = "Limpiar"
        GButton_406["relief"] = "flat"
        GButton_406.place(x=60,y=40,width=70,height=25)
        GButton_406["command"] = self.GButton_406_command

        GButton_926=tk.Button(root)
        GButton_926["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_926["font"] = ft
        GButton_926["fg"] = "#273fda"
        GButton_926["justify"] = "center"
        GButton_926["text"] = "Analizar"
        GButton_926.place(x=200,y=40,width=70,height=25)
        GButton_926["command"] = self.GButton_926_command

        GButton_17=tk.Button(root)
        GButton_17["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_17["font"] = ft
        GButton_17["fg"] = "#2fa3d2"
        GButton_17["justify"] = "center"
        GButton_17["text"] = "Elegir archivo"
        GButton_17.place(x=320,y=40,width=90,height=25)
        GButton_17["command"] = self.GButton_17_command

        GButton_116=tk.Button(root)
        GButton_116["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_116["font"] = ft
        GButton_116["fg"] = "#e4af25"
        GButton_116["justify"] = "center"
        GButton_116["text"] = "Salir"
        GButton_116.place(x=470,y=40,width=70,height=25)
        GButton_116["command"] = self.GButton_116_command

        GLabel_39=tk.Label(root)
        GLabel_39["anchor"] = "nw"
        GLabel_39["bg"] = "#ebcd26"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_39["font"] = ft
        GLabel_39["fg"] = "#333333"
        GLabel_39["justify"] = "center"
        GLabel_39["text"] = "Programa de análisis "
        GLabel_39.place(x=210,y=10,width=170,height=25)

        GRadio_841=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_841["font"] = ft
        GRadio_841["fg"] = "#333333"
        GRadio_841["justify"] = "center"
        GRadio_841["text"] = "Carga"
        GRadio_841.place(x=30,y=130,width=85,height=25)
        GRadio_841["command"] = self.GRadio_841_command

        GRadio_11=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_11["font"] = ft
        GRadio_11["fg"] = "#333333"
        GRadio_11["justify"] = "center"
        GRadio_11["text"] = "Descarga"
        GRadio_11.place(x=150,y=130,width=85,height=25)
        GRadio_11["command"] = self.GRadio_11_command

        GRadio_400=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_400["font"] = ft
        GRadio_400["fg"] = "#333333"
        GRadio_400["justify"] = "center"
        GRadio_400["text"] = "0,5Hz"
        GRadio_400.place(x=260,y=130,width=85,height=25)
        GRadio_400["command"] = self.GRadio_400_command

        GRadio_863=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_863["font"] = ft
        GRadio_863["fg"] = "#333333"
        GRadio_863["justify"] = "center"
        GRadio_863["text"] = "1,0Hz"
        GRadio_863.place(x=360,y=130,width=85,height=25)
        GRadio_863["command"] = self.GRadio_863_command

        GRadio_132=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_132["font"] = ft
        GRadio_132["fg"] = "#333333"
        GRadio_132["justify"] = "center"
        GRadio_132["text"] = "1,5Hz"
        GRadio_132.place(x=460,y=130,width=85,height=25)
        GRadio_132["command"] = self.GRadio_132_command

        GMessage_296=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_296["font"] = ft
        GMessage_296["fg"] = "#333333"
        GMessage_296["justify"] = "center"
        GMessage_296["text"] = "Aquí se presenta resultados"
        GMessage_296.place(x=160,y=200,width=214,height=38)

    def GButton_406_command(self):
        print("command")


    def GButton_926_command(self):
        print("command")


    def GButton_17_command(self):
        print("command")


    def GButton_116_command(self):
        print("command")


    def GRadio_841_command(self):
        print("command")


    def GRadio_11_command(self):
        print("command")


    def GRadio_400_command(self):
        print("command")


    def GRadio_863_command(self):
        print("command")


    def GRadio_132_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
