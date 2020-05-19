import csv

def fee(ip,free,rate):
    with open('output.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        free = float(free)
        rate = float(rate)
        temp = 0
        for row in csv_reader:
            if row[3] == ip :
                temp += float(row[12])
        for row in csv_reader:
            if row[4] == ip :
                temp += float(row[12])
        fee = temp/1000000
        if (fee < free):
            rm = ((free - fee)*1000)
            print('Number of used data : %.3f Mb'%(fee))
            print('Number of free data left: %.3f Kb'%(rm))
        else:
            fee = (((temp/1000000)-free) * rate)
            print('Cost of using data: %.3f rub'%(fee))
    

def graphcsvfile(ip):
    with open('output.csv') as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter=',')
        for row in csv_reader:
            if (row[3] == ip) or (row[4] == ip):
                with open('graph.csv','a',newline='') as csv_file2:
                    filewriter = csv.writer(csv_file2)
                    filewriter.writerow([row[0]+row[1],row[12]])
                     
print('\t\t\tLab2')
ip = input('fee of user: ')
free = input('numbers of free data (Mb):')
rate = input('data rate: ')
fee(ip,free,rate)
graph(ip)
