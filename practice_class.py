class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


# class FlyableUnit(Unit, Flyable): #Unit생성자 나옴
class FlyableUnit(Flyable, Unit):  # Flyable 생성자
    def __init__(self):
        # super().__init__() #둘중 하나만 나옴.

        Unit.__init__(self)
        Flyable.__init__(self)  # 두개 다 나옴


# 드랍쉽
dropship = FlyableUnit()
