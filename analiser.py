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

    def findClosestDate(self , list , targetDate):
        start = 0
        finish = len(list) - 1
        val = 0
        while start<=finish:
            i = finish - (finish - start) //2
            if abs(list[i] - targetDate) < abs(list[val] - targetDate ):
                val = i
            elif abs(list[i] - targetDate) == abs(list[val] - targetDate):
                val = min(i , val)
            if list[i] == targetDate:
                return i
            elif list[i] < targetDate:
                start = i + 1
            else:
                finish = i - 1
          #  print(f"{start}  {finish}")
           # print(f"{list[i]}  {i}")
            print(f"{start} {i} {finish}")
        return min(i  , val)

