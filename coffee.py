#Your code goes here
coffee_price = 75

def main():
    print("The price of the cofee is 75p!")
    print("The machine only accepts 50p, 20p, 10p and 5p coins")
    inserted_money = 0
    while inserted_money < coffee_price:
        print(f"You need to insert {coffee_price - inserted_money}p more")
        coin = input("Insert a coin")
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

        
