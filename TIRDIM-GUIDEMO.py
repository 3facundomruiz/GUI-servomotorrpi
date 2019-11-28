#!/usr/bin/python
# -*- coding: <encoding name> -*-  
from Tkinter import *
import RPi.GPIO as GPIO
from PIL import Image
from tkcalendar import *


#defino GPIO INPUT o OUT#
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

##Mando pwm de GPIOs##
pwm12 = GPIO.PWM(12, 80)
pwm16 = GPIO.PWM(16, 80)

###Angulo de inicio de cada motor###
pwm12.start(0)
pwm16.start(0)
global a


        
class App:


    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        frame=root


        label = Label(frame, text= "TIRDIM - GUI")
        label.pack(side=TOP)
        label.config(font=("Courier " ,25, "bold"))

        G = Button(frame, text ="Uso de Interfaz",command = self.ingresargrado)
        G.config(font=("Courier", 12))
        G.pack( side=LEFT, padx=200)
     

        R = Button(frame, text ="Sobre Nosotros", command = self.sn, state = ACTIVE)
        R.config(font=("Courier", 12))
        R.pack(  side=RIGHT, padx=200)

        
        S = Button(frame, text ="EMPEZAR", command = self.indie, state = ACTIVE)
        S.config(font=("Courier", 12))
        S.pack(  side=TOP)
        
        """
        lbl1 = Label(frame, width=15, height=3, bg='SlateGray2')
        lbl1.pack(side=TOP, pady=15, padx=10)

        lbl2 = Label(frame, width=15, height=3, bg='SlateGray3')
        lbl2.pack(side=TOP, padx=10)

        lbl3 = Label(frame, width=15, height=3, bg='SlateGray4')
        lbl3.pack(side=TOP, pady=100, padx=100)
        """


        


    #introducir grados por teclado       
    def ingresargrado(self):
        global indicaciones
        indicaciones=Tk()
        indicaciones.title("GUI indicaciones")
        indicaciones.geometry("1000x500+400+100")
        
        label = Label(indicaciones, text= "PARA UN USO CORRECTO DE LA GUI, SEGUIR LOS SIGUIENTES PASOS:")
        label.grid()
        label.config(bg="navajo white",
                     font=("Times " ,18))
        
        label = Label(indicaciones, text= "1. Antes de usar esta aplicacion, el medico debera hacer habilitar el uso de la misma")
        label.grid(row=1)
        label.config(font=("Times " ,18))
                
        label = Label(indicaciones, text= "2. En esta aplicacion hay 2 tipos de rehabilitacion:")
        label.grid(row=2)
        label.config(font=("Times " ,18),bg="gray70")

        label = Label(indicaciones, text= "La rehabilitacion 1, cuenta con 3 escalas las cuales tienen un limite de angulo hasta los 90grados")
        label.grid(row=3)
        label.config(font=("Times " ,18),bg="gray70")

        label = Label(indicaciones, text= "La rehabilitacion 2, cuenta con 3 escalas las cuales mueven 3 servomotores distintos")
        label.grid(row=4)
        label.config(font=("Times " ,18),bg="gray70")

        
        
    #funcion de ventana  para usuario
    def sn(self):
                      
        global instagram
        instagram=Tk()
        
        instagram.title("INSTAGRAM")
        instagram.geometry("250x50")
        
        label = Label(instagram, text= "@tirdim3d")
        label.pack(anchor=CENTER)
        label.config(bg="LightGreen",
                     font=("Times " ,24))




    def indie(self):
        global indi
        indi=Tk()
        indi.wm_title('TIPO DE REHABILITACION')
        indi.geometry("600x100+550+95")

        label = Label(indi, text= "ELEGIR EL TIPO DE TRATAMIENTO")
        label.pack(anchor=CENTER)
        label.config(bg="SteelBlue1",
                     font=("Times" ,18),width=200)

        uno = Button(indi, text ="Rehabilitcion 1", command = self.runo, state = ACTIVE)
        uno.config(font=("Courier", 12))
        uno.pack()

        
        dos = Button(indi, text ="Rehabilitacion 2", command = self.indie, state = ACTIVE)
        dos.config(font=("Courier", 12))
        dos.pack()


      



        
    def runo(self):
        global rservouno
        rservouno=Tk()
        rservouno.wm_title('REHABILITACION 1')
        rservouno.geometry("600x450+550+650")
        
        
        
        scale = Scale(rservouno, from_=0, to=30,
        command=self.update12,
        length=600,showvalue=1,
        width=40, relief=RAISED, orient=HORIZONTAL, label = "Servo1 CODO", tickinterval = 10)
        scale.grid()

        scale1 = Scale(rservouno, from_=30, to=60,
        command=self.update12,
        length=600,showvalue=1,
        width=40, relief=RAISED, orient=HORIZONTAL, label = "Servo1 CODO", tickinterval = 10)
        scale1.grid()

        
        scale2 = Scale(rservouno, from_=60, to=90,
        command=self.update12,
        length=600,showvalue=1,
        width=40, relief=RAISED, orient=HORIZONTAL, label = "Servo1 CODO", tickinterval = 10)
        scale2.grid()

        uno = Button(rservouno, text ="REGISTRO", command = self.cal)
        uno.config(font=("Courier", 12))
        uno.grid()
        

    def cal(self):
        global cal
        cal=Tk()
        cal.wm_title('REGISTRO')
        cal.geometry("350x400+100+200")
        

        cal = Calendar(cal, font = "Arial 14", selectmode="day", year=2019, month=5, day=17)
        cal.grid()



    
        
    def update12(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm12.ChangeDutyCycle(duty) 




        







        
        """
        global nombre_user
        global clave_user
        global nombre_apellido
        global clave
        nombre_user = StringVar()
        clave_user = StringVar()

        label = Label(registro, text= "Introduzca sus datos")
        label.pack(anchor=CENTER)
        label.config(bg="LightGreen",
                     font=("Verdana " ,24))


        label_nombre = Label(registro, text="Nombre de usuario * ")
        label_nombre.pack()

        nombre_apellido = Entry(registro, textvariable=nombre_user) #ESPACIO PARA INTRODUCIR EL NOMBRE.
        nombre_apellido.pack()

        label_clave = Label(registro, text="Clave * ")
        label_clave.pack()

        clave = Entry(registro, textvariable=clave_user, show='*') #ESPACIO PARA INTRODUCIR EL NOMBRE.
        clave.pack()

        Label(registro, text="").pack

        Button(registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack()
"""
                             
root = Tk()



myimage = PhotoImage(file='/home/pi/Desktop/tirdim/mmm.png')
mylabel = Label(root, image=myimage)
mylabel.place(x=0, y=0)

myimage2 = PhotoImage(file='/home/pi/Desktop/tirdim/foto.gif')
mylabel = Label(root, image=myimage2)
mylabel.pack()





"""
imagenAnchuraMaxima=300
imagenAlturaMaxima=200

myimage2 = PhotoImage(file='/home/pi/Desktop/tirdim/insta.png')
myimage2.geometry(10x10)
mylabel = Label(root, image=myimage2)
mylabel.pack(side=TOP)
"""


root.wm_title('Servo Control')
appservo = App(root)
root.geometry("1680x1000+0+0")
root.update()
root.deiconify()
root.mainloop()


            
