
import math
AMZN = [
    [129.479996,129.820007,133.270004,136.449997,126.82,128.550003,126.279999],
    [123.529999,124.660004,122.190002,118.540001,117.309998,113.779999,115.150002],
    [114.410004,118.010002,114.800003,113,115.879997,121.089996,120.949997],
    [120.300003,114.559998,113.669998,112.209999,112.900002,112.529999,106.900002],
    [113.790001,116.360001,115.07,115.25,119.32,119.82,120.599998],
    [115.660004,110.959999,103.410004,102.440002,96.790001,92.120003,89.300003],
    [90.980003,90.529999,89.980003,86.139999,96.629997,100.790001,98.489998,98.940002]
]


META = [
    [160.389999,162.059998,169.149994,168.960007,153.130005,151.470001,149.550003],
    [146.289993,148.020004,146.089996,142.119995,142.820007,140.410004,136.369995],
    [134.399994,141.610001,136.410004,135.679993,138.610001,140.279999,138.979996],
    [139.070007,133.449997,133.789993,128.539993,127.5,130.289993,126.760002],
    [134.039993,132.800003,133.229996,131.529999,130.009995,129.720001,137.509995],
    [129.820007,97.940002,99.199997,93.160004,95.199997,90.540001,88.910004],
    [90.790001,96.720001,96.470001,101.470001,111.870003,113.019997,114.220001,117.080002] 
]



#mean = sum_of_all_elements in the list / len(list)
#variance = sum_of_squared_differences / len()
#squared_difference = mean - each element **2
#standard deviation = square root of variance >>> sqrt(variance). 

def mean(some_list):
    return sum(some_list)/len(some_list)

def variance(some_list):
    total=0 #assign the total variable to 0
    for element in some_list: #iretate each element using a for loop. 
        total+= (mean(some_list)-element)**2 #squared_difference
    total= total / len(some_list) 
    return total 

def std_dev(some_list):
    return math.sqrt(variance(some_list))

#to print out the standard devs, mean and variance for each week
#for week in AMZN:
#print (std_dev(week))
#print (mean(week)) #if we wanted to print the mean
#print (variance(week)) #if we wanted to print the variance

#Print out all of the standard devs for each week in AMZN stock
weeks=0
for week in AMZN:
    weeks+=1
    print("AMZN", weeks, std_dev(week)) 
    

#Print out all of the standard devs for each week in META stock
weeks=0
for week in META:
    weeks+=1
    print("META", weeks, std_dev(week))