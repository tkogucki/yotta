#!/usr/bin/python3

from ppadb.client import Client
import time

def connection():
    # accessing adb server
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()

    if len(devices) == 0:
        print('no device attached')
        quit()

    device = devices[0]
    # Tap input example
    # device.shell(f'input tap 116 1946')
    return device

def tap(device, coords = (116,2066)):
    device.shell(f' input tap {int(coords[0])} {int(coords[1])}')

def input_ticket(device, coordList):
    # create new ticket
    newTicketCoords = (999,1108)
    tap(device, newTicketCoords)
    time.sleep(1)
    for i, val in enumerate(coordList):
        if i == 6:
            #sleep half a second to allow for animation
            time.sleep(1)
            tap(device, val)
        else:
            tap(device, val)
    # confirm ticket pick
    time.sleep(0.5)
    confirmationCoord = (524, 713)
    tap(device, confirmationCoord)
    #sleeping to allow the return animation to complete
    time.sleep(1.5)
    print("Ticket Generation Complete")

def delete_tickets(device, num2Delete = 100):
    deleteButton  = (939, 1311)
    confirmButton = (604, 1499)
    i = 0
    while i < num2Delete:
        print(f"Deleting ticket number: {i}")
        tap(device, deleteButton)
        time.sleep(.75)
        tap(device,confirmButton)
        time.sleep(.75)
        i = i + 1




if __name__ == "__main__":
    device = connection()
    # should tap number 64
    # tap(device)
    delete_tickets(device)
    input_ticket(device, [(962, 1946), (116,2066), (257,2066), (398, 2066), (539, 2066), (680, 2066), (962, 1856)])