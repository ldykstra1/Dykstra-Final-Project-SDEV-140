"""

Author:  Lisa Dykstra
Date written: 07/23/2024
Assignment:   Module#08 Final Project
Short Desc:   This program provides a GUI interface
              for converting various units from Standard 
              to metric and vice versa. It includes 2 
              windows and 4 images.

"""

#Import everything from tkinter
from tkinter import *

#import PIL
from PIL import Image, ImageTk
#Everything is a widget; create the root widget
root = Tk()
#Write a title
root.title("Conversions Made Easy")
#choose a size based on size of background image
root.geometry("663x601")

#add an image to the background
#Define image for the background
compiled_image = PhotoImage(file = "compiled_images_3.png")
#create a label for the image
background_image_label = Label(root, image=compiled_image)
#the image can be placed using label
background_image_label.place(x=0, y=0, relwidth=1, relheight=1)

#create a label widget on root windwo
firstQuestion = Label(root, font = "Helvetica", fg = "#F2F5FB", bg = '#022B73', text="          Select the type of measurement that you would like to convert:         ")
#place the label on the frame
firstQuestion.grid(row=0, column=0)

#create a function to open Temperature window, which contains labels, entry fields, and buttons
def open_TempWindow():
    #create global variables for temperature input so they can be used in another function
    global enterFahrenheit
    global enterCelsius
    #make a new window
    top1 = Toplevel()
    #window=Toplevel(top)
    top1.geometry("400x200")
    top1.title("Temperature Conversion")
    #create labels, entry boxes, and buttons in Temp window
    FahrenheitLabel = Label(top1, text="Fahrenheit")
    CelsiusLabel = Label(top1, text="Celsius")
    enterFahrenheit = Entry(top1, width = 20)
    enterCelsius = Entry(top1, width = 20)
    convertToCelsius_button = Button(top1, text= "Convert >>>", command = convertToCelsius, fg = "green")
    convertToFahrenheit_button = Button(top1, text= "<<< Convert", command = convertToFahrenheit, fg = "green")
    #place the labels, entry boxes, and buttons to the Temp window
    FahrenheitLabel.grid(row=1, column=1)
    CelsiusLabel.grid(row=1, column=2)
    enterFahrenheit.grid(row=2, column=1)
    enterCelsius.grid(row=2, column=2)
    convertToCelsius_button.grid(row=3, column=1)
    convertToFahrenheit_button.grid(row=3, column=2)
    
#Define the function to convert from Celsius to Fahrenheit
#add validation feature to ensure correct data type is entered
def convertToFahrenheit():
    if enterCelsius.get().isdigit() == False or enterCelsius == "null":
        #make a new window for the error message to print
        top5 = Toplevel()
        top5.geometry("200x50")
        top5.title("Warning")
        warningLabel = Label(top5, text ="Please enter a number")
        warningLabel.grid(row=0, column=0)
    else:
        #Inputs the temp in Celsius, computes the equivalent Fahrenheit temp
        #define variables to use in the conversion
        numCelsius = float(enterCelsius.get())
        result = (9/5)*numCelsius + 32
        result = float(result)
        enterFahrenheit.insert(0, f'{result:.2f}')

#Define the function to convert from Fahrenheit to Celsius
#add validation feature to ensure correct data type is entered
def convertToCelsius():
    if enterFahrenheit.get().isdigit() == False or enterFahrenheit == "null":
        #use new pop-up window for error message
        top5 = Toplevel()
        top5.geometry("200x50")
        top5.title("Warning")
        warningLabel = Label(top5, text ="Please enter a number")
        warningLabel.grid(row=0, column=0)
    else:
        #input number for Fahrenheit, convert and display Celsius
        #create a variable to do the conversion
        numFahrenheit = float(enterFahrenheit.get())
        result = (numFahrenheit - 32)*5/9
        result = float(result)
        enterCelsius.insert(0, f'{result:.2f}')

