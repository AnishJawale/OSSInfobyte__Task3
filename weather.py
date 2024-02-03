from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3d637637909da1befc555f9ed9714bf4")

   
    w_label1.config(text="")
    wb_label1.config(text="")
    t_label1.config(text="")
    p_label1.config(text="")

    if response.status_code == 200:
        data = response.json()
        w_label1.config(text=f"Climate: {data['weather'][0]['main']}")
        wb_label1.config(text=f"Weather Description: {data['weather'][0]['description']}")
        t_label1.config(text=f"Temperature: {data['main']['temp'] - 273.15} °C")
        p_label1.config(text=f"Pressure: {data['main']['pressure']} hPa")
    else:
        error_message = f"Failed to get weather data for {city}. Please check the city name."
        print(error_message)
        w_label1.config(text=error_message)

root = Tk()
root.title("Weather App")
root.config(bg="#4CAF50")
root.geometry("500x570")


label_style = {"font": ("Arial", 16), "bg": "#4CAF50", "fg": "white"}
button_style = {"font": ("Arial", 16, "bold"), "bg": "#333", "fg": "white"}

name_label = Label(root, text="Weather App", font=("Times New Roman", 30, "bold"), bg="#4CAF50", fg="white")
name_label.place(x=25, y=30, height=50, width=450)

city_name = StringVar()
list_names = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(root, values=list_names, font=label_style, textvariable=city_name)
com.place(x=25, y=100, height=40, width=450)

w_label1 = Label(root, **label_style)
w_label1.place(x=25, y=180, height=40, width=450)

wb_label1 = Label(root, **label_style)
wb_label1.place(x=25, y=240, height=40, width=450)

t_label1 = Label(root, **label_style)
t_label1.place(x=25, y=300, height=40, width=450)

p_label1 = Label(root, **label_style)
p_label1.place(x=25, y=360, height=40, width=450)

done_button = Button(root, text="Get Weather", command=data_get, **button_style)
done_button.place(y=430, height=50, width=200, x=150)

root.mainloop()
