num = int(input("Enter the  number to Know the day between 1-7 : "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Thursday")
    case 4:
        print("Wednesday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Ek kaam shi se na hota ,\n kahe the na 1-7 ke bich me koi value do")