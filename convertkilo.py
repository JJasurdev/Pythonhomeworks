import math

def convert_kilo():
    kilometers = float(input("Enter the distance in kilometers: ")) 
    miles = kilometers * 0.621371  
    print("The distance is", miles, "miles.")

def convert_meters():
    meters = float(input("Enter the distance in meters: "))  
    kilometers = meters / 1000  
    print("The distance is", kilometers, "kilometers.")
            
def convert_centimeters():
    centimeters = float(input("Enter the distance in centimeters: "))  
    inches = centimeters / 2.54
    print("The distance is", inches, "inches.")
           
