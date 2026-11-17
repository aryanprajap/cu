numofemployees=int(input("enter total no of records"))

company=[]

for i in range (numofemployees):
    name=input("enter name of employee :")
    employeeID=int(input("enter the employeeID :"))
    salary=int(input("enter the salary :"))

    if salary>80000:
        print("high")
    elif salary>50000:
        print("medium")
    else:
        print("low")

employee_record = {
    "name" : name,
    "employeeID" : employeeID,
    "salary" : salary
}

company.append(employee_record)

for i in range (numofemployees):
    product_name=input("enter name of product :")
    productID=int(input("enter the productID :"))
    price=int(input("enter the price :"))
    quantity=int(input("enter the quantity :"))
    Total_value = price*quantity

product_record = {
    "name" : product_name,
    "ID" : productID,
    "price" : price,
    "quantity" : quantity,
    "total_value" : Total_value
    }

company.append(product_record)

print(company)
    

    