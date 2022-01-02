class Pillar():
    def __init__(self, a, b, h):
        self._a = a 
        self._b = b 
        self._h = h 
    def getVolume(self):
        return "기둥의 부피: " + str(self._a * self._b * self._h) 
    def getSurface(self):
        return "기둥의 겉넓이: " + str((2 * (self._a * self._b))\
             + ((2 * (self._a + self._b)) * self._h))

a = Pillar(3, 4, 5)
print(a.getVolume())
print(a.getSurface())

class Car():
    def __init__(self, max_speed = 160, speed = 0):
        self._max_speed = max_speed
        self._speed = speed 
    def getSpeedUp(self):
        self._speed += 20
        return self._speed 
    def getSpeedDown(self):
        self._speed -= 20
        return self._speed
    def __str__(self):
        if 0 <= self._speed <self._max_speed:
            return f"Maximum speed: {self._max_speed}km/h\nCurrent speed: {self._speed}km/h"
        return "Speed cannot be detected."
print(Car())
car1 = Car(180, 100)
print(car1)
car1.getSpeedDown()
print(car1)
car1 = Car(180, 180)
print(car1)
car1 = Car(170, 60)
car1.getSpeedUp()
print(car1)

class SportCar(Car):
    def __init__(self, max_speed=200, speed=0):
        super().__init__(max_speed, speed)
    def getSpeedUp(self):
        self._speed += 45
        return self._speed 
    def getSpeedDown(self):
        self._speed -= 45
        return self._speed 
    def __str__(self):
        if 0 <= self._speed < self._max_speed:
            return f"Maximum speed: {self._max_speed}km/h\nCurrent speed: {self._speed}km/h"
        return "Speed cannot be detected."

print(SportCar())
car2 = SportCar(180, 70)
car2.getSpeedUp()
print(car2)
car2.getSpeedDown()
print(car2)
car2.getSpeedDown()
print(car2)

class Truck(Car):
    def __init__(self, max_speed = 100, speed = 0):
        super().__init__(max_speed, speed)
    def getSpeedUp(self):
        self._speed += 15
        return self._speed 
    def getSpeedDown(self):
        self._speed -= 15
        return self._speed 
    def __str__(self):
        if 0 <= self._speed < self._max_speed:
            return f"Maximum speed: {self._max_speed}km/h\nCurrent speed: {self._speed}km/h"
        return "Speed cannot be detected."

print(Truck())
car2 = Truck(120, 40)
car2.getSpeedUp()
print(car2)
for i in range(3):
    car2.getSpeedDown()
print(car2)
