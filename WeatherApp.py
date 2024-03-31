from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import time
import tkinter.messagebox as tmsg           #########  librarys
import asyncio
import customtkinter as ctk
from bs4 import BeautifulSoup
import requests


if __name__=="__main__":
    def WindowSize(Width,Height):  #### window size function
        root.geometry(f"{Width}x{Height}")
        root.minsize(Width,Height)
        root.maxsize(Width,Height)

root = ttkb.Window(themename="litera")


#################   date day function
if __name__=="__main__":
    def DateDay():
        Daydate = time.strftime("%A %d %B %Y")
        DateLabel.configure(text=Daydate)
        root.after(1000,DateDay)

if __name__=="__main__":
    def CurrentTimeFunc():  ###  current time
        currtime = time.strftime("%I:%M:%S %p")
        CurrentTime.configure(text=currtime)
        root.after(1000,CurrentTimeFunc)

##################  main app function

if __name__=="__main__":
    def WeatherAppFunction():
        PlaceName = PlaceVar.get()   #######  geting name from entry box
        PlaceName = PlaceName.capitalize()

        if PlaceName == "":
            tmsg.showinfo("Entry","Enter place name")
        else:
            CityNamevar.set(PlaceName)
            if __name__=="__main__":
                async def WeatherUrl(CityName):   ##########  getting weather data url
                    try:
                        weatherLink = requests.get(f"https://www.wunderground.com/weather/in/{CityName}")
                        global Weather
                        Weather = BeautifulSoup(weatherLink.content,"html.parser")
                    except Exception as err:
                        tmsg.showerror("error...",err)

            if __name__=="__main__":
                async def SunMoonUrl(RiseSet):   ##########  getting sun and moon url
                    try:
                        SunMoonLink = requests.get(f"https://www.wunderground.com/hourly/in/{RiseSet}") 
                        global SunMoon
                        SunMoon = BeautifulSoup(SunMoonLink.content,"html.parser")
                    except Exception as err:
                        tmsg.showerror("error...",err)

                asyncio.run(WeatherUrl(CityName=PlaceName))
                asyncio.run(SunMoonUrl(RiseSet=PlaceName))

            try:
                FahrenheitTemperature = Weather.find_all("span",class_="temp")   #########  celcius temperature
                FahrenheitTemp = int(FahrenheitTemperature[0].text[:2])
                celciusTemp = (FahrenheitTemp-33)*5/9
                CelciusVar.set(str(int(celciusTemp))+"°C")
                FeelsLikeVar.set(str(int(celciusTemp))+"°")  ### feels like
                FeelsLikeTextvar.set("Feels Like")
                CelciusFahrenheitVar.set(str(FahrenheitTemp)+"°F"+"  "+str(int(celciusTemp))+"°C")
            except Exception as error:
                tmsg.showerror("Error...",error)

            try:
                Day = time.strftime("%A")  ####  day
                DayVar.set(str(Day))

                CitiTime = time.strftime("%I:%M")
                CityNameTimeVar.set(str(PlaceName)+" "+str(CitiTime))
            except Exception as error:
                tmsg.showerror("Error...",error)
            
            if __name__=="__main__":
                async def WeatherCondition():   #########  weather condition
                    try:
                        ConditionWe = Weather.find("div", class_="condition-icon small-6 medium-12 columns")
                        return ConditionWe.text
                    except Exception as error:
                        tmsg.showerror("Error...",error)

                StatusVar.set(str(asyncio.run(WeatherCondition())))
            
            if __name__=="__main__":
                async def Pressure():   #############  pressure
                    try:
                        pressure =  Weather.find("span",class_="test-false wu-unit wu-unit-pressure ng-star-inserted")
                        return (pressure.text[:4]+" in")
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                PressureVar.set(asyncio.run(Pressure()))

            if __name__=="__main__":
                async def Clouds():       ##############  clouds
                    try:
                        clouds = Weather.find("span",class_="wx-value")
                        return clouds.text
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                CloudsVar.set(asyncio.run(Clouds()))

            if __name__=="__main__":
                async def Visibility():    ###########  visibility
                    try:
                        visibal = Weather.find("span",class_="test-false wu-unit wu-unit-distance ng-star-inserted")
                        return visibal.text[:2]+"miles"
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                VisibilityVar.set(asyncio.run(Visibility()))

            if __name__=="__main__":
                async def Humidity():    ###########  Humidity
                    try:
                        humidity = Weather.find("span",class_="test-false wu-unit wu-unit-humidity ng-star-inserted")
                        return (humidity.text[:3]+"%")
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                HumidityVar.set(asyncio.run(Humidity()))

            if __name__=="__main__":
                async def DewPoint():    ###########  dew point
                    try:
                        dewpoint = Weather.find("span",class_="test-false wu-unit wu-unit-temperature ng-star-inserted")
                        return (dewpoint.text[:3]+" F")
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                DewpointVar.set(asyncio.run(DewPoint()))

            if __name__=="__main__":
                async def Rainfall():    ###########  dew point
                    try:
                        rainfall = Weather.find("span",class_="test-false wu-unit wu-unit-rain ng-star-inserted")
                        return (rainfall.text[:4]+" in")
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                RainfallVar.set(asyncio.run(Rainfall()))

            if __name__=="__main__":
                async def SunRise():    ###########  Sun rise
                    try:
                        sunrise = SunMoon.find("span",class_="astro-data sunrise-icon")
                        return sunrise.text
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                SunRiseVar.set(str(asyncio.run(SunRise()))+" AM")

            if __name__=="__main__":
                async def SunSet():    ###########  Sun set
                    try:
                        sunset = SunMoon.find("span",class_="astro-data sunset-icon")
                        return sunset.text
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                SunsetVar.set(str(asyncio.run(SunSet()))+" PM")

            if __name__=="__main__":
                async def Moonrise():    ###########  moonrise
                    try:
                        moonrise = SunMoon.find("span",class_="astro-data moonset-icon")
                        return moonrise.text
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                MoonriseVar.set(str(asyncio.run(Moonrise()))+" PM")

            if __name__=="__main__":
                async def Moonset():    ###########  moon set
                    try:
                        moonset = SunMoon.find("span",class_="astro-data moonrise-icon")
                        return moonset.text
                    except Exception as error:
                        tmsg.showerror("error...",error)
                
                MoonsetVar.set(str(asyncio.run(Moonset()))+" AM")



