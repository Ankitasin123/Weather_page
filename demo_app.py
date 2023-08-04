from tkinter import*
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9c3987cd7a02392484622a4847f9764c").json()

    weather_label.config(text=data["weather"][0]["main"])
    weatherd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    humidity_label1.config(text=data["main"]["humidity"])
    pressure_label1.config(text=data["main"]["pressure"])
    


 






wind = Tk()
wind.title("Weather")
wind.config(bg="green")
wind.geometry("450x550")

name_label = Label(wind,text="Weather App", font=("Time New Roman",35,"bold"))
name_label.place(x=25,y=50,height=50,width=400)

city_name = StringVar()
list_name= ["Ahmednagar","Akola","Amravati","Aurangabad","Beed","Bhandara","Buldhana","Chandrapur","Dhule","Gadchiroli","Gondia","Hingoli","Jalgaon","Jalna","Kolhapur","Latur","Mumbai City",
    "Mumbai Suburban","Nagpur","Nanded","Nandurbar","Nashik","Osmanabad","Palghar","Parbhani",
    "Pune","Raigad","Ratnagiri","Sangli","Satara","Sindhudurg","Solapur","Thane","Wardha","Washim","Yavatmal"]
com= ttk.Combobox(wind,text="Weather App",values=list_name,
                                font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=110,height=50,width=400)

weather_label = Label(wind,text="Weather Climate", font=("Time New Roman",10,"bold"))
weather_label.place(x=25,y=240,height=50,width=210)

weather_label1 = Label(wind,text="", font=("Time New Roman",10,"bold"))
weather_label1.place(x=210,y=240,height=50,width=210)

weatherd_label = Label(wind,text="Weather Discription", font=("Time New Roman",10,"bold"))
weatherd_label.place(x=25,y=300,height=50,width=210)

weatherd_label1 = Label(wind,text="", font=("Time New Roman",10,"bold"))
weatherd_label1.place(x=210,y=300,height=50,width=210)

temp_label = Label(wind,text="Temperature", font=("Time New Roman",10,"bold"))
temp_label.place(x=25,y=360,height=50,width=210)

temp_label1 = Label(wind,text="", font=("Time New Roman",10,"bold"))
temp_label1.place(x=210,y=360,height=50,width=210)

humidity_label = Label(wind,text="Humidity", font=("Time New Roman",10,"bold"))
humidity_label.place(x=25,y=420,height=50,width=210)

humidity_label1 = Label(wind,text="", font=("Time New Roman",10,"bold"))
humidity_label1.place(x=210,y=420,height=50,width=210)

pressure_label = Label(wind,text="Pressure", font=("Time New Roman",10,"bold"))
pressure_label.place(x=25,y=480,height=50,width=210)

pressure_label1 = Label(wind,text="", font=("Time New Roman",10,"bold"))
pressure_label1.place(x=210,y=480,height=50,width=210)

done_button = Button(wind,text="Done",font=("Time New Roman",15,"bold"),command=data_get)
done_button.place(y=180,height=50,width=100,x=180)

wind.mainloop()

