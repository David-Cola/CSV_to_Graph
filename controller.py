from finalproject import Analyzer

a = Analyzer("config.csv")
#a.plot(0)

for i in range(0, a.number_of_datasets):
    a.plot(i)
    print(a.trend(i))
