from tkinter import *
import requests
import json 

window = Tk()
window.title("Welcome to ABCD")
l1 = Label(window,text= "Weather App", bg="yellow", fg="blue", width=40)
l1.place(x=560,y=200)

img = PhotoImage(file="C:/Users/LENOVO/Pictures/Saved Pictures/logo.png")
l2 = Label(window, image= img)
l2.pack()

v = StringVar()

def action():
    city = v.get()
    url= "http://api.weatherapi.com/v1/current.json?key=feff49cb9758454bb9962819231409&q="+city

    df= requests.get(url)
    data=json.loads(df.content)
    l3.config(text="Temperature in Celcicus :-" + str(data['current']['temp_c']),bg="yellow",fg="blue")
    l4.config(text="Location :-" + str(data['location']['name']),bg="yellow",fg="blue")
    




e1 = Entry(window, width=20, font=("Calibri,20"),textvariable=v)
e1.place(x=560,y=240)

b1 = Button(window, text="Submit", bg="Green", fg="yellow", command=action)
b1.place(x=560,y=280)

l3 = Label(window,text= "Weather Forcasting", bg="yellow", fg="blue", width=40)
l3.place(x=560,y=320)

l4 = Label(window,text="Get Location", bg="yellow", fg="blue", width=40)
l4.place(x=560,y=360)

#l1.place(x=500,y=200)
#l1.grid(row=0,column=5)
#window.minsize(width=300,height=600)
#window.maxsize(width=800,height=1000)
window.mainloop()
