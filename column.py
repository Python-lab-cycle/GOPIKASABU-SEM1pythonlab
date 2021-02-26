import csv
with open('emp.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("emp no empname")
    print("--------------------")
    for row in data:
        print(row['emp no'],row['empname'])
