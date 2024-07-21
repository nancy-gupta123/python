class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
         
    def get_brand(self):
        return  self.__brand + "!"   

    def full_name(self):
        return f"{self.__brand} {self.__model}" 

    def fuel_type(self):
        return "Petrol and Diesel"  


    @property
    def model(self):
        return self.__model 
    
    @staticmethod
    def general_description():
        return "Car are means of transport"


#my_car= Car("Toyota","Corolla")
#print(my_car.get_brand()) 
#print(my_car.model)

#print(my_car.full_name())


#my_car->object h
#Car->class h

#inheritance

class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"    

#my_tesla=Electric_car("Tesla","Model S","85Kwh") 
#print(isinstance(my_tesla,Car))
#print(isinstance(my_tesla,Electric_car))

#print(my_tesla.full_name()) 
#print(my_tesla.__brand)  
#print(my_tesla.get_brand())
#print(my_tesla.fuel_type())

#safari=Car("Tata","Safari")
#safari.model="city"
#safari.brand="Toyota"
#print(safari.fuel_type())
#print(safari.model)
#print(safari.brand)


#print(Car.total_car)
#print(Car.general_description())

class Battery:
    def battery_info(self):
        return "this is battery !"
    

class Engine:
    def engine_info(self):
        return "this is engine"  


class Electrinengine_two(Battery,Engine,Car):
    pass


my_new_tesla=Electrinengine_two("Tesla","model")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
