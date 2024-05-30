class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Количество этажей: {self.numberOfFloors}')


h1 = House()
h1.setNewNumberOfFloors(25)
