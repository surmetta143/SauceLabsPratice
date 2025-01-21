import time
class BaseClass:

    def __init__(self, driver):
        self.driver = driver
    def Implicity_Wait(self,value):
        time.sleep(value)
