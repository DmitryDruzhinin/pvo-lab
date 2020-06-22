class Loco:
    def __init__(self):
        self._loco = 'oooTT'

    def __str__(self):
        return self._loco


class Train:
    def __init__(self, weight):
        self._wagons = []
        self._max_weigth = 16383
        self._weight = weight

    def SetLoco(self):
        self._loco = Loco()

    def AddWagon(self, wagon_type):
        self._wagons.append(wagon_type)

    def Run(self):
        if self._weight <= self._max_weigth:
            return True
        else:
            return False

    def __str__(self):
        train = str(self._loco)
        for wagon in self._wagons:
            train += str(wagon)
        return train


class TrainPass(Train):
    def __init__(self, _weight):
        super().__init__(_weight)
        self.type = 'pass'


class TrainCargo(Train):
    def __init__(self, _weight):
        super().__init__(_weight)
        self.type = 'cargo'


class Wagon:
    def __init__(self):
        self.type = None


class WagonPass(Wagon):
    def __init__(self, place=''):
        super().__init__()
        self.type = 'pass'

    def __str__(self):
        return ".[_ _]"


class WagonCargo(Wagon):
    def __init__(self):
        super().__init__()
        self.type = 'cargo'

    def __str__(self):
        return ".(_ _)"


class WagonCoupe(WagonPass):
    def __init__(self, place=''):
        super().__init__(place)
        self.comf_type = 'coupe'


class WagonPlat(WagonPass):
    def __init__(self, place=''):
        super().__init__(place)
        self.comf_type = 'plat'


class WagonSit(WagonPass):
    def __init__(self, place=''):
        super().__init__(place)
        self.comf_type = 'sit'


t = Train(int(input("enter train mass: ")))
t.SetLoco()
t.AddWagon(WagonPass())
t.AddWagon(WagonPass())
t.AddWagon(WagonCargo())
print(t)
ok = t.Run()
if ok:
    print("ok")
else:
    print("can not run, too big mass")
