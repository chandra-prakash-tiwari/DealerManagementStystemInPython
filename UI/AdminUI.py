from Models.AdminUser import AdminUser
from Models.Car import Car
from Models.Dealer import Dealer


def AdminUI(dealer_service, car_service):
    next_command = int(input("press the given number:"
                             "\n\t\t\t1. Create Dealer"
                             "\t\t\t2. View all Dealers"
                             "\t\t\t3. Create new Car Model"
                             "\t\t\t4. View all cars details"
                             "\t\t\t5. Logout"))
    if next_command == 1:
        dealer_service.add(AddDealerUI())
    elif next_command == 2:
        ShowDealers(dealer_service.get_dealers())
    elif next_command == 3:
        car_service.add(AddCarUI())
    elif next_command == 4:
        ShowCars(car_service.get_cars())
    elif next_command == 5:
        return "logout"
    else:
        print("Enter correct value")
        AdminUI()


def AddDealerUI():
    return Dealer(input("Dealer company name: "), input("Contact details: "), input("Address: "), input("UserName: "),
                  input("Password: "))


def AddCarUI():
    return Car(input("Name: "), int(input("Base Price: ")))


def ShowDealers(dealers):
    if len(dealers) > 0:
        for dealer in dealers:
            print("-------------------------------------------------------------")
            print("Name: ", dealer.company_name)
            print("Contact Details: ", dealer.mobile_number)
            print("Address: ", dealer.address)
            print("-------------------------------------------------------------")
    else:
        print("No dealer found!!")


def ShowCars(cars):
    if len(cars) > 0:
        i = 1
        for car in cars:
            print("-------------------------------------------------------------")
            print("Sl no: ", i)
            print("Name: ", car.name)
            print("Base Price: ", car.base_price)
            print("-------------------------------------------------------------")
            i += 1
    else:
        print("No car record found")


def CreateAdminUI():
    print("First setup your company credential for future use")
    admin = AdminUser()
    admin.username = input("Enter your username: ")
    admin.password = input("Enter your password: ")
    return admin
