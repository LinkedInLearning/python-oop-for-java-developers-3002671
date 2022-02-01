class lamp:
    def __init__(self, title, power, intensity):
        self.title = title                        #Notice Python allows the class variable title to be the same name as the formal parameter title
        self.power = power
        self.intensity = intensity

    def displayLampStatus(self):
        print(self)

    def lampOff(self):
        self.power = False

    def lampOn(self):
        self.power = True

    def increaseIntensity(self):
        self.intensity += 1

    def decreaseIntensity(self):
        self.intensity -= 1

    def __str__(self):          #Python's implementation of Java toString()
        return  "lamp title is " + self.title +  ", lamp power is " +  str(self.power) +  ", lamp intensity is " +  str(self.intensity)


if __name__ == "__main__":
    studyRmLamp = lamp("Study Room Lamp", False, 0)  # instantiate studyRmLamp
    livingRmLamp = lamp("Living Room Lamp", True, 20)  # instantiate livinRmLamp


    studyRmLamp.displayLampStatus()
    livingRmLamp.displayLampStatus()

    print("Turning studyRmLamp On and Increasing Intensity")
    studyRmLamp.lampOn()
    studyRmLamp.increaseIntensity()
    studyRmLamp.displayLampStatus()

    print("Decreasing livingRmLamp intensity")
    livingRmLamp.decreaseIntensity()
    livingRmLamp.displayLampStatus()