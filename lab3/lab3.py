import csv
import sys
import os
import win32com.client
from mailmerge import MailMerge

wdFormatPDF = 17


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
        use = temp/1000000
        if (use < free):
            rm = ((free - use)*1000)
            print('Number of used data : %.3f Mb'%(use))
            print('Number of free data left: %.3f Kb'%(rm))
        else:
            fee = ((use-free) * rate)
            print('Cost of using data: %.3f rub'%(fee))
    return use

def graph(ip):
    with open('output.csv') as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter=',')
        for row in csv_reader:
            if (row[3] == ip) or (row[4] == ip):
                with open('graph.csv','a',newline='') as csv_file2:
                    filewriter = csv.writer(csv_file2)
                    filewriter.writerow([row[0]+row[1],row[12]])

def billing(call_min,call_fee,mes_fee,mes_count,netuse,intfee,total,tax):
    total = str(total)
    tax = str(tax)
    call_min = str(call_min)
    call_fee = str(call_fee)
    mes_fee = str(mes_fee)
    mes_count = str(mes_count)
    netuse = str(netuse)
    intfee = str(intfee)
    template = "base.docx"
    document = MailMerge(template)
    document.merge(
        bank='VTB Bank',
        bank_code='044525187',
        bank_acc_num='40262000000',
        inn='7702070139',
        kpp='783501001',
        comp_name='Stark industry',
        comp_acc_num='6204000000',
        check_num='20022016',
        day='19',
        month='3',
        year='20',
        supplier='MTS telecom',
        buyer='Bruce Wayne',
        osn='№ 20022016 от 12.02.2020',
        serv_name1='call service',
        num1=call_min,
        count1='min',
        price1='1 rub',
        sum1=call_fee,
        serv_name2='messages',
        num2=mes_count,
        count2='message(s)',
        price2='5 rub',
        sum2=mes_fee,
        serv_name3='internet',
        num3=netuse,
        count3='Mb',
        price3='0.5',
        sum3=intfee,
        total=total,
        tax=tax,
        ftotal=total,
        supervisor='Nick Furry',
        accountant='Morgan Freeman')
    document.write('bill.docx')
    in_file=r'C:\Users\Lequa\Desktop\mobile năm 3\lab3\bill.docx'
    out_file=r'C:\Users\Lequa\Desktop\mobile năm 3\lab3\bill.pdf'
    word = win32com.client.Dispatch('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()                         

print('\t\t\tLab3')
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
if int(rate_in) == 0:
    in_min=0
else:
    in_min = in_fee/float(rate_in)
if int(rate_out) ==0:
    out_min=0
else:
    out_min = out_fee/float(rate_out)

call_min = float(in_min) + float(out_min)
call_fee = float(in_fee) + float(out_fee) 
mes_fee = mes(phonenum,rate_mes)
mes_count= mes_fee/float(rate_mes)
print('Cost of incoming call: %.3f'%(in_fee))
print('Cost of outgoing call: %.3f'%(out_fee))
print('Cost of messages: %d'%(mes_fee))
ip = input('fee of user: ')
free = input('numbers of free data (Mb):')
rate = input('data rate: ')
netuse = fee(ip,free,rate)
if float(netuse) < float(free):
    intfee = 0
elif float(netuse) > float(free):
    intfee = (netuse * rate)
graph(ip)
total = (call_fee + mes_fee + intfee)
tax = ((call_fee + mes_fee + intfee)/100*15)
billing(call_min,call_fee,mes_fee,mes_count,netuse,intfee,total,tax)
