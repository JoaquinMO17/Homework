#First we import the random library to create the main set
import random
#We declare the main set as a set of 1000 random integers from -100 and 100, then we declare the 3 subsets we'll use and the sum variables to compare
mainset = [random.randint(-100, 100) for _ in range(100)]
lastsubset = []
greatestsubset = []
negativesubset = []
sumay = 0
sumaz = 0
#We print the main set to check if our code works
print(mainset)
#Now we iterate for each item on our main set and append the positive values to our lastsubset, the negative values are ignored and every time one appears, we compare our lastsubset with our greatestsubset
#If the lastsubset is greater, it replaces the greatestsubset
#When we find a negative value, the lastsubset is deleted, except in the case that we find more than 1 negative value in a row, we don't compare again
for i in range(len(mainset)):
    if mainset[i] >= 0:
      lastsubset.append(mainset[i])
      sumay = sum(lastsubset)
      del negativesubset[:]
    elif mainset[i] < 0:
       negativesubset.append(mainset[i])
       if len(negativesubset) > 1:
         continue
       if sumay > sumaz:
         greatestsubset = lastsubset.copy()
         sumaz = sum(greatestsubset) 
       del lastsubset[:] 
#Finally, we print our results
print(greatestsubset)
print(sum(greatestsubset))
