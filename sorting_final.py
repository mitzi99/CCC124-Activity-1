'''Mitzi V. Dorato
    2018-5849
    BSCS 2
'''
import random
import time
import matplotlib.pyplot as plt

print("Insertion Sort")
startten = time.time()
tenlist = []
for i in range(0,10):
    t = random.randint(0,10)
    tenlist.append(t)
def insertion_tenth(ten):
    for index in range(1,len(ten)):
        current_element = ten[index]
        posten = index
        while current_element<ten[posten-1] and posten >0:
            ten[posten] = ten[posten-1]
            posten = posten-1
        ten[posten] = current_element

insertion_tenth(tenlist)
endten = time.time()
executionten = endten - startten
print('10 Integers Sorted')
print(tenlist)
print('Execution Time: ', executionten)
print("")

print("Insertion Sort")
starthundred = time.time()
hundredlist = []
for i in range(0,100):
    h = random.randint(0,100)
    hundredlist.append(h)
def insertion_hundred(hundred):
    for index in range(1,len(hundred)):
        current_element = hundred[index]
        poshundred = index
        while current_element<hundred[poshundred-1] and poshundred >0:
            hundred[poshundred] = hundred[poshundred-1]
            poshundred = poshundred-1
        hundred[poshundred] = current_element

insertion_hundred(hundredlist)
endhundred = time.time()
executionhundred = endhundred - starthundred
print("100 Integers Sorted")
print(hundredlist)
print('Execution Time: ', executionhundred)
print("")

print("Insertion Sort")
startthousand = time.time()
thousandlist = []
for i in range(0,1000):
    thousand = random.randint(0,1000)
    thousandlist.append(thousand)
def insertion_thousand(thousand):
    for index in range(1,len(thousand)):
        current_element = thousand[index]
        posthousand = index
        while current_element<thousand[posthousand-1] and posthousand >0:
            thousand[posthousand] = thousand[posthousand-1]
            posthousand = posthousand-1
        thousand[posthousand] = current_element

insertion_thousand(thousandlist)
endthousand = time.time()
executionthousand = endthousand - startthousand
print("1000 Integers Sorted")
print(thousandlist)
print('Execution Time: ', executionthousand)
print("")

print("Insertion Sort")
starttenk = time.time()
tenklist = []
for i in range(0,10000):
    tenk = random.randint(0,10000)
    tenklist.append(tenk)
def insertion_tenk(tenk):
    for index in range(1,len(tenk)):
        current_element = tenk[index]
        postenk = index
        while current_element<tenk[postenk-1] and postenk >0:
            tenk[postenk] = tenk[postenk-1]
            postenk = postenk-1
        tenk[postenk] = current_element

insertion_tenk(tenklist)
endtenk = time.time()
executiontenk = endtenk - starttenk
print("10000 Integers Sorted")
print(tenklist)
print('Execution Time: ', executiontenk)
print("")

#merge sort

print("Merge Sort")
starttimetm=time.time()
tmlist = []
for i in range(0,10):
    tm = random.randint(0,10)
    tmlist.append(tm)
def mergeSort(tmlist):
    if len(tmlist)>1:
        mid = len(tmlist)//2
        lefthalf = tmlist[:mid]
        righthalf = tmlist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                tmlist[k]=lefthalf[i]
                i=i+1
            else:
                tmlist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            tmlist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            tmlist[k]=righthalf[j]
            j=j+1
            k=k+1
mergeSort(tmlist)
endtimetm=time.time()
executionmergetm = endtimetm - starttimetm
print('10 Integers Sorted')
print(tmlist)
print('Execution Time: ', executionmergetm)
print("")


print("Merge Sort")
starttimehundredm=time.time()
hundredmlist = []
for i in range(0,100):
    hundredm = random.randint(0,100)
    hundredmlist.append(hundredm)
def mergeSorthundred(hundredmlist):
    #print("Splitting ",alist)
    if len(hundredmlist)>1:
        mid = len(hundredmlist)//2
        lefthalf = hundredmlist[:mid]
        righthalf = hundredmlist[mid:]
        mergeSorthundred(lefthalf)
        mergeSorthundred(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                hundredmlist[k]=lefthalf[i]
                i=i+1
            else:
                hundredmlist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            hundredmlist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            hundredmlist[k]=righthalf[j]
            j=j+1
            k=k+1
mergeSorthundred(hundredmlist)
endtimehundredm=time.time()
executionmergehundred = endtimehundredm - starttimehundredm
print('100 Integers Sorted')
print(hundredmlist)
print('Execution Time: ', endtimehundredm - starttimehundredm)
print("")

print("Merge Sort")
starttimethousandm=time.time()
thousandmlist = []
for i in range(0,1000):
    thousandm = random.randint(0,1000)
    thousandmlist.append(thousandm)
def mergeSortthousand(thousandmlist):
    if len(thousandmlist)>1:
        mid = len(thousandmlist)//2
        lefthalf = thousandmlist[:mid]
        righthalf = thousandmlist[mid:]
        mergeSortthousand(lefthalf)
        mergeSortthousand(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                thousandmlist[k]=lefthalf[i]
                i=i+1
            else:
                thousandmlist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            thousandmlist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            thousandmlist[k]=righthalf[j]
            j=j+1
            k=k+1
mergeSortthousand(thousandmlist)
endtimethousandm=time.time()
executionmergethousand = endtimethousandm - starttimethousandm
print('1000 Integers Sorted')
print(thousandmlist)
print('Execution Time: ', executionmergethousand)
print("")

print("Merge Sort")
starttimetenthousandm=time.time()
tenthousandmlist = []
for i in range(0,10000):
    tenthousandm = random.randint(0,10000)
    tenthousandmlist.append(tenthousandm)
def mergeSorttenthousand(tenthousandmlist):
    if len(tenthousandmlist)>1:
        mid = len(tenthousandmlist)//2
        lefthalf = tenthousandmlist[:mid]
        righthalf = tenthousandmlist[mid:]
        mergeSorttenthousand(lefthalf)
        mergeSorttenthousand(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                tenthousandmlist[k]=lefthalf[i]
                i=i+1
            else:
                tenthousandmlist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            tenthousandmlist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            tenthousandmlist[k]=righthalf[j]
            j=j+1
            k=k+1
mergeSorttenthousand(tenthousandmlist)
endtimetenthousandm=time.time()
executionmergetenthousand = endtimetenthousandm - starttimetenthousandm
print('10000 Integers Sorted')
print(tenthousandmlist)
print('Execution Time: ', executionmergetenthousand)
print("")

x1 = [1,2,3,4]
y1 = [executionten, executionhundred, executionthousand, executiontenk]
plt.plot(x1, y1, label="Insertion Sort")

x2 = [1,2,3,4]
y2 = [executionmergetm, executionmergehundred, executionmergethousand, executionmergetenthousand]
plt.plot(x2, y2, label="Merge Sort")

plt.xlabel('x - axis / Integers')
plt.ylabel('y - axis / Time in seconds')
plt.title('lines in the graph')
plt.legend()
plt.show()
