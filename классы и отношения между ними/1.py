class Locomotive:
    def __init__(self):
        self._loco = 'oooTT'

    def __repr__(self):
        return self._loco


class Train:
    def __init__(self, weight):
        self._wagons = []
        self._max_weigth = 20000
        self._weight = weight
        self._loco = None
        self.type = 'default'

    def add_loco(self):
        self._loco = Locomotive()

    def add_wagon(self, wagon_type):
        self._wagons.append(wagon_type)

    def run(self):
        if (self._weight <= self._max_weigth):
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


class Wagon():
    def __init__(self):
        self.type = None


class WagonPass(Wagon):
    def __init__(self, place=''):
        self.place = place
        self.type = 'passenger'

    def __repr__(self):
        return ".[_ _]"


class WagonCargo(Wagon):
    def __init__(self):
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


train = TrainPass(10000)
train.add_loco()
train.add_wagon(WagonPass())
train.add_wagon(WagonCargo())
print(train)
print(train.run())
