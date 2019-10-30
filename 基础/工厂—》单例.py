class CarFactory:
    __obj = None  #类的私有属性，外部不能直接引用
    __init_flag = True

    def create_car(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"
    
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self):
        if CarFactory.__init_flag:
            # self.name = name
            print("init CarFactory......")
            CarFactory.__init_flag = False

class Benz:
    pass 
class BMW:
    pass
class BYD:
    pass

factory1 = CarFactory()
c1 = factory1.create_car("奔驰")
c2 = factory1.create_car("比亚迪")
print(c1)
print(c2)

factory2 = CarFactory()# 这里使用单例模式，从而是需要创建一个CarFactory类实例，即不同的factory指向同一个CarFactory
print(factory1)
print(factory2)