import numpy
import random
import names
import surnames
import set
   
def randpos(arr):
    return arr[int(numpy.floor(random.random()*(len(arr)-1)))]
   
def randcode(mlen, rlen):
    leng = mlen + numpy.floor(random.random()*rlen)
    res = ""
    while leng > 0:
        leng = leng-1
        res = res + randpos(set.data)
    print("code: ", res)
def randate(minage, curyear):
    year = minage+randpos(range(0,minage))
    month = month = 1+randpos(range(0,12))
    day = 0
    if month == 2:
        day = day = 1+randpos(range(0,28))
    elif month % 2 == 1:
        day = 1+randpos(range(0,31))
    else:
        day = 1+randpos(range(0,30))
    print("date: ", day, ".", month, ".", curyear-year)
def randnm():
    name = randpos(names.names)
    surname = randpos(surnames.surnames)
    print("Name: ", name, surname)
randcode(8, 4)
randate(20, 2023)
randnm()
 