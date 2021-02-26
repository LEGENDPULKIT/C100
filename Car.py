class Car(object):
    def __init__(self,modal,color,company,speed_limit):
        self.color=color
        self.company=company
        self.modal=modal
        self.speed_limit=speed_limit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelarate(self):
        print("Accelarating")

    def change_gear(self,gear_type):
        print("gear changed")        

Audi=Car("A6","red","Audi",120)

print(Audi.start())
print(Audi.stop())
print(Audi.accelarate())
print(Audi.color)
