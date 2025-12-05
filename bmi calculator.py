#Author: Chloe Gerhardson
#Body Mass Index Calculator


#Welcome user

print("Welcome to Chloe's BMI Calculator" + "\n")

#Declare constants for conversions

INCHES_TO_METER = 39.36
POUNDS_TO_KILO = 2.2

#Ask user for name, and get inputs of weight and height
#Convert numerical inputs to metric values

sName=input("Name of person we are calculating the BMI for:")
iHeightInMeters=int(input("Supply Height in Inches:"))/INCHES_TO_METER
iWeightInKilograms=int(input("Supply Weight in Pounds:"))/POUNDS_TO_KILO

#Calculate BMI
fBodyMassIndex = iWeightInKilograms / (iHeightInMeters * iHeightInMeters)

print(sName, "'s BMI is:", format(fBodyMassIndex,".2f"))

#Determine BMI Finding

sFinding = "Underweight" if fBodyMassIndex <= 18.50 else "Normal" if fBodyMassIndex <= 24.90 \
           else "Overweight" if fBodyMassIndex <= 29.90 else "Obese"

print("BMI finding is the subject is: ", sFinding)
