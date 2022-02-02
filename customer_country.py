import csv

customers = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

customer_file = csv.reader(customers, delimiter = ',')

# to skip a line if the file contains a header record
next(customer_file)

for record in customer_file: 
    print('Name:', record[1], record[2])
    print('Country:',record[4])
    outfile.write(record[1] + ',' + record[2] + ',' + record[4] + '\n')
       
#for record in customer_file:
    #outfile.write(record[1])
    #outfile.write(record[2])
    #outfile.write(record[4])
        
outfile.close()

