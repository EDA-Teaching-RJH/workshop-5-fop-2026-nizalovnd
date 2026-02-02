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

def main():
    print("The price of the cofee is 75p!")
    print("The machine only accepts 50p, 20p, 10p and 5p coins")
    inserted_money = 0
    while inserted_money < coffee_price:
        print(f"You need to insert {coffee_price - inserted_money}p more")
        coin = input("Insert a coin")
        if coin not in accepted_coins:
            print("Invalid coin inserted. Collect rejected coin")
            continue
        coin_val = ""
        for l in coin:
            if l.isnumeric():
                coin_val += l
            else:
                continue
        coin_num = int(coin_val)
        inserted_money += coin_num
        
    if inserted_money == coffee_price:
        print("Enjoy your coffee!")
    elif inserted_money > coffee_price:
        print(f"The change due is {inserted_money - coffee_price}p")
        print("Enjoy your coffee and don't forget your change!")

if __name__ == "__main__":
    main()

        
