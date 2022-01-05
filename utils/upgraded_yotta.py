#!/usr/bin/python3

import numpy as np
import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

# Floor division to check how many times we can put in linear yotta scale
def yotta_check(ticketNum, yottaNum = 63):
    yottaMultiples = ticketNum // yottaNum
    yottaRemainder = ticketNum % yottaNum
    return yottaMultiples, yottaRemainder

# generate overall ticket and check for tickets
def overall_ticket_generator(non_yotta):
    overall_ticket = np.random.randint(1, non_yotta+1, 6)
    # outputs is unique elements in array only
    overall_ticket = np.unique(overall_ticket)
    # print(overall_ticket)
    # print(len(overall_ticket))
    #reject non unique configurations
    if len(overall_ticket) != 6:
        return overall_ticket_generator(non_yotta)
    elif np.size(overall_ticket) == 6 and type(overall_ticket) != None:
        # print("Generator value " + str(overall_ticket))
        # print(f"Generated size {np.size(overall_ticket)}")
        # receiving good unique tickets
        return overall_ticket
    
    return overall_ticket_generator(non_yotta)


    
def ticket_generator(yottaMultiples, yottaRemainder, ticketNumber):
    print("Generating sequential yotta numbers ... ")
    yottaNums = []
    i = 1
    # largest yotta_number
    yotta_top = 63
    # smallest non yotta number
    non_yotta = 70
    # generating numbers with incremental yotta nums
    while i <= yottaMultiples:
        for j in range(0, yotta_top):
            print(f"Index Number: {j}")
            outputTicket = overall_ticket_generator(non_yotta)
            #print(f"Array: {outputTicket}")
            #print(f"Size After Return: {len(outputTicket)}")
            outputTicket = np.append(outputTicket,j+1)
            yottaNums.append(outputTicket)
            
            print(f"Output: {outputTicket}")
        
        #incrementing i
        i = i + 1
    print("Completed generating sequential yotta numbers")
    print("Generating non-sequential yotta numbers ... ")
    # looping through the remainder
    for i in range(0, yottaRemainder):
        ticket = overall_ticket_generator(non_yotta)
        yottaValue = np.random.randint(1, yotta_top, 1, dtype = int)
        ticket = np.append(ticket, yottaValue)
        print(ticket)
        yottaNums.append(ticket)


    print("Completed generating non-sequential yotta numbers")
    lenArray = len(yottaNums)
    print(f"Generated {lenArray} tickets of {ticketNumber}")

    return yottaNums

# csv export
def export(yottaNums, filename = "yottanums.csv"):
    with open(filename, 'w+', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        writer.writerow(["1", "2", "3", "4", "5", "6", "Yotta"])
        #print_yottas(yottaNums)
        for i in yottaNums:
            writer.writerow([i[0], i[1], i[2], i[3],i[4], i[5], i[6]])

def print_yottas(yottaNums):
    for i in yottaNums:
        print(i)

def histogram_generator(yottaNums):
    histogramVals = []
    for i in yottaNums:
        for j, val in enumerate(i):
            if j <= 5:
                histogramVals.append(val)

    plt.hist(histogramVals)
    plt.show()

def wrapper(ticketNumber = 160):
    ticketNumber = ticketNumber
    yottaMultiples, yottaRemainder = yotta_check(ticketNumber)
    yottaNums = ticket_generator(yottaMultiples, yottaRemainder, ticketNumber)
    fileDateString = dt.now().strftime("%Y_%m_%d")
    filenameExport = str(fileDateString) + "yottanums.csv"
    export(yottaNums, filename = filenameExport)
    return yottaNums


def main():

    ticketNumber = 160
    yottaMultiples, yottaRemainder = yotta_check(ticketNumber)
    yottaNums = ticket_generator(yottaMultiples, yottaRemainder, ticketNumber)
    export(yottaNums)
    histogram_generator(yottaNums)

if __name__ == "__main__":
    main()