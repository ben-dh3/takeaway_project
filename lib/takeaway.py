class Takeaway:

    def __init__(self):
        self.menu = [
        {'Chicken Katsu Curry': 8.40}, 
        {'Vegetable Yakisoba': 7.80}
        ]
        self.order_list = []


    def order(self, dish, quantity):
        for i in range(0,len(self.menu)):
            for key,value in self.menu[i].items():
                if dish == key:
                    price = value*quantity
                    self.order_list.append({key: price})
        return self.order_list

    def calculate_total(self):
        total = 0
        for i in range(0,len(self.order_list)):
            for value in self.order_list[i].values():
                total += value
        self.order_list.append({'Total Cost': total})
        return self.order_list