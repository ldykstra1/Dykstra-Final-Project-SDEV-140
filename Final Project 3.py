"""

Author:  Lisa Dykstra
Date written: 07/23/2024
Assignment:   Module#08 Final Project
Short Desc:   This program provides a GUI interface
              for converting various units from Standard 
              to metric and vice versa. It includes 2 
              windows and 4 images.

"""
from tkinter import*

#create window
mainWindow = Tk()

#frame1: define a function and give it arguments
frame1 = LabelFrame(mainWindow, text = "Conversions Made Easy", padx = 10, pady= 10)

#add frame to the window; the arguments are where on the frame you're going to put it
frame1.grid(row = 0, column = 0, rowspan=10, columnspan=10)

#create a label widget
firstQuestion = Label(frame1, text="Select the type of measurement that you would like to convert:")
#place the label on the frame
firstQuestion.grid(row=2, column=0)

#create buttons for frame 1
#create a buttons for Temperature, length1, length 2, and weight
temperature_button = Button(frame1, text= "Temperature")
length1_button = Button(frame1, text= "Length (inches and centimeters)")
length2_button = Button(frame1, text= "Length (miles and kilometers)")
weight_button = Button(frame1, text= "Weight")

#place the button on frame1
temperature_button.grid(row=3, column=0)
length1_button.grid(row=5, column=0)
length2_button.grid(row=7, column=0)
weight_button.grid(row=9, column=0)

#This is for the temperature on frame 2
#define a function and give it arguments
frame2 = LabelFrame(mainWindow, text = "Temperature Conversion", padx = 10, pady= 10)
#add frame to the window; the arguments are where on the frame you're going to put it
frame2.grid(row = 0, column = 25, rowspan=10, columnspan=10)

#Define the function to convert from Celsius to Fahrenheit
def convertToFahrenheit():
#Inputs the temp in Celsius, computes the equivalent Fahrenheit temp
    numCelsius = enterCelsius.getNumber()
    result = (9/5)*numCelsius + 32
    enterFahrenheit.setNumber(result)
#Define the function to convert from Fahrenheit to Celsius
def convertToCelsius():
    numFahrenheit = enterFahrenheit.getNumber()
    result = (numFahrenheit - 32)*5/9
    enterCelsius.setNumber(result)

#create labels, entry boxes, and buttons for Fahrenheit and Celsius
FahrenheitLabel = Label(frame2, text="Fahrenheit")
CelsiusLabel = Label(frame2, text="Celsius")
enterFahrenheit = Entry(frame2, width = 20)
enterCelsius = Entry(frame2, width = 20)
convertToCelsius_button = Button(frame2, text= "Convert >>>", command = convertToCelsius, fg = "green")
convertToFahrenheit_button = Button(frame2, text= "<<< Convert", command = convertToFahrenheit, fg = "green")

#place the labels, entry boxes, and buttons on the frame
FahrenheitLabel.grid(row=3, column=0)
CelsiusLabel.grid(row=3, column=1)
enterFahrenheit.grid(row=4, column=0)
enterCelsius.grid(row=4, column=1)
convertToCelsius_button.grid(row=5, column=0)
convertToFahrenheit_button.grid(row=5, column=1)


#This is for the length(inches to centimeters) frame 3
#define a function and give it arguments
frame3 = LabelFrame(mainWindow, text = "Length Conversion", padx = 10, pady= 10)
#add frame to the window; the arguments are where on the frame you're going to put it
frame3.grid(row = 25, column = 0, rowspan=10, columnspan=10)

#create labels, entryboxes, and buttons for inches and centimeters
inchesLabel = Label(frame3, text="Inches")
centimetersLabel = Label(frame3, text="Centimeters")
enterInches = Entry(frame3, width = 20)
enterCentimeters = Entry(frame3, width = 20)
convertToCentimeters_button = Button(frame3, fg = "green", text= "Convert  >>>")
convertToInches_button = Button(frame3, fg = "green", text= "<<<  Convert") 

#place the labels, entryboxes, and buttons on the frame
inchesLabel.grid(row=3, column=0)
centimetersLabel.grid(row=3, column=1)
enterInches.grid(row=4, column=0)
enterCentimeters.grid(row=4, column=1)
convertToCentimeters_button.grid(row=5, column=0)
convertToInches_button.grid(row=5, column=1)

#This is for the length(miles to kilometers) on frame 4
#define a function and give it arguments
frame4 = LabelFrame(mainWindow, text = "Long Distance Conversion", padx = 10, pady= 10)
#add frame to the window; the arguments are where on the frame you're going to put it
frame4.grid(row = 25, column = 25, rowspan=10, columnspan=10)

#create labels, entryboxes, and buttons for miles and kilometers
milesLabel = Label(frame4, text="Miles")
kilometersLabel = Label(frame4, text="Kilometers")
enterMiles = Entry(frame4, width = 20)
enterKilometers = Entry(frame4, width = 20)
convertToKilometers_button = Button(frame4,fg = "green", text= "Convert >>>")
convertToMiles_button = Button(frame4, fg = "green", text= "<<< Convert")

#place the labels, entryboxes, and buttons on the frame
milesLabel.grid(row=3, column=0)
kilometersLabel.grid(row=3, column=1)
enterMiles.grid(row=4, column=0)
enterKilometers.grid(row=4, column=1)
convertToKilometers_button.grid(row=5, column=0)
convertToMiles_button.grid(row=5, column=1)







mainWindow.mainloop()