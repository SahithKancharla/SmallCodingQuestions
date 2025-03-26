import math as Math




sum = 0
q = []
mean_timeseries = []
varience_timeseries = [] 
# assumtpions q.pop() and q.push() as the standard for adding and deleteing elemnts in a array based queue
# assuming K in the number of elementss that I am tracking
# stream is a string of numbers as a array of numbers seperated by ,
def mean_varience(stream:int):

    if len(q) == k:
        removed_elem = q.pop()
        sum -= removed_elem
    
    q.push(i)
    sum += i 
    mean = sum / len(q)

    varience = 0
    for elem in q:
        varience += Math.sqr(elem - mean)/ len(q)
    
    mean_timeseries.append(mean)
    varience_timeseries.append(varience)

    
    
# assumign that the input is JSON
def main(response):
    Body = JSON.jsonify(response).body
    latency = Body.latency
    mean_varience(latency)

    return JSON.parse("Mean:" mean_timeseries, "varience:", varience_timeseries)