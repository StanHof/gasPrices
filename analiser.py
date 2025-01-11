class analiser:
    def __init__(self, prices , distances):
        self.prices = prices
        self.distances = distances
        self.prices_dates = []
        self.distances_dates = []
        self.fuelUsage = 5
        for i in prices:
            self.prices_dates.append(i[0])
        print(self.prices_dates)
        for i in distances:
            self.distances_dates.append(i[0])

    def findClosestDate(self, dateList, targetDate):
        start = 0
        finish = len(dateList) - 1
        val = 0
        while start <= finish:
            i = finish - (finish - start) //2
            if abs(dateList[i] - targetDate) < abs(dateList[val] - targetDate):
                val = i
            elif abs(dateList[i] - targetDate) == abs(dateList[val] - targetDate):
                val = min(i , val)
            if dateList[i] == targetDate:
                return i
            elif dateList[i] < targetDate:
                start = i + 1
            else:
                finish = i - 1
            #print(f"{start} {i} {finish}")
        return min(i  , val)
    def getFuelCost(self , date):
        return self.prices[self.findClosestDate(self.prices_dates , date)][1] / 1000
    def getDistance(self, date):
        return self.distances[self.findClosestDate(self.distances_dates , date)][1]
    def getDayUsage(self, date):
        return self.getDistance(date) * self.getFuelCost(date) / self.fuelUsage