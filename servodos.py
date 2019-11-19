#!/usr/bin/python
# -*- coding: <encoding name> -*-  
from Tkinter import *
import RPi.GPIO as GPIO

from functools import partial
import time
import os



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





#funcion guarda dato de registro de usuario     
def registro_usuario():
 
    usuario_info = nombre_user.get()
    clave_info = clave_user.get()

 
    file = open(usuario_info, 'w')
    
    
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    clave.delete(0, END)
    nombre_apellido.delete(0, END)
        
 
    Label(registro, text="Registro completado con exito", fg="green", font=("calibri", 11)).pack()

                     
class App:


    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        #ServoMOTOR antebrazo
        scale = Scale(frame,from_=90, to=0,
              command=self.update12,
              length=900,
                 showvalue=1, width=80, relief=RAISED, orient=HORIZONTAL
                      , label = "Servo1 antebrazo")
        scale.grid()

        
        G = Button(frame, text ="Grado",command = self.ingresargrado)
        G.grid()
     
        R = Button(frame, text ="Registro", command = self.registro, state = ACTIVE)
        R.grid()

        B = Button(frame, text ="Ej1: 0 a 90", command = self.nines, state = ACTIVE)
        B.place(x=50, y=120)

        repeinput = Entry(frame, width=10, selectborderwidth=10)
        repeinput.place(x=150, y=125)

        scale2 = Scale(frame, from_=90, to=0,
               command=self.update16,
              length=200,showvalue=1,
                       width=10, relief=RAISED, orient=HORIZONTAL, label = "Servo2 mano", tickinterval = 30)
        scale2.grid()




    def update12(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm12.ChangeDutyCycle(duty)    

    def update16(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm16.ChangeDutyCycle(duty)
        
    def nines(self):
        global a
        a=0
    
        while (a<5):
            pwm12.ChangeDutyCycle(3)
            pwm16.ChangeDutyCycle(3)
            time.sleep(3)
            
            pwm12.ChangeDutyCycle(6)
            time.sleep(1)
            pwm12.ChangeDutyCycle(9)
            time.sleep(1)
            
            pwm12.ChangeDutyCycle(6)
            pwm16.ChangeDutyCycle(12)
            time.sleep(2)
            a = a+1


    #introducir grados por teclado       
    def ingresargrado(self):
        global ventanagrados
        ventanagrados=Tk()
        ventanagrados.title("Grados")
        ventanagrados.geometry("320x250")
        global primergrado
        global segundogrado

        
        global boton
        global inputgrado1
        global inputgrado2
        global grado1
        global grado2
        grado1 = StringVar()
        grado2 = StringVar()
        
        

        label = Label(ventanagrados, text="Introduzca grados")
        label.pack(anchor=CENTER)
        label.config(bg="LightGreen",
                     font=("Verdana " ,24))


        label_ngrado = Label(ventanagrados, text="1er grado * ")
        label_ngrado.pack()

        primergrado = Entry(ventanagrados, textvariable=grado1) 
        primergrado.pack()

        label_ngrado2 = Label(ventanagrados, text="2er grado * ")
        label_ngrado2.pack()

        segundogrado = Entry(ventanagrados, textvariable=grado2) 
        segundogrado.pack()


        boton = Button(ventanagrados, text="ok", command = nine).pack()

        
        
    #funcion de ventana registro para usuario
    def registro(self):
                      
        global registro
        registro=Tk()
        registro.title("Datos del paciente")
        registro.geometry("500x250")
        
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

                             
root = Tk()
root.wm_title('Servo Control')
appservo = App(root)
root.geometry("1000x500+0+0")
root.update()
root.deiconify()
root.mainloop()




