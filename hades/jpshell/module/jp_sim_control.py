from jp_design_os import *

def getSimulator():
    global simulator
    editor = getEditor()
    simulator = editor.getSimulator()
    return simulator


def setSimulator(sim):
    global simulator
    simulator = sim


def updateSimulator():
    global simulator
    editor = getEditor()
    simulator = editor.getSimulator()


def pauseSimulator():
    simulator = getSimulator()
    simulator.pauseSimulation()


def resetSimulator():
    simulator = getSimulator()
    simulator.initializeSimulator() 


def runSimulator(time=""):
    simulator = getSimulator()
    if(time):
        pass
    else:
        simulator.runForever()
