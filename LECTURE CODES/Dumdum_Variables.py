from traceback import print_tb
import math
#FullName = "Red Colby S. Dumdum"
#intLength = len(strFullName)
#print(intLength)

#D =print(strFullName[13])
#u =print(strFullName[intLength - 5])
#m =print(strFullName[15])
#b =print(strFullName[7])

#strtatay = "Wala"

#strFullName = strtatay
#intLength = len(strtatay)
#print(strFullName)
#print(intLength)


#strNewVal = FullName.upper()
#print(strNewVal)
#strNewVal2 = FullName.lower()
#print  (strNewVal2)
#strNewVal3 = FullName.title()
#print(strNewVal3)
#strNewVal4 = FullName.capitalize()
#print(strNewVal4)
#strNewVal5 = FullName.count("m")
#print(strNewVal5)
#strNewVal6 = FullName.split()
#print(strNewVal6)
#strNewVal7 = FullName.startswith("R")
#print(strNewVal7)
#strNewVal8 = FullName.replace("Red", "Blue")
#print(strNewVal8)

#String Join
#FirstName = "Red Colby"
#LastName = "Dumdum"
#MiddleIn = "S."
#JoinedName = ", ".join((LastName, FirstName, MiddleIn))
#print(JoinedName)

#Substring
#DisplayName = "pneumonoultramicroscopicsilicovolcanoconiosis"

#sub1 = DisplayName[0:8]
#print(sub1)
#sub2 = DisplayName[8:24]
#print(sub2)
#sub3 = DisplayName[24:51]
#print(sub3)

#Index
#index1 = DisplayName.index("a")
#print(index1)
#index2 = DisplayName.index("o", 5, 30)
#print(index2)
#index3 = DisplayName.index("s", 25,)
#print(index3)

#DirtyStr = "R2131131313e13131113d341443 C31313131o23313l1313313b31132312y"
#NewStr = ""
#for char in DirtyStr:
#    if not char.isnumeric():
#        NewStr = NewStr + char

#print(NewStr)

#Integer/Numerical Variables

A = 25
B = 12.231441451531
C = 16
D = 1.23134124145535305848
E = 21j + 2
F = 32 + 5j

Sum = round(A + B, 2)
print(Sum)

Diff = round(C - D, 2)
print(Diff)

Product = round(A - D, 2)
print(Product)

Quotient = round(C / D, 2)
print(Quotient)

Cplx = E * F
print(Cplx)

Modulus = A % C
print(Modulus)

Modulus == A - int(A/C)*C
print (Modulus)

Angle = round(math.cos(math.radians(90)),1)
print(Angle)

Factorial = math.factorial(5)
print(Factorial)

if Sum >= Diff:#True
    print("I am so skibidi")
else:#False
    print("I am so sigma")

myVal = (((Sum % Diff)/Quotient)*Product) % (Product*Quotient+Diff)
print(myVal)

match myVal:
    case _ if myVal < 7:
        print("No")
    case _ if 7 >= myVal < 14:
        print("Yes")
    case _ if 14 >= myVal < 21:
        print("Yes")
    case _:
        print("Invalid")

#Logical Operator
a = 10
b = 5

op = (a == b)
print(op)
op2 = (a >= b)
print(op2)
op3 = (a <= b)
print(op3)
op4 = (a != b)
print(op4)
op5 = "02082007"
print(op5.isnumeric())

#Membership Operator
Manok = ["Meron", "Wala"]
Panalo = Manok[1]  # "Wala"
Sugal = input("Pumili ka ng manok (Meron o Wala): ")

if Sugal in Panalo:
    print("Panalo kana!")
else:
    print("Talo ka!")
