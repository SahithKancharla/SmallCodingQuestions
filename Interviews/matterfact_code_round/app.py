import math as Math


stream = [100]
k = 5
# assumtpions q.pop() and q.push() as the standard for adding and deleteing elemnts in a array based queue
# assuming K in the number of elementss that I am tracking
# stream is a string of numbers as a array of numbers seperated by ,
def mean_varience(stream:str):
    for i in stream.split(","):
        q = []

        if len(q) == k:
            removed_elem = q.pop()
            sum -= removed_elem

        q.push(i)
        sum += i 
        mean = sum / len(q) 

        varience = 0
        for elem in q:
            varience += Math.sqr(mean - elem)/mean
    return mean, varience
    
# assumign that the input is JSON
def main(response):
    Body = JSON.jsonify(response).body
    latency = Body.latency

    mean, varience = mean_varience(latency)

    return JSON.parse("Mean:" mean, "varience:", varience)