#### first frame  input data entry box

FirstFrame = ctk.CTkFrame(
    master=root,
    fg_color='#d5def5',
    corner_radius=6,
)
FirstFrame.pack_propagate(False)
FirstFrame.configure(height=1000,width=45)
FirstFrame.pack(side=TOP,padx=6,pady=6,fill=BOTH)

####  weather city input

PlaceVar = StringVar()   ###  input variable

NameEntry = ttkb.Entry(
    master=FirstFrame,
    width=19,
    font=("carbel",16),
    bootstyle="info",
    foreground="#2f3c4f",
    background="green",
    textvariable=PlaceVar
)
NameEntry.grid(row=0,column=0,pady=9,padx=12)

######  button 
GettingDataBtn = ctk.CTkButton(
    master=FirstFrame,
    text="Get Report",
    font=("carbel",16),
    height=35,
    cursor="hand2",
    command=WeatherAppFunction
)
GettingDataBtn.grid(row=0,column=1,pady=9,padx=0)

#####  blank label
ctk.CTkLabel(
    master=FirstFrame,
    text="ㅤㅤㅤㅤㅤㅤㅤㅤ",
    bg_color='#d5def5',
    fg_color='#d5def5',
    text_color='#d5def5',
    
).grid(row=0,column=2,pady=9,padx=0)

#############   date day
DateLabel = ttkb.Label(
    master=FirstFrame,
    foreground="#152744",
    font=("ds-digital",14,"bold"),
    background='#d5def5'
)
DateLabel.grid(row=0,column=3,pady=9,padx=13)
DateDay()

