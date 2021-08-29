# items
class Bike:
    def __init__(self, type, hou_price, day_price, wee_price, quantity):
        self.type = type
        self.hou_price = hou_price
        self.day_price = day_price
        self.wee_price = wee_price
        self.quantity = quantity


# shop
class Shop:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, bike):
        self.items.append(bike)

    def avai_items(self):
        for item in self.items:
            print(f'Type: {item.type} ')
            print(f'Quantity: {item.quantity} ')
            print(f'Price: ${item.hou_price}/hour - ${item.day_price}/day - ${item.wee_price}/week')
            print()

    def show_bill(self, buy_lst):
        for item in buy_lst:
            product = item[0]
            quantt = int(item[1])
            rent_type = item[2]
            time = item[3]

            if quantt > product.quantity:
                return "We don't have enough bikes for you at the moment. Please reduce the number of bikes you want. Thank you."
            else:
                product.quantity = product.quantity - quantt
                if rent_type == 'hourly':
                    total_cost = product.hou_price * time * quantt
                elif rent_type == 'daily':
                    total_cost = product.day_price * time * quantt
                elif rent_type == 'weekly':
                    total_cost = product.wee_price * time * quantt

            if quantt >= 3:
                total_cost = total_cost * 1.03

            print(f"""
Type: {product.type}
Quantity: {quantt}
Time: {time} {rent_type.replace('ly', '')}s
Total cost: ${total_cost}""")


# Customer
class Customer():
    def __init__(self, name):
        self.name = name
        self.buy_lst = []

    def buy(self, bike, quantity, rent_type, time):
        self.buy_lst.append([bike, quantity, rent_type, time])


# Instance
# Bikes
traditional = Bike('traditional', 3, 12, 30, 20)
professional = Bike('professional', 5, 20, 60, 10)

# Shop
nk_shop = Shop('The Dang Shop')
# Add items
nk_shop.add_items(traditional)
nk_shop.add_items(professional)
# Return
# nk_shop.avai_items()

# Customer

print(f"Welcome to {nk_shop.name}.")
cus = input("What's your name: ")
print(f"Hi {cus}. Hey's what you can do")
cus = Customer(cus)
print("""
Type 1: Show available items at the moment.
Type 2: To select what you want to buy.
Type 3: Finish.""")
while True:
    act = input("What do you want to do: ")
    while act not in '123':
        act = input("Valid Input. Please try again: ")
    if act == '1':
        nk_shop.avai_items()
    if act == '2':
        item = input("What type of bike do you want to rent: ")
        while item != 'traditional' and item != 'professional':
            item = input("Valid Input. Please try again: ")
        if item == 'traditional':
            item = traditional
        else:
            item = professional

        quantity = input("How many bikes do you want: ")
        while quantity not in '0123456789':
            quantity = input("Valid Input. Please try again: ")
        quantity = int(quantity)

        rent_type = input("Do you want to buy it hourly, daily or weekly: ")
        while rent_type != 'hourly' and rent_type != 'daily' and rent_type != 'weekly':
            rent_type = input("Valid Input. Please try again: ")

        time = input("How long do you want to rent it ")
        while time not in '0123456789':
            time = input("Valid Input. Please try again: ")
        time = int(time)

        cus.buy(item, quantity, rent_type, time)
        print("Here's your bill: ")
        print(nk_shop.show_bill(cus.buy_lst))

    if act == '3':
        print("Nice to serve you. Goodbye!")
        break