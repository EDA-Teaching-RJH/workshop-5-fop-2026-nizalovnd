#Statement of requirements
'''
Functional Requirements:
The system only accepts 50p, 20p, 10p and 5p coins
The output of the change is calculated using integer values, and then outputs using the print function with adding p after the integer.

Non-functional requirements:
The system should reject all invalid entries, including wrong coins denumeration, wrong currency coins and wrong format input.
The system should not crash and disregard the invalid input and continue to ask for more coins to finish paying or the coffee.
'''
#Your code goes here
coffee_price = 75
accepted_coins = [ "50p","20p","10p" ,"5p"]

def get_coin():
    coin = input("Insert a coin")
    if coin not in accepted_coins:
        print("Invalid coin inserted. Collect rejected coin")
        return 0
    coin_val = ""
    for l in coin:
        if l.isnumeric():
            coin_val += l
        else:
            continue
    coin_num = int(coin_val)
    return coin_num

def update_total(current, coin):
    current += coin
    return current

def dispense_product(total_inserted):
    if total_inserted == coffee_price:
        print("Enjoy your coffee!")
    elif total_inserted > coffee_price:
        print(f"The change due is {total_inserted - coffee_price}p")
        print("Enjoy your coffee and don't forget your change!")
        calculate_change(total_inserted - coffee_price)


def calculate_change(amount):
    coin_list = []
    while amount > 0:
        while True:
            if amount - 50 >= 0:
                amount = amount - 50
                coin_list.append(50)
            else:
                break
        while True:
            if amount - 20 >= 0:
                amount = amount - 20
                coin_list.append(20)
            else:
                break
        while True:
            if amount - 10 >= 0:
                amount = amount - 10
                coin_list.append(10)
            else:
                break
        while True:
            if amount - 5 >= 0:
                amount = amount - 5
                coin_list.append(5)
            else:
                break
        
    print(f"Returning: {', '.join(str(l)+"p" for l in coin_list)}")   
        


def main():
    print("The price of the cofee is 75p!")
    print("The machine only accepts 50p, 20p, 10p and 5p coins")
    inserted_money = 0
    while inserted_money < coffee_price:
        print(f"You need to insert {coffee_price - inserted_money}p more")
        coin_num = get_coin()
        inserted_money = update_total(inserted_money, coin_num)
        dispense_product(inserted_money)
        
    

if __name__ == "__main__":
    main()

        