#######  current time

CurrentTime = ttkb.Label(
    master=FirstFrame,
    foreground="#152744",
    font=("ds-digital",14,"bold"),
    background='#d5def5'
)
CurrentTime.grid(row=0,column=4,pady=9,padx=0)
CurrentTimeFunc()

##########  frame 2

SecondFrame = ttkb.Frame(master=root)
SecondFrame.pack(side=TOP,padx=6,pady=0,anchor=W,fill=BOTH)
SecondFrame.pack_propagate(False)

#### informaition of place heading label

DisplayInfo = ttkb.Label(
    master=SecondFrame,font=("carbel",19),
    text="Current Weather Report of",
    foreground="#152744"
    
)
DisplayInfo.grid(row=0,column=0,padx=3,pady=0)

CityNamevar = StringVar()

CityNameLabel = ttkb.Label(
    master=SecondFrame,font=("carbel",19),
    foreground="#ff8b00",textvariable=CityNamevar
)
CityNameLabel.grid(row=0,column=1,padx=3,pady=0)


######  temperature label main
CelciusVar = StringVar()
FeelsLikeVar = StringVar()
FeelsLikeTextvar = StringVar()

celciusLabel = ttkb.Label(
    master=root,
    textvariable=CelciusVar,   ########## celcius
    font=("ds-digital",55,"bold"),
    foreground="#152744"
)
celciusLabel.place(x=76,y=230)

FeelsLikeLabel = ttkb.Label(
    master=root,
    textvariable=FeelsLikeTextvar,
    font=("ds-digital",13),      ######  feels like
    foreground="#152744"
)
FeelsLikeLabel.place(x=360,y=240)

FeelsLikeTextLabel = ttkb.Label(
    master=root,
    textvariable=FeelsLikeVar,
    font=("ds-digital",13),      ######  feels like
    foreground="#ff8b00"
)
FeelsLikeTextLabel.place(x=465,y=240)

###########  getting day
DayVar = StringVar()

GetDay =  ttkb.Label(
    master=root,
    textvariable=DayVar,
    font=("ds-digital",13),      ######  feels like
    foreground="#152744"
)
GetDay.place(x=360,y=266)

#######  city name and Time
CityNameTimeVar = StringVar()

CityNameTime = ttkb.Label(
    master=root,
    textvariable=CityNameTimeVar,   
    font=("ds-digital",13),
    foreground="#152744"
)
CityNameTime.place(x=360,y=296)

########  weather status
StatusVar = StringVar()

WeatherStatus = ttkb.Label(
    master=root,
    textvariable=StatusVar,
    font=("ds-digital",33),
    foreground="#18224b"
)
WeatherStatus.place(x=76,y=330)


###############  third frame

ThirdFrame = ttkb.Frame(
    master=root,width=400,height=300,
)
ThirdFrame.pack(side=TOP,anchor=E,padx=26)
ThirdFrame.pack_propagate(False)
ThirdFrame.configure(width=400,height=300)


#####  temperature in celcius and fahrenheit
CelciusFahrenheitVar = StringVar()

Temperature = ttkb.Label(
    master=ThirdFrame,
    text="Temperature",   #@##########  temperature label
    font=("carbel",15),foreground="#18224b"
)
Temperature.grid(row=0,column=1,sticky=W,padx=9,pady=0)

GetTemperature = ttkb.Label(
    master=ThirdFrame,
    textvariable=CelciusFahrenheitVar,
    font=("carbel",15),foreground="#18224b"
)
GetTemperature.grid(row=0,column=0,padx=135,sticky=W)

#####################################################################################

Line1 = Label(
    master=root,
    text="―――――――――――――――――――――――――――――――"   #######  seperator 1
    ,foreground="#f7f7f7",
    background="#f7f7f7"
).place(x=630,y=151)

##########  pressure  ##########

PressureVar = StringVar()

