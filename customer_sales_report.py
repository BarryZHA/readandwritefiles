import csv 
infile = open("sales.csv", "r")
csv_reader = csv.reader(infile)

outfile = open("salesreport.csv", "w", newline="")
writer = csv.writer(outfile)
writer.writerow(["CustomerID", "GrandTotal"])
# Keep track of the current customer ID and GrandTotal
current_customer = None
current_total = 0
next(csv_reader,None) #skip header  
# Iterate through each row
for row in csv_reader:
    # Get the customer's ID
    customer_id = row[0]
    if current_customer != customer_id:
        if current_customer is not None:
            writer.writerow([current_customer, "{:.2f}".format(current_total)])
        current_customer = customer_id
        current_total = 0
    current_total += float(row[3]) + float(row[4]) + float(row[5])
#Write the last cutomer's ID and GrandTotal 
writer.writerow([current_customer, current_total])

infile.close()
outfile.close()
