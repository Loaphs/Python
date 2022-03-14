from asyncio.windows_events import NULL
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title('PhasTracker')
window.geometry('500x500')

l = Label(window, width=20, text='empty')
l.pack()

GhostList = []

class Ghost:
    def __init__(self, name, trait1, trait2, trait3):
        self.name = name
        self.t1 = trait1
        self.t2 = trait2
        self.t3 = trait3
    
    def __repr__(self):
        return repr(self.name)

def newlabel(ghost):
    ghostLabel = Label(window, font='calibri 14 bold', text=ghost)
    ghostLabel.pack(anchor='center')

def main(item):
    item = input()
    update(item)

def update(item):
    for ghost in ghosts:
        if hasattr(ghost, item) == False:
            ghosts.remove(ghost)
        else:
            newlabel(ghost)
        print(repr(ghost))
    main(item)


if __name__ == '__main__':
    emf = "EMF 5"
    orb = "Ghost Orbs"
    box = "Spirit Bos"
    frz = "Freezing Temps"
    fng = "Fingerprints"
    wrt = "Ghost Writing"
    dot = "D.O.T.S"

    ghosts = [
    Ghost('banshee', orb, fng, dot), Ghost('demon', frz, fng, wrt), Ghost('goryo', emf, fng, dot), Ghost('hantu', orb, frz, fng),
    Ghost('jinn', emf, frz, fng), Ghost('mare', orb, box, wrt), Ghost('myling', emf, fng, wrt), Ghost('obake', emf, orb, fng),
    Ghost('oni', emf, frz, dot), Ghost('onryo', orb, box, frz), Ghost('phantom', box, fng, dot), Ghost('poltergeist', box, fng, wrt),
    Ghost('raiju', emf, orb, dot), Ghost('revenant', orb, frz, wrt), Ghost('shade', emf, frz, wrt), Ghost('spirit', emf, box, wrt),
    Ghost('mimic', box, frz, fng), Ghost('twins', emf, box, frz), Ghost('wraith', emf, box, dot), Ghost('yokai', orb, box, dot),
    Ghost('yurei', orb, frz, dot) ]

    item = NULL

    main(item)
    window.mainloop()