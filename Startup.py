from Services.CarService import CarService
from Services.DealerService import DealerService
from UI.AdminUI import CreateAdminUI, AdminUI
from UI.CustomerUI import CustomerUI
from UI.DealerUI import DealerUI
from UI.LoginUI import LoginUI

def Startup():
    UI()


def UI():
    admin = None
    currentuser = None
    while True:
        print(" W e l c o m e   i n   T a t a    M o t o r s ! ! ! ")
        if admin == None:
            admin = CreateAdminUI()
            dealer_service = DealerService()
            car_service = CarService()
            continue
        else:
            if currentuser == None:
                usertype = int(input("You are a: \n\t\t 1. Admin\t\t 2. Dealer\t\t 3. Customer\t\t4. Exit"))
                if usertype == 1:
                    login_input = LoginUI()
                    if login_input.username == admin.username and login_input.password == admin.password:
                        currentuser = admin.username

                    else:
                        print("Please enter correct credentials")
                        continue
                elif usertype == 2:
                    authenticate = dealer_service.authenticate(LoginUI())
                    if authenticate is not None:
                        currentuser = authenticate
                        if DealerUI(dealer_service, car_service, currentuser) == "logout":
                            currentuser = None
                    else:
                        print("Please enter correct credentials")
                else:
                    CustomerUI(dealer_service, car_service)

            elif currentuser == admin.username:
                if AdminUI(dealer_service, car_service) == "logout":
                    currentuser = None
            else:
                if DealerUI(dealer_service, car_service, currentuser) == "logout":
                    currentuser = None


#Startup()

def pow(b, p):
    y = b ** p
    return y


def square(x):
    a = pow(x, 2)
    return a


n = 5
result = square(n)
print(result)