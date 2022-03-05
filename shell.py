import os , sys
from colorama import Fore 

run = True
currentdistro = "None"
BashCommand = ""
def main():
    while run:
        handlinginput()
def handlinginput():
    userinput = input(Fore.CYAN + "adamzz@" + currentdistro + " > ")
    exitshell(userinput)
    changedistro(userinput)
    # print(BashCommand)
    os.system(BashCommand)
def exitshell(Input):
    global run
    if Input == ("exit"):
        run = False
def changedistro(userinput):
    global BashCommand
    global currentdistro
    if userinput == "debian":
        currentdistro = "debian"
    elif userinput == "fedora":
        currentdistro = "fedora"
    elif userinput == "void":
        currentdistro = "void"
    elif userinput == "gentoo":
        currentdistro = "gentoo"
    elif userinput == "arch":
        currentdistro = "arch"
    elif userinput == "centos":
        currentdistro = "centos"
    elif userinput == "alpine":
        currentdistro = "alpine"
    elif userinput == "ubuntu":
        currentdistro = "ubuntu"
    else:
        if currentdistro == "debian":
            BashCommand = debian(userinput)
        elif currentdistro == "fedora":
            BashCommand = fedora(userinput)
        elif currentdistro == "void":
            BashCommand = void(userinput)
        elif currentdistro == "gentoo":
            BashCommand = gentoo(userinput)
        elif currentdistro == "arch":
            BashCommand = arch(userinput)
        elif currentdistro == "centos":
            BashCommand = centos(userinput)
        elif currentdistro == "alpine":
            BashCommand = alpine(userinput)
        elif currentdistro == "ubuntu":
            BashCommand = ubuntu(userinput)
        else:
            print("error: no distro passed in")

        
def debian(userinput):
    return "brl strat debian " + userinput
def fedora(userinput):
    return "brl strat fedora " + userinput
def void(userinput):
    return "brl strat void " + userinput
def gentoo(userinput):
    return "brl strat gentoo " + userinput
def arch(userinput):
    return "brl strat arch " + userinput
def centos(userinput):
    return "brl strat centos " + userinput
def alpine(userinput):
    return "brl strat alpine " + userinput
def ubuntu(userinput):
    return "brl strat ubuntu " + userinput
main()