#create a function to open Length 1 window, which contains labels, entry fields, and buttons
def open_Length1Window():
    #create variables to use in the conversion function as well as this function
    global enterInches
    global enterCentimeters
    top2 = Toplevel()
    #window=Toplevel(top)
    top2.geometry("400x200")
    top2.title("Length Conversion")
    #create labels, entryboxes, and buttons for inches and centimeters
    inchesLabel = Label(top2, text="Inches")
    centimetersLabel = Label(top2, text="Centimeters")
    enterInches = Entry(top2, width = 20)
    enterCentimeters = Entry(top2, width = 20)
    convertToCentimeters_button = Button(top2, fg = "green", command = convertToCentimeters, text= "Convert  >>>")
    convertToInches_button = Button(top2, fg = "green", command = convertToInches, text= "<<<  Convert") 
    #place the labels, entryboxes, and buttons on the frame
    inchesLabel.grid(row=3, column=0)
    centimetersLabel.grid(row=3, column=1)
    enterInches.grid(row=4, column=0)
    enterCentimeters.grid(row=4, column=1)
    convertToCentimeters_button.grid(row=5, column=0)
    convertToInches_button.grid(row=5, column=1)

#Define the function to convert from inches to centimeters
#add validation feature to ensure correct data type is entered
def convertToCentimeters():
    if enterInches.get().isdigit() == False or enterInches == "null":
        #create new pop up window for error message
        top5 = Toplevel()
        top5.geometry("200x50")
        top5.title("Warning")
        warningLabel = Label(top5, text ="Please enter a number")
        warningLabel.grid(row=0, column=0)
    else:
        #Inputs the length in inches, computes the equivalent centimeters length
        numInches = float(enterInches.get())
        result = numInches*2.54
        enterCentimeters.insert(0, f'{result:.2f}')

#Define the function to convert from centimeters to inches
#add validation feature to ensure correct data type is entered
def convertToInches():
    if enterCentimeters.get().isdigit() == False or enterCentimeters == "null":
        #create new pop up window for error message
        top5 = Toplevel()
        top5.geometry("200x50")
        top5.title("Warning")
        warningLabel = Label(top5, text ="Please enter a number")
        warningLabel.grid(row=0, column=0)
    else:
        #Input in centimeters is converted to inches and displayed
        #variables used in calculation
        numCentimeters = float(enterCentimeters.get())
        result = (numCentimeters)/2.54
        enterInches.insert(0, f'{result:.2f}')

#create a function to open Length 2 window, which contains labels, entry fields, and buttons
def open_Length2Window():
    global enterMiles
    global enterKilometers
    top3 = Toplevel()
    #window=Toplevel(top)
    top3.geometry("400x200")
    top3.title("Long Distance Conversion")
    #create labels, entryboxes, and buttons for miles and kilometers
    milesLabel = Label(top3, text="Miles")
    kilometersLabel = Label(top3, text="Kilometers")
    enterMiles = Entry(top3, width = 20)
    enterKilometers = Entry(top3, width = 20)
    convertToKilometers_button = Button(top3,fg = "green", command = convertToKilometers, text= "Convert >>>")
    convertToMiles_button = Button(top3, fg = "green", command = convertToMiles, text= "<<< Convert")
    #place the labels, entryboxes, and buttons on the frame
    milesLabel.grid(row=3, column=0)
    kilometersLabel.grid(row=3, column=1)
    enterMiles.grid(row=4, column=0)
    enterKilometers.grid(row=4, column=1)
    convertToKilometers_button.grid(row=5, column=0)
    convertToMiles_button.grid(row=5, column=1)

#Define the function to convert from miles to kilometers
#add validation feature to ensure correct data type is entered
def convertToKilometers():
    if enterMiles.get().isdigit() == False or enterMiles == "null":
        #create new pop up window for error message
        top5 = Toplevel()
        top5.geometry("200x50")
        top5.title("Warning")
        warningLabel = Label(top5, text ="Please enter a number")
        warningLabel.grid(row=0, column=0)
    else:
        #Inputs the length in miles, computes the equivalent kilometers distance
        #variables used in calculation
        numMiles = float(enterMiles.get())
        result = numMiles*1.61
        enterKilometers.insert(0, f'{result:.2f}')

#Define the function to convert from centimeters to inches
#add validation feature to ensure correct data type is entered
def convertToMiles():
    if enterKilometers.get().isdigit() == False or enterKilometers == "null":
        #create new pop up window for error message
        top5 = Toplevel()
        top5.geometry("200x50")
        top5.title("Warning")
        warningLabel = Label(top5, text ="Please enter a number")
        warningLabel.grid(row=0, column=0)
    else:
        #input kilometers and convert to miles
        numKilometers = float(enterKilometers.get())
        result = (numKilometers)/1.61
        enterMiles.insert(0, f'{result:.2f}')

