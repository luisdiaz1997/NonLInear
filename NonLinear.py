import math
data = open("Data.txt")     #read data, first column must include time, second voltage
time = list()
voltage = list()
modelList = list()
V= 2.009                    #input maximum voltage, start from V - 0.1
b= 442.825              #any arbitrary value, keep replacing for better accuracy
w= 42334                #any arbitrary value, keep replacing for better accuracy
phi = 0
bestFit = 100           #the best fit should be as close to zero as possible
intervalV = 0.0001        #you want to keep changing the three values at different rates
intervalB= 0.0001
intervalW= 0.01
bestValues= [0,0,0,0,0] #best values will be stored here
originalW= w            
originalB= b

for line in data:
    set = line.split()
    time.append(float(set[0]))
    voltage.append(float(set[1]))   #sets arrays
def model(t, V, b, w, phi):     
    expo = math.exp((-b)*t)
    cos = math.cos((w*t)+phi)       
    return (V*expo*cos)             #returns the value
    
def squaredDev(a,b):                
    return (a-b)**2                #makes squared deviation

def sumDev():                       #adds all the deviations
    sum = 0
    current = 0
    for t in time:
        sum += squaredDev(voltage[current],modelList[current])
        current +=1
    return sum

def fillValues():                   #fills the values of the formula into an array
    for t in time:
        value = model(t, V, b, w, phi)
        modelList.append(value)

def better(x):                  #tests whether the new fit is better than the current one
    if x < bestFit:
        return True
    else:
        return False       
for z in range(10):             #you can modify the ranges at wish

        for _ in range(100):
            
            for _ in range(100):    
                
                    fillValues()
                    fit = sumDev()
                    if (better(fit)):
                        bestFit = fit
                        bestValues = [V, b, w, phi,fit]
                    modelList = list()
                    #print V, b, w, phi, fit
                    w += intervalW
            w= originalW
            b += intervalB
        b = originalB
        V += intervalV
    

print bestValues
print "Best fit so far"