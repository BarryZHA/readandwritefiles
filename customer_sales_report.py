import csv 
infile = open("sales.csv", "r")
csv_reader = csv.reader(infile)
next(csv_reader,None)#skip header  

SalesData = {}

header = ["CustomerID", "SubTotal", "TaxAmount", "Freight", "GrandTotal"]
print(header)

##insert data 
for row in csv_reader: 
    CustomerID = row[0]
    SubTotal = "{:.2f}".format(float(row[3]))
    TaxAmount = "{:.2f}".format(float(row[4]))
    Freight = "{:.2f}".format(float(row[5]))
    GrandTotal = SubTotal + TaxAmount + Freight 

    if CustomerID in SalesData: 
        SalesData[CustomerID][0] += SubTotal 
        SalesData[CustomerID][1] += TaxAmount
        SalesData[CustomerID][2] += Freight 
        SalesData[CustomerID][3] += GrandTotal 
    else: 
        SalesData[CustomerID] += [SubTotal, TaxAmount, Freight, GrandTotal]

infile.close()
