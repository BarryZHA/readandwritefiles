import csv 
infile = open("EmployeePay.csv", "r")
csv_reader = csv.reader(infile)
next(csv_reader,None) ##skip the header 

header = ["ID", "EmployeeName", "TotalPay" ]

print(header)

for row in csv_reader: 
    print([row[0], row[1] + " " + row[2], "{:.2f}".format(float((int(row[3]) * ( 1 + float(row[4])))))])

infile.close()

