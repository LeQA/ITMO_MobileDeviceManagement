import csv
def in_call(phonrnum,free_in,rate_in):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        temp1 = 0
        for row in csv_reader:
            if row[2] == phonenum :
                temp1 += float(row[3])
        fee_in = ((temp1 - float(free_in)) * int(rate_in))
        if fee_in < 0:
            fee_in = 0
    return (fee_in)

def out_call(phonrnum,free_out,rate_out):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        temp2 = 0
        for row in csv_reader:
            if row[1] == phonenum :
                temp2 += float(row[3])
        fee_out = ((temp2 - float(free_out)) * int(rate_out))
        if fee_out < 0:
            fee_out = 0
    return (fee_out)

def mes(phonenum,rate_mes):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[2] == phonenum :
                fee_mes = int(row[4]) * int(rate_mes)
    return (fee_mes)

print('\t\t\tLab1')
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t\t{row[4]}')
phonenum = input('fee of user: ')
free_in = input('numbers of free incoming minutes: ')
free_out = input('numbers of free outcoming minutes:')
rate_in = input('incoming call rate: ')
rate_out = input('outcoming call rate: ')
rate_mes = input('SMS rate: ')
in_fee = in_call(phonenum,free_in,rate_in)
out_fee = out_call(phonenum,free_out,rate_out)
mes_fee = mes(phonenum,rate_mes)
print('Cost of incoming call: %.3f rub'%(in_fee))
print('Cost of outgoing call: %.3f rub'%(out_fee))
print('Cost of messages: %d rub'%(mes_fee))
