my_list = ["apple", "apple", "orange", "grape", "banana"]

#print(my_list[0])
#print(my_list[1])
#print(my_list[2])
#print(my_list[3])
#print(my_list[4])

is_there = "orange" in my_list
#print(is_there)

my_list.remove("apple")
my_list.append("blueberry")
my_list.insert(2, "raspberry")
my_list[1] = "starfruit"
#print(my_list)


my_list.insert(2, "dragonfruit")
#rint(len(my_list))

randomized = [False, "green", 15]
#print(randomized)

#EXTENDED LIST

pcolor = ['blue', 'red', 'yellow']
scolor = ['green','orange','violet']
tcolor = ['red-orange','blue-green','blue-violet']
tcolor2 = ['red-violet','red-green','blue-red']

colors = pcolor + scolor + tcolor
colors.extend(tcolor2)
#print(colors)

setA = {'pink', 'cyan', 'gold', 'orange', 'blue'}
setB = {'white', 'green', 'olive', 'gray', 'pink'}
setC = {'gold', 'violet', 'green', 'purple', 'brown'}

CunA = setC.union(setA)
CunB = setC.union(setB)

#print(CunA)
#print(CunB)

CintB = setC.intersection(setA)
CintA = setC.intersection(setB)

#print(CintB)
#print(CintA)

CdA = setC.difference(setA)
CdB = setC.difference(setB)

#print(CdA)
#print(CdB)

sinS = [setA, setB, setC]
#print(sinS)

tupleA = ("sin", "cos")
tupleB = ("tan", "cot")
tupleC = ("sec", "csc")

trigfunc = (
    (tupleA),
    (tupleB),
    (tupleC),
)
print(trigfunc[2][0]) #secant

my_pinfo = {
    "name": {
        "fname": "Red Colby",
        "lname": "Dumdum"
    },
    "age": 18,
    "gender": "male",
    "height": "dwarf",
    "favorite_word": "skibidi",
    "nicknames": [
        "Red",
        "Pula",
        "Mrutotman",
        "Utot",
        "Kupal",
    ]
}
my_pinfo["favorite_word"] ="tung tung sahur"
my_pinfo.update({"favorite course": "Classical Physics"})

print(my_pinfo["name"]["lname"])
print(my_pinfo["name"]["fname"])
print(my_pinfo["age"])
print(my_pinfo["gender"])
print(my_pinfo["height"])
print(my_pinfo["favorite_word"])
print(my_pinfo["nicknames"][2])




