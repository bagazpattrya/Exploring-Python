#THIS CAN CALCULATE RMS SHIT
import math

def findVPP(VPVal):
    VPP = VPVal * 2
    return VPP

def findRMS(Vpeak):
    RMS = Vpeak / math.sqrt(2)
    return RMS

def findVpeak(RMS):
    Vpeak = RMS * math.sqrt(2)
    return Vpeak


def choice(case):
    if case == 1:
        RMS = findRMS(float(input("Enter Vpeak Value")))
        print(RMS)
    if case == 2:
        VP = findVpeak(float(input("Enter RMS Value")))
        print(VP)



def main():
    program = True
    while program == True:
        print("WELCOME TO THIS RMS/VP CALCULATOR, Please insert\n1. to Find RMS\n2. Find VPP")
        case = int(input("Enter choice : "))
        choice(case)
        programStatus = input("Calculate again? y/n")
        if programStatus != 'y':
            print("THANK YOU!")
            program = False

main()
