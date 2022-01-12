class Dealer:
    def __init__(self, company_name, mobile_number, address, username, password):
        self.company_name = company_name
        self.mobile_number = mobile_number
        self.address = address
        self.cars = []
        self.username = username
        self.password = password

    def add_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars
