class Dog():
    """小狗的类，属性包含name和age"""

    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def sit(self):
        """小狗的蹲下行为"""
        print("The dog have been sited")
    def roll_over(self):
        """小狗的翻滚行为"""
        print("The dog roll over")

my_dog = Dog("jack", 10)

print("my dog is " + my_dog.name.title() + ".")
my_dog.sit()
my_dog.roll_over()

#在类内使用属性
class Car():
    """这是一个汽车的类"""
    def __init__(self, year, name):
        self.year = year
        self.name = name
        #给属性一个初始值
        self.color = "black"

    def get_car_info(self):
        """打印汽车信息"""
        print("The car make in " + str(self.year) + 
                " name is " + self.color + 
                " " + self.name)
    def set_color(self, color):
        """更改汽车颜色"""
        self.color = color

my_car = Car(2016, "Audi")
my_car.get_car_info()
#直接修改属性
my_car.color = "red"
my_car.get_car_info()
#使用方法修改属性
my_car.set_color("blue")
my_car.get_car_info()


#继承
class ElectricCar(Car):
    """这是一个电动汽车的类"""
    def __init__(self, year, name):
        super().__init__(year, name)
        self.power = 100
    #通过 同名 来完成对父类方法的屏蔽
    def get_car_info(self):
        """打印汽车信息"""
        print("The car make in " + str(self.year) + 
                " name is " + self.color + 
                " " + self.name +
                " bettry have " + str(self.power))

my_electric_car = ElectricCar(2019, "TSLA")
my_electric_car.get_car_info()

#使用另一个类
class Battery():
    """电池的类"""
    def __init__(self, battery_size = 3000):
        self.size = battery_size
    
class Phone():
    """手机的类"""
    def __init__(self, name, os):
        self.name = name
        self.os = os
        self.battery = Battery()
    def get_phone_info(self):
        print("This phone be made in " + self.name + " use " +
        self.os + " OS " +
        "have " + str(self.battery.size) + "mah battery")

my_phone = Phone("xiaomi","android")
my_phone.get_phone_info()







