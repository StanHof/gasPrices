class analiser:
    def __init__(self, prices , distances):
        self.prices = prices
        self.distances = distances
        self.prices_dates = []
        self.distances_dates = []
        for i in prices:
            self.prices_dates.append(i[0])
        print(self.prices_dates)
        for i in distances:
            self.distances_dates.append(i[0])
        print(self.distances_dates)
    def getDayCost(self , date):
        min(self.prices, key = lambda x : abs(x))
