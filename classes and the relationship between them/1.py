class Loco:
    def __init__(self):
        self._loco = 'oooTT'

    def __repr__(self):
        return self._loco


class Train:
    def __init__(self, weight):
        self._wagons = []
        self._max_weigth = 16383
        self._weight = weight
        self._loco = None
        self.type = 'default'

    def add_loco(self):
        self._loco = Loco()

    def add_wagon(self, wagon_type):
        self._wagons.append(wagon_type)

    def run(self):
        if self._weight <= self._max_weigth:
            return True
        else:
            return False

    def __repr__(self):
        train = str(self._loco)
        for wagon in self._wagons:
            train += str(wagon)
        return train


class TrainPass(Train):
    def __init__(self, _weight):
        super().__init__(_weight)
        self.type = 'passanger'


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
        self.place = place
        self.type = 'passenger'

    def __repr__(self):
        return ".[_ _]"


class WagonCargo(Wagon):
    def __init__(self):
        super().__init__()
        self.type = 'cargo'

    def __repr__(self):
        return ".(_ _)"


class WagonPassCoupe(WagonPass):
    def __init__(self, place=''):
        super().__init__(place)
        self.comf_type = 'coupe'


class WagonPassPlat(WagonPass):
    def __init__(self, place=''):
        super().__init__(place)
        self.comf_type = 'plat'


class WagonPassSit(WagonPass):
    def __init__(self, place=''):
        super().__init__(place)
        self.comf_type = 'sit'


t = Train(int(input("enter train mass: ")))
t.add_loco()
t.add_wagon(WagonPass())
t.add_wagon(WagonCargo())
print(t)
ok = t.run()
if ok:
    print("ok")
else:
    print("can not run, too big mass")
