import names
import surnames
import numpy
import sys
class weight:
    def __init__(self, weight, letter):
        self.letter = letter
        self.weight = weight
 
def edit(ar, letter):
    for x in ar:
        if x.letter == letter:
             x.weight = x.weight + 1
             return ar
    if (letter != "'") and (letter != "-"):
        ar.append(weight(1, letter))
    return ar
   
def balance():
    weights = [weight(0, "a")]
    print("calculating..")
    arg = sys.argv
    data = names.names if (not len(arg)) else surnames.surnames
    for j in data:
       for i in j:
           weights = edit(weights, i)
    print("compressing..")
    mn = weights[0].weight
    for x in weights:
        if x.weight < mn:
            mn = x.weight
    res = ""
    print("writing file (set.py)..")
    for x in weights:
        res = res + x.letter*int(numpy.floor(x.weight/mn))
    file = open("set.py", "w")
    file.write("data = '" + res + "'")
    print("Ready " + str(len(res)) + " characters.")
balance()
    