import csv

# fields
product_field = ['product_id', 'name', 'barcode', 'date_of_manufacture', 'price']
employee_field = ['employee_id', 'name', 'salary', 'department']
customer_field = ['customer_id', 'name', 'age', 'city', 'state']


# for Products
def create_product_file():
    ''' create a file and field'''
    with open("products.csv", 'w') as products_file:
        # creating a csv writer object 
        csv_writer = csv.writer(products_file)
        # writing the fields 
        csv_writer.writerow(product_field)


def add_product_in_file():
    ''' add the product in the product list file'''
    with open("products.csv", 'a') as products_file:
        # creating a csv writer object 
        csv_writer = csv.writer(products_file)
        # writing the fields
        n = int(input("enter number of product to add in files: "))
        for i in range(n):
            print(f'For {i} product details')
            row_data = []
            for j in range(len(product_field)):
                row_data.append(input(f'Enter {product_field[j]}: '))
            csv_writer.writerow(row_data)
            print("\n")


def see_product():
    '''see product available in store'''
    with open("products.csv", 'r') as file:
        csv_file = csv.reader(file)
        row_count = sum(1 for row in csv_file) -1
        print(f'Total Number of products available in store : {row_count}')



# for employee
def create_employee_file():
    ''' create a file and field'''
    with open("employee.csv", 'w') as employee:
        # creating a csv writer object 
        csv_writer = csv.writer(employee)
        # writing the fields 
        csv_writer.writerow(employee_field)
        

def add_employee_in_file():
    ''' add the product in the product list file'''
    with open("employee.csv", 'a') as employee:
        # creating a csv writer object 
        csv_writer = csv.writer(employee)
        # writing the fields
        n = int(input("enter number of product to add in files: "))
        for i in range(n):
            print(f'For {i} product details')
            row_data = []
            for j in range(len(employee_field)):
                row_data.append(input(f'Enter {employee_field[j]}: '))
            csv_writer.writerow(row_data)
            print("\n")


def see_employee():
    '''see product available in store'''
    with open("employee.csv", 'r') as file:
        csv_file = csv.reader(file)
        row_count = sum(1 for row in csv_file) -1
        print(f'Total Number of employee : {row_count}')
        

def find_total_salary():
    '''find total salary'''
    with open("employee.csv", 'r') as file:
        count = 0
        total_salary = 0
        csv_file = csv.reader(file)
        for row in csv_file:
            count += 1
            if count >=2:
                total_salary += int(row[2])
        print(f'total salary: {total_salary}')


# for sold out product
def see_sold_product():
    '''see sold product'''
    with open("sold_products.csv", 'r') as file:
        csv_file = csv.reader(file)
        row_count = sum(1 for row in csv_file) -1
        print(f'Total Number sold out product : {row_count}')

def find_total_revenue():
    '''Total revenue generated'''
    with open("sold_products.csv", 'r') as file:
        count = 0
        total_revenue = 0
        csv_file = csv.reader(file)
        for row in csv_file:
            count += 1
            if count >=2:
                total_revenue += int(row[4])
        print(f'total salary: {total_revenue}')


# for customer
def create_customer_file():
    ''' create a file and field'''
    with open("customer.csv", 'w') as customer_file:
        # creating a csv writer object 
        csv_writer = csv.writer(customer_file)
        # writing the fields 
        csv_writer.writerow(customer_field)


def add_customer_in_file():
    ''' add the product in the product list file'''
    with open("customer.csv", 'a') as customer_file:
        # creating a csv writer object 
        csv_writer = csv.writer(customer_file)
        # writing the fields
        n = int(input("enter number of customer to add in files: "))
        for i in range(n):
            print(f'For {i} customer details')
            row_data = []
            for j in range(len(customer_field)):
                row_data.append(input(f'Enter {customer_field[j]}: '))
            csv_writer.writerow(row_data)
            print("\n")

def oldest_customer():
    '''oldest customer'''
    with open("customer.csv", 'r') as file:
        count = 0
        age =[]
        name = []
        csv_file = csv.reader(file)
        for row in csv_file:
            count += 1
            if count >=2:
                age.append(int(row[2]))
                name.append(row[1])
        print(f'oldest customer age: {max(age)}')
        index_of_max_age = age.index(max(age))
        print(f'name of youngest customer :{name[index_of_max_age]}')

def youngest_customer():
    '''youngest customer'''
    with open("customer.csv", 'r') as file:
        count = 0
        age =[]
        name = []
        csv_file = csv.reader(file)
        for row in csv_file:
            count += 1
            if count >=2:
                age.append(int(row[2]))
                name.append(row[1])
        print(f'oldest customer age: {min(age)}')
        index_of_min_age = age.index(min(age))
        print(f'name of youngest customer :{name[index_of_min_age]}')


def main():
    # Introduction of System and option list
    introList = [
        "\nWelcome to Inventory Management System",
        "--------------------------------------\n",
        "Enter Option number according to the task\n",
        "1. See available product in store.",
        "2. See employee working in warehouse.",
        "3. Find the total salary paid to all employees.",
        "4. See product which were sold.",
        "5. Find total revenue generated.",
        "6. Find the oldest customer",
        "7. Find the youngest customer",
        "-------------------------------",
        "For creating record and storing details",
        "-------------------------------",
        "8. Create a file to write a products",
        "9. write product details in product file",
        "10.Crate a employee file",
        "11.add employee details in employee file",
        "12.create a customer files",
        "13.add a customer details in the customer files",
    ]
    # print introduction and option list
    for i in introList:
        print(i)
    
    # enter the input from the user
    n = int(input("Enter a number : "))

    # switch case to choose options
    match n:
        case 1:
            see_product()
        case 2:
            see_employee()
        case 3:
            find_total_salary()
        case 4:
            see_sold_product()
        case 5:
            find_total_revenue()
        case 6:
            oldest_customer()
        case 7:
            youngest_customer()

        # to create files and add details in file
        # for product
        case 8:
            create_product_file()
        case 9:
            add_product_in_file()

        # for employee
        case 10:
            create_employee_file()
        case 11:
            add_employee_in_file()
        
        # for customer
        case 12:
            create_customer_file()
        case 13:
            add_customer_in_file()

        case default:
            print("sorry for wrong input")


if __name__ == "__main__":
    main()