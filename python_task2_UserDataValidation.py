#importing neccessary module for random string generator
import random
import string

#Function to randomly generate last five strings
def generate_random_string(length):
    all_letters = string.ascii_lowercase
    RandString = "".join(random.choice(all_letters) for i in range(length))
    return RandString

def DisplayDetails(Firstname, Lastname, email, password):
    print("Below are your details:\n")
    print("Firstname: " + Firstname + ".\n")
    print("Lastname: " + Lastname + ".\n")
    print("Email: " + email + ".\n")
    print("password: " + password + ".\n")


#Employee detail container
employeeDetails = []

def Add_employee():
    #Employee details
    Firstname = input("Please Enter your first name:_")
    Lastname = input("Please Enter your last name:_")
    email = input("Please Enter your email address:_")

    password = str(Firstname[:2]) + str(Lastname[:2]) + str(generate_random_string(5))
    print("{}, is your computer generated password".format(password))

    while True:
        Response = input("Are you statisfied with it?..y/n:>>")
        if Response == str("y" or "Y"):
            DisplayDetails(Firstname, Lastname, email, password) 
            currentEmployee = [Firstname, Lastname,email, password]   
            employeeDetails.append(currentEmployee)
        elif Response == str("n" or "N"):
            UserPassword = input("Please Enter your desired Password[NB Password must not be less than 7 characters]:>>")
            while len(UserPassword) < 7:
                print("Password must be 7 characters or more")
                UserPassword = input("Please Enter your desired Password[NB Password must not be less than 7 characters]:>>")
                password = UserPassword  
                DisplayDetails(Firstname, Lastname, email, password) 
                currentEmployee = [Firstname, Lastname,email, password]   
                employeeDetails.append(currentEmployee)
        break
    
Add_employee()
Resp = input("Add another employee?Y/N:>>")   
if Resp == str("y" or "Y"):
    Add_employee()
else:
    print("Ok thanks")

print(employeeDetails)
exit()

    #Employee details cache




    #print(employeeDetails)
    #print(currentEmployee)
