from UI.AdminUI import ShowCars


def DealerUI(dealer_service, car_service, dealer):
    next_command = int(input("press the given number:"
                             "\n\t\t\t1. View all cars in your company"
                             "\t\t\t2. View all cars in your inventory"
                             "\t\t\t3. Add car in your inventory"
                             "\t\t\t4. Logout"))
    if next_command == 1:
        ShowCars(car_service.get_cars())
    elif next_command == 2:
        ShowCars(dealer_service.get_all_cars_in_dealer(dealer))
    elif next_command == 3:
        all_cars = car_service.get_cars()
        ShowCars(all_cars)
        dealer_service.add_car_in_dealer(dealer, all_cars[int(input("Select sr. number"))-1]) if len(all_cars) > 0 else ""
    elif next_command == 4:
        return "logout"
    else:
        DealerUI(dealer_service, car_service, dealer)