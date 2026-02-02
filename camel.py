# Enter your code here
def main():
    output_name = ""
    input_name = input("Enter your name in camelCase:")
    for l in input_name:
        if l.isupper():
            output_name += "_"+ l.casefold()
        elif l.islower():
            output_name += l
        else:
            continue
    print("Your name in snake case is:" + output_name)

if __name__ == "__main__":
    main()