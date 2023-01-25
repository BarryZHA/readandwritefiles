import csv

infile = open("customers.csv", "r")
csv_reader = csv.reader(infile)

outfile = open("customer_country.csv","w")
csv_writer = csv.writer(outfile)

header = (["ID"], ["EmployeeName"], ["FinalPay"])
print(header)

for row in csv_reader: 
    csv_writer.writerow([row[1] + " " + row[2], row[4]])

infile.close()
outfile.close()






