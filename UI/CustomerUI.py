from UI.AdminUI import ShowCars, ShowDealers


def CustomerUI(dealer_service, car_service):
    next_command = int(input("press the given number:"
                             "\n\t\t\t1. View all cars"
                             "\n\t\t\t2. Get quotation"))

    if next_command == 1:
        ShowCars(car_service.get_cars())
    elif next_command == 2:
        query = QuotationQueryUI()
        car_under_budget = car_service.get_car_under_price(query.budget)
        ShowCars(car_under_budget)
        car_select = int(input("Enter sl no to select car for quotation neither other number"))
        if 0 < car_select <= len(car_under_budget):
            dealer = dealer_service.get_dealers_where_car_available(car_under_budget[car_select - 1])
            ShowDealers(dealer)
            dealer_select = int(input("enter dealer sl no"))
            if 0 < dealer_select <= len(dealer):
                print("______________________________________________________________")
                print("Quotation Document")
                print("Customer Name: ", query.customer_name)
                print("Car Model: ", car_under_budget[car_select - 1].name)
                print("Price: ", car_under_budget[car_select - 1].base_price)
                print("Dealer: ", dealer[dealer_select - 1].company_name)
                print("Contact Details: ", dealer[dealer_select - 1].mobile_number)
                print("Address: ", dealer[dealer_select - 1].address)
                print("______________________________________________________________")
    else:
        CustomerUI(dealer_service, car_service)


def QuotationQueryUI():
    return QuotationQuery(input("Enter Customer Name: "), int(input("Budget: ")))

class QuotationQuery:
    def __init__(self, customer_name, budget):
        self.customer_name = customer_name
        self.budget = budget