PressureLab = ttkb.Label(
    master=ThirdFrame,
    text="Pressure",   #@##########  Pressure label
    font=("carbel",15),foreground="#18224b"
)
PressureLab.grid(column=1,row=1,sticky=E,padx=9,pady=16)

GetPressure = ttkb.Label(
    master=ThirdFrame,
    textvariable=PressureVar,
    font=("carbel",15),foreground="#18224b"
)
GetPressure.grid(row=1,column=0,padx=160,sticky=W)

######################################################################################

Line2 = Label(
    master=root,
    text="―――――――――――――――――――――――――――――――"   #######  seperator 2
    ,foreground="#f7f7f7",
    background="#f7f7f7"
).place(x=630,y=200)

############  clouds

CloudsVar = StringVar()

CloudsLab = ttkb.Label(
    master=ThirdFrame,
    text="Clouds",   #@##########  Clouds label
    font=("carbel",15),foreground="#18224b"
)
CloudsLab.grid(column=1,row=2,sticky=E,padx=9,pady=3)

GetClouds = ttkb.Label(
    master=ThirdFrame,
    textvariable=CloudsVar,
    font=("carbel",15),foreground="#18224b"
)
GetClouds.grid(row=2,column=0,padx=104)

#######################################################################################

Line3 = Label(
    master=root,
    text="―――――――――――――――――――――――――――――――"   #######  seperator 3
    ,foreground="#f7f7f7",
    background="#f7f7f7"
).place(x=630,y=249)

#############  visibility
VisibilityVar = StringVar()

VisibilityLab = ttkb.Label(
    master=ThirdFrame,
    text="Visibility",   #@##########  Visibility label
    font=("carbel",15),foreground="#18224b"
)
VisibilityLab.grid(column=1,row=3,sticky=E,padx=9,pady=16)

GetVisibility = ttkb.Label(
    master=ThirdFrame,
    textvariable=VisibilityVar,
    font=("carbel",15),foreground="#18224b"
)
GetVisibility.grid(row=3,column=0,padx=104)

#######################################################################################
HumidityVar = StringVar()

Line4 = Label(
    master=root,
    text="―――――――――――――――――――――――――――――――"   #######  seperator 4
    ,foreground="#f7f7f7",
    background="#f7f7f7"
).place(x=630,y=300)

##########  humidity
HumidityVar = StringVar()

HumidityLab = ttkb.Label(
    master=ThirdFrame,
    text="Humidity",   #@##########  Visibility label
    font=("carbel",15),foreground="#18224b"
)
HumidityLab.grid(column=1,row=4,sticky=E,padx=9,pady=4)
 
GetHumidity = ttkb.Label(
    master=ThirdFrame,
    textvariable=HumidityVar,
    font=("carbel",15),foreground="#18224b"
)
GetHumidity.grid(row=4,column=0,padx=104)

#######################################################################################3

Line5 = Label(
    master=root,
    text="―――――――――――――――――――――――――――――――"   #######  seperator 5
    ,foreground="#f7f7f7",
    background="#f7f7f7"
).place(x=630,y=357)

#####  dewpoint
DewpointVar = StringVar()

DewpointLab = ttkb.Label(
    master=ThirdFrame,
    text="Dew Point",   #@##########  Visibility label
    font=("carbel",15),foreground="#18224b"
)
DewpointLab.grid(column=1,row=5,sticky=E,padx=9,pady=17)

GetDewpoint = ttkb.Label(
    master=ThirdFrame,
    textvariable=DewpointVar,
    font=("carbel",15),foreground="#18224b"
)
GetDewpoint.grid(row=5,column=0,padx=104)

#####################################################################################

Line6 = Label(
    master=root,
    text="―――――――――――――――――――――――――――――――"   #######  seperator 5
    ,foreground="#f7f7f7",
    background="#f7f7f7"
).place(x=630,y=409)

############   rain fall
RainfallVar = StringVar()

