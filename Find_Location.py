from tkinter import *

import subprocess

root = Tk()

root.resizable(0,0)

root.title("Find Location IP")

def seeker():
    subprocess.run("Sudo apt-get install git",shell=True)
    subprocess.run("y",shell=True)
    subprocess.run("git clone https://github.com/thewhiteh4t/seeker.git", shell=True)


def Ipgeo():
    subprocess.run("Sudo apt-get install git", shell=True)
    subprocess.run("y", shell=True)
    subprocess.run("git clone https://github.com/maldevel/IPGeoLocation.git", shell=True)


def instruction():
    subprocess.run("Sudo apt-get install git", shell=True)
    subprocess.run("y" ,shell=True)
    subprocess.run("git clone https://github.com/Hansploit/findlocationip_instruction.git", shell=True)

welcome = Label(root, text="Hello Guys Welcome to Find Location IP Tool").pack()


seeker = Button(root, text="Click To install Seeker On you device", command=seeker).pack()


Space2 = """
"""

space2 = Label(root, text=Space2).pack()

IP_geo_location = Button(root, text="click to Install IP Geolocation Tool", command=Ipgeo).pack()


Space = """
"""

space = Label(root, text=Space).pack()


instruction = Button(root, text="Click to Download Instruction File", command=instruction).pack()

root.mainloop()
