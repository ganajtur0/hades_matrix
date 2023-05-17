class Stimuli:
    def __init__(self, pin, value, time):
        self.pin = pin
        self.value = value
        self.time = time

    def getPin(self):
        return self.pin

    def getValue(self):
        return self.value

    def getTime(self):
        return self.time

    def __str__(self):
        return "Stimuli( pin="+str(self.pin)+", value="+str(self.value)+", time="+str(self.time)+")"
