import csv
from matplotlib import pyplot
import numpy as np
from os.path import isfile

def CSV_Read(FileName):
    with open(FileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count==0:
                Header=row
                lstf=[[] for i in range(len(Header))]
            else:
                index=0
                for item in row:
                    lstf[index].append(item)
                    index+=1
            line_count += 1
    return [line_count-1, Header, lstf]

def CSV_Plot(Data, Header, ColNum1, ColNum2):
    #pyplot.plot(Data[ColNum1],Data[ColNum2],'ro')
    pyplot.plot([float(item) for item in Data[ColNum1]],[float(item) for item in Data[ColNum2]],'.')
    #pyplot.ylabel(Header[ColNum2])
    #pyplot.xlabel(Header[ColNum1])
    #pyplot.xlim(0,40)
    pyplot.show()
    return True

def Trend(Data, ColNum1, ColNum2):
    z=np.polyfit([float(item) for item in Data[ColNum1]],[float(item) for item in Data[ColNum2]],1)
    return z

def CSV_Write(FileName, Data, Header):
    new = not isfile(FileName) #checks if the file exists
    #Potential improvement: if the file exists use your CSV_Read function to ensure the number of columns in Data match number of columns in file
    with open(FileName, 'a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        if new:    writer.writerow(Header)
        resortedData = [[Data[i][r] for i in range(len(Data))]for r in range(len(Data[0]))] #convert the elements of the list from columns to rows
        for r in resortedData:
            writer.writerow(r)

def is_date(string):
    try:
        datetime.datetime.strptime(string, '%Y-%m-%d')
        return True
    except:
        return False
    
def CSV_Plot_vs_Time(Data, Header, ColNum1):
    date_found = [is_date(col[0]) for col in Data]
    if sum(date_found)>1: print("Warning!! More than one date column found in data. Review Data")
    date_index = date_found.index(True)
    dateTime = [datetime.datetime.strptime(i,'%Y-%m-%d') for i in Data[date_index]]
    #dateTime = [parse(i+" "+"16:00") for i in Data[date_index]]
    plot.plot(dateTime,[float(i) for i in Data[ColNum1]])
    plot.xlabel(Header[0])
    plot.ylabel(Header[2])
    plot.show()
    


                          



    
    
