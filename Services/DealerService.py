class DealerService:
    __dealer_list__ = []

    def add(self, dealer):
        self.__dealer_list__.append(dealer)
        return True

    def get_dealers(self):
        return self.__dealer_list__

    def get_all_cars_in_dealer(self, dealer):
        return (self.__dealer_list__[self.__dealer_list__.index(dealer)]).cars

    def add_car_in_dealer(self, dealer, car):
        cars = (self.__dealer_list__[self.__dealer_list__.index(dealer)]).cars
        cars.append(car)

    def get_dealers_where_car_available(self, car_obj):
        result_dealer = []
        for dealer in self.__dealer_list__:
            for car in dealer.cars:
                if car == car_obj:
                    result_dealer.append(dealer)

        return result_dealer

    def authenticate(self, login):
        for dealer in self.__dealer_list__:
            if dealer.username == login.username and dealer.password == login.password:
                return dealer
