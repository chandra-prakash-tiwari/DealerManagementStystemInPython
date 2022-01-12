class CarService:
    __car_list__ = []

    def add(self, car):
        self.__car_list__.append(car)
        return True

    def get_cars(self):
        return self.__car_list__

    def get_car_under_price(self, amount):
        result_list = []
        type(amount)
        for i in self.__car_list__:
            if i.base_price < amount:
                result_list.append(i)

        return result_list
