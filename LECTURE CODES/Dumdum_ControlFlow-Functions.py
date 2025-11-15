'''
AssessmentL = ("Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","PF")

def myGrade():
        grades = {}  # lagayan ng grades
        AssIn = 0
        while True:
            while AssIn < len(AssessmentL):
                Assessment = AssessmentL[AssIn]
                myChoice = input(f"Grade mo sa {Assessment}: ")
                try:
                    myGradeVal = float(myChoice)
                    if myGradeVal >= 0 and myGradeVal <= 100:
                        grades[Assessment] = myGradeVal
                        AssIn += 1
                    else:
                        print("Invalid Stupid")

                except ValueError:
                    print(f"Invalid input for {Assessment}. Please enter a number.")



            if grades:  # calculate only if there are grades
                grade = sum(grades.values()) / len(grades)
                print("\nAll grades:")

                for Ass, Grd in grades.items():
                    print(f"{Ass}: {Grd}")

                print(f"\nYour transmuted/final grade is: {round(grade,3)}")

                return grade  # return the grade

while True:
    grade = myGrade()
    if grade >= 97 and grade <= 100:
        print("plat uno 1.0 OMG")
    elif grade >= 94 and grade < 97:
        print("wantupayp 1.25 OMG")
    elif grade >= 91 and grade < 94:
        print("wampipti")
    elif grade >= 88 and grade < 91:
        print("1.75*_*")
    elif grade >= 85 and grade < 88:
        print("dos")
    elif grade >= 82 and grade < 85:
        print("dos25")
    elif grade >= 79 and grade < 82:
        print("dos50")
    elif grade >= 76 and grade < 79:
        print("dos75")
    elif grade >= 75 and grade < 76:
        print("tres")
    elif grade >= 65 and grade < 75:
        print("fail")
    else:
        print("INC, W, or D")
'''
'''
OriginalVal = "RacecaR"
print("original value: " + OriginalVal)
newVal = ""

for x in OriginalVal:
    newVal = x + newVal

print("new value : " + newVal)

myString = "Pneumonoultramicroscopicsilicovolcanoconiosis"
for char in myString:
    print(char.upper())

print("After Loop")


for i in range(10):
    if i % 2 == 0:
        print("Even Number : " + str(i))
        continue
    if i > 6:
        print("i is greater than 7")
        break

print("i value now is : " + str(i))
print("after loop")
'''
'''
import time

isConnected = "No"

for retry in range(4):
    print(f"Retry: {retry + 1}")
    time.sleep(2)  # 2 seconds delay
    isConnected = input("Is connected? (Yes/No): ")

    if isConnected == "Yes":
        print("Now Connected")
        break
    else:
        print("Request timed out.")
        print("Processing your request . . .")
'''
'''
charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#',
            '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
            ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{',
            '|', '}', '~', ' ']

# SIMPLE ENCRYPTION
myInput = 'r'
output = ''
key = (5%3)*2

for letter in myInput:
    indexCounter = charList.index(letter)
    output += charList[(indexCounter + key) % len(charList)]

print(output)
'''
'''
def area(shape, x, y = 0):
   if shape == "triangle":
       return 0.5 * x * y
   elif shape == "square":
       return x * x
   elif shape == "circle":
       return 3.1416 * x ** 2
   elif shape == "cylinder":
       return (2 * 3.1416 * x * y) + (2 * 3.1416 * x ** 2)
   elif shape == "sphere":
       return 4 * 3.1416 * x ** 2
   else:
       return 0

x = 5
y = 3

#print(area("square",x,y))


import time

def countdown (num):
    if num == "odd":
        for i in range (0, 20, +1):
            time.sleep(0.5)
            print(2*i + 1)
    elif num == "even":
        for i in range (0, 20, +1):
            time.sleep(0.5)
            print(2*i)
    else:
        for i in range(0, 20, +1):
            time.sleep(0.5)
            print(i)

countdown("even")
'''