RainfallLab = ttkb.Label(
    master=ThirdFrame,
    text="Rainfall",   #@##########  Visibility label
    font=("carbel",15),foreground="#18224b"
)
RainfallLab.grid(column=1,row=6,sticky=E,padx=9,pady=10)

GetRainfall = ttkb.Label(
    master=ThirdFrame,
    textvariable=RainfallVar,
    font=("carbel",15),foreground="#18224b"
)
GetRainfall.grid(row=6,column=0,padx=104)

#############################################################3

###########  styles

style1 = ttkb.Label(
    master=root,
    text="★",foreground="#352961",font=("arial",30)
).place(x=1000,y=500)


style2 = ttkb.Label(
    master=root,
    text="★",foreground="#de1b4a",font=("arial",26)
).place(x=950,y=530)

style3 = ttkb.Label(
    master=root,
    text="★",foreground="#367591",font=("arial",23)
).place(x=905,y=470)

FourthFrame = ctk.CTkFrame(
    master=root,width=580,height=76,fg_color='#ebebeb',corner_radius=56
).pack(side=BOTTOM,anchor=W,padx=26,pady=20)


#############  sun and moon

######  sun text

Sun = ttkb.Label(
    master=root,text="Sun",
    font=("ds-digital",17,"bold"),background="#ebebeb",
    foreground='#203e5f'
)
Sun.place(x=92,y=510)

SunLogo = ttkb.Label(
    master=root,text="☀️",background="#ebebeb",
    font=("arial",19),
    foreground="#f35e3e"
).place(x=149,y=510)

####################3  sun rise
SunRiseVar = StringVar()

SunriseLab = ttkb.Label(
    master=root,text="Rise ",font=("ds-digital",12),
    background="#ebebeb",foreground='#203e5f'
).place(x=96,y=545)

GetSunrise = ttkb.Label(
    master=root,textvariable=SunRiseVar,
    font=("ds-digital",12),background="#ebebeb",
    foreground="#111d5e"
).place(x=142,y=545)

###########  sun set
SunsetVar = StringVar()

SunsetLab = ttkb.Label(
    master=root,text="Set ",font=("ds-digital",12),
    background="#ebebeb",foreground='#203e5f'
).place(x=256,y=545)

GetSunset = ttkb.Label(
    master=root,
    textvariable=SunsetVar,
    font=("ds-digital",12),background="#ebebeb",
    foreground='#111d5e'
).place(x=293,y=545)

########### moon text

Moon = ttkb.Label(
    master=root,text="Moon",
    font=("ds-digital",17,"bold"),background="#ebebeb",
    foreground="#203e5f"
)
Moon.place(x=422,y=510)

MoonLogo = ttkb.Label(
    master=root,text="🌑",background="#ebebeb",
    font=("arial",16),
    foreground="#fdb44b"
).place(x=500,y=507)

###########  moon rise
MoonriseVar = StringVar()

MoonriseLab = ttkb.Label(
    master=root,text="Rise ",font=("ds-digital",12),
    background="#ebebeb",foreground='#203e5f'
).place(x=425,y=545)

Getmoonrise = ttkb.Label(
    master=root,
    textvariable=MoonriseVar,
    font=("ds-digital",12),background="#ebebeb",
    foreground='#111d5e'
).place(x=468,y=545)

###########
MoonsetVar = StringVar()

MoonsetLab = ttkb.Label(
    master=root,text="Set ",font=("ds-digital",12),
    background="#ebebeb",foreground='#203e5f'
).place(x=581,y=545) 

GetMoonset = ttkb.Label(
    master=root,
    textvariable=MoonsetVar,
    font=("ds-digital",12),background="#ebebeb",
    foreground='#111d5e'
).place(x=618,y=545)

####################################

DesigneAndCreated = ttkb.Label(
    master=root,
    text="Designed & Created by Nishant Maity",
    font=("ds-digital",9,'bold'),
    foreground='#111d5e'
).place(x=832,y=585)

WindowSize(Width=1120,Height=610)
root.title("day Forecaster ~ Nishant Maity")
root.mainloop()
