'''
1. Create a Vehicle class with following  variables and methods

    Instance Variable

            1.name

            2.max_speed with default value 10

            3.mileage with default value 35

    Instance method

            1.seating_capacity(self,capacity)

2.  Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

 (note:- Use the above question code for your parent Vehicle class. You need to use method overriding.cls

3.Define property that should have the same value for every class instance for above Vehicle class.
'''
class Vehicle:
    color="White"
    def setprop(self,name,max_speed=10,mileage=35):
        self.name=name
        self.maxspeed=max_speed
        self.mileage=mileage

    def seating_capacity(self,capacity):
        print('Name of vehicle=',self.name)
        print('Maximum Speed of vehicle=',self.maxspeed)
        print('Mileage of vehicle=',self.mileage)
        print('Seating capacity of vehicle is:',capacity,'seats')

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

b=Bus()
b.setprop('Bus')
b.seating_capacity()
print(f'Color of Bus is {b.color}.')
print(f'Color of Vehicle is {b.color}.')

