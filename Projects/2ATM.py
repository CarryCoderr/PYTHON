userATMId="252534"
userATMPin="4545"
userBalance=10000
userATMID=str(input("enter the atm number"))
if userATMID.isdigit():
    if userATMId==userATMID:
        userEnterPin=str(input("enter the pin"))
        if userEnterPin.isdigit():
            if userEnterPin==userATMPin:
                userEnterAmount=str(input("enter the amount"))
                if int(userEnterAmount)<=userBalance:
                    userBalance-=int(userEnterAmount)
                    print("please don't forget to collect your Amount \n")
                    print(f"Current Balance is {userBalance}\n")
                    print("(happy to use:)\n")
                    print("please revisit carrycoder bank atm")
                else:
                    print("not enough balance")
            else:
                print("please enter the correct pin")
            
        else:
            print("only digit allow")
        
    else:
        print("your atm Id is wrong")
        
    
else:
    print("only digit allow")