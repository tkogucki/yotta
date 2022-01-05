#!/usr/bin/python3

from utils import dictionary_gen as dg
from utils import upgraded_yotta as yotta
from utils import adb_controls as adbc

# function for generating tickets using all the utils
def gen_tickets_live(device, ticketList, clickCoords):
    for i in ticketList:
        coords = []
        print(f'Generating ticket {i}')
        for j in i:
            coords.append(clickCoords[j])
        adbc.input_ticket(device, coords)

device = adbc.connection()



# create dictionary
clickCoords = dg.dict_gen()

# creating yotta tickets
ticketNumberCount = 200*2
tickets = yotta.wrapper(ticketNumber= ticketNumberCount)
splittingIndex = int(ticketNumberCount/2)
ticketsACCT1 = tickets[0:splittingIndex]
ticketsACCT2 = tickets[splittingIndex:]

# deleting all previous tickets
adbc.delete_tickets(device, 185)

# generating acct 1 tickets
gen_tickets_live(device, ticketsACCT1, clickCoords)

print("/" * 100)
print("Complete generating tickets on account 1")
input("Press enter when ready to generate tickets for account 2...")
print("Generating tickets for account 2, standby...")

# deleting all previous tickets
adbc.delete_tickets(device, 185)

# generating account 2 tickets
gen_tickets_live(device, ticketsACCT2, clickCoords)

# End message
print("/" * 100)
print("Complete generating tickets on account 2")
print("All Tickets have been generated successfully")