from random import randint

def generate_number(min_num, max_num):
    try:
        return randint(min_num, max_num)
    except Exception as e:
        raise Exception(f"Error while generating the number. {e}")

def main():
    while True:
        try:
            user_range_start = int(input("Enter the minium number: "))
            user_range_end =  int(input("Enter a max number : "))
            generated_number = generate_number(user_range_start, user_range_end)
            print(f"The Number is {generated_number}")
        except ValueError as ve:
            print(f"Input error {ve}")
        except Exception as e:
            print(f"Error: {e}")
        user_choice = input("Enter 1 if you want to continue. \nEnter 0 if you want to Exit \n")
        match user_choice : 
            case "1":
                continue
            case "0":
                break
            case _:
                print("Invalid choice")
        

if __name__ == "__main__":
    main()