#create a function to open Weight window, which contains labels, entry fields, and buttons
def open_WeightWindow():
    #create variables to for the input in this window and they will also be used in the calculation function below
    global enterPounds
    global enterKilograms
    top4 = Toplevel()
    #window=Toplevel(top)
    top4.geometry("400x200")
    top4.title("Weight Conversion")
    #create labels, entry boxes, and buttons in Temp window
    PoundsLabel = Label(top4, text="Pounds (lb)")
    KilogramsLabel = Label(top4, text="Kilograms")
    enterPounds = Entry(top4, width = 20)
    enterKilograms = Entry(top4, width = 20)
    convertToKilograms_button = Button(top4, text= "Convert >>>", command = convertToKilograms, fg = "green")
    convertToPounds_button = Button(top4, text= "<<< Convert", command = convertToPounds, fg = "green")
    #place the labels, entry boxes, and buttons to the Temp window
    PoundsLabel.grid(row=1, column=1)
    KilogramsLabel.grid(row=1, column=2)
    enterPounds.grid(row=2, column=1)
    enterKilograms.grid(row=2, column=2)
    convertToKilograms_button.grid(row=3, column=1)
    convertToPounds_button.grid(row=3, column=2)

#Define the function to convert from pounds to kilograms
#add validation feature to ensure correct data type is entered
def convertToKilograms():
    if enterPounds.get().isdigit() == False or enterPounds == "null":
        #create new pop up window for error message
        top5 = Toplevel()
        top5.geometry("200x50")
        top5.title("Warning")
        warningLabel = Label(top5, text ="Please enter a number")
        warningLabel.grid(row=0, column=0)
    else:
        #Inputs the weight in pounds, computes the equivalent weight in kilograms
        #variables created for calculation
        numPounds = float(enterPounds.get())
        result = numPounds/2.2046
        enterKilograms.insert(0, f'{result:.2f}')
    
#Define the function to convert from kilograms to pounds
#add validation feature to ensure correct data type is entered
def convertToPounds():
    if enterKilograms.get().isdigit() == False or enterPounds == "null":
        #create new pop up window for error message
        top5 = Toplevel()
        top5.geometry("200x50")
        top5.title("Warning")
        warningLabel = Label(top5, text ="Please enter a number")
        warningLabel.grid(row=0, column=0)
    else:
        #Inputs the weight in kilograms, computes the equivalent weight in pounds
        #variables used in calculation
        numKilograms = float(enterKilograms.get())
        result = (numKilograms)*2.2046
        enterPounds.insert(0, f'{result:.2f}')

#create buttons for root window
#create a buttons for Temperature, length1, length 2, weight, and exit
temperature_button = Button(root, text= "Temperature", command = open_TempWindow, font = "Helvetica", fg = "#F2F5FB", bg = '#022B73',padx= 40, pady=15)
length1_button = Button(root, text= "Length (inches and centimeters)", font = "Helvetica", fg = "#F2F5FB", bg = '#022B73', command = open_Length1Window,padx= 40, pady=15)
length2_button = Button(root, text= "Length (miles and kilometers)",  font = "Helvetica",fg = "#F2F5FB", bg = '#022B73', command = open_Length2Window,padx= 40, pady=15)
weight_button = Button(root, text= "Weight", fg = "#F2F5FB",  font = "Helvetica",bg = '#022B73', command = open_WeightWindow,padx= 40, pady=15)
exit_button = Button(root, text = "Exit Program", font = "Helvetica", fg = "#F2F5FB", bg = '#022B73', command =root.quit,padx= 40, pady=15)

#Put the buttons on the screen
temperature_button.grid(row=5, column=0, pady=20)
length1_button.grid(row=6, column=0, pady=20)
length2_button.grid(row=7, column=0, pady=20)
weight_button.grid(row=8, column=0, pady=20)
exit_button.grid(row=9, column=0, pady=20)

#Create an event loop; a program is continually looping
root.mainloop()