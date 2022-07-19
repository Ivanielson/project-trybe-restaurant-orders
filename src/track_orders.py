import operator


class TrackOrders:
    def __init__(self):
        self.__data = list()
    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.__data)

    def add_new_order(self, customer, order, day):
        self.__data.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        result = {}
        for name, request, _ in self.__data:
            if name == customer:
                if request not in result:
                    result[request] = 1
                else:
                    result[request] += 1
        return max(result.items(), key=operator.itemgetter(1))[0]

    def get_never_ordered_per_customer(self, customer):
        menu = set()
        customer_requests = set()
        for name, request, _ in self.__data:
            menu.add(request)
            if name == customer:
                customer_requests.add(request)
        return menu.difference(customer_requests)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        presence_of_customer = set()
        for name, _, day in self.__data:
            days.add(day)
            if name == customer:
                presence_of_customer.add(day)
        return days.difference(presence_of_customer)

    def get_busiest_day(self):
        result = {}
        for _, _, day in self.__data:
            if day not in result:
                result[day] = 1
            else:
                result[day] += 1
        return max(result.items(), key=operator.itemgetter(1))[0]

    def get_least_busy_day(self):
        result = {}
        for _, _, day in self.__data:
            if day not in result:
                result[day] = 1
            else:
                result[day] += 1
        return min(result.items(), key=operator.itemgetter(1))[0]


# REF: https://www.delftstack.com/pt/howto/python/find-max-value-in-
# dictionary-python/#:~:text=Resultado%3A%20Copy%20key3-,Utilize%20max
# ()%20e%20dict.,%C3%A9%20utilizado%20o%20m%C3%A9todo%20dict.
