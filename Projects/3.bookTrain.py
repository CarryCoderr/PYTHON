startTrainLocation="BSB"
endTrainLocation="RMM"
trainDepartureTime="8:00,10-05-2023"
trainArrivalTime="22:00,11-05-2023"
totalDistanceAndTime="2463 km-1day 14h"
trainSeat="2AC B-10"
bookCost=2000
upicharge=20
atmcharge=30
userBalance=20000
userAtmId="252534"
UserAtmPin="4545"
userUpiId="carrycoder@okcc"
userUpiPin="363636"
print()
print("----------Carrycoder Booking Platform me Apka svagat hai-----")
print()
userEnterStartLocation=input("Enter your start Location :")
if userEnterStartLocation.upper()==startTrainLocation:
    userEnterEndLocation=input("Enter your end Location")
    if userEnterEndLocation.upper()==endTrainLocation:
        dateandtimeD=trainDepartureTime.split(',')
        dateandtimeE=trainArrivalTime.split(',')
        totalDistanceAndTime=totalDistanceAndTime.split('-')
        print("start Location  End Location  Start Date   End Date Distance & Time  Cost  ")
        print()
        print(f"VARANASI({startTrainLocation})  RAMESWARAM({endTrainLocation}) {dateandtimeD[0], dateandtimeD[1]}  {dateandtimeE[0] ,dateandtimeE[1]}")
        print()
        YesNo=input("want to book this Train(y/n)")
        if YesNo=="y"or YesNo=="yes" or YesNo=="Yes":
            userName=input("enter the your Name :")
            if len(userName)==0:
                print("Name Required")
            else:
                userAge=input("enter the Age :")
                if userAge.isdigit():
                    if int(userAge)<10:
                        print("you are not allow to traval")
                    else:
                        print(f"UPI Payment is{upicharge} and ATm is{atmcharge}")
                        print()
                        choice=input("choose Payment Method \n for UPI press(u) or for ATM press(a):")
                        if choice=='u' or choice=="U":
                            print(f"Total Payable Amount{bookCost+upicharge}")
                            userEnterUpiId=input("enter Your UPI ID:")
                            if userEnterUpiId==userUpiId:
                                userEnterUpiPin=input("enter your upi pin :")
                                if userEnterUpiPin==userUpiPin:
                                    if userBalance>=(bookCost+upicharge):
                                        print("-----Your ticket Has Been Successfully Book--")
                                        print()
                                        print(f"Name:   {userName}")
                                        print(f"Age :    {userAge}")
                                        print(f" seat :  {trainSeat}")
                                        print(f" PNR  :    121221")
                                        print()
                                        print("(: Thanks for using Carrycoder Booking Platform)")
                                        userBalance-=(bookCost+upicharge)
                                    else:
                                         print("Rupya kaam ahai apka khate me dosta mango")
                                else:
                                    print("apna upi pin hi bhul gaye ?")
                            else:
                                print("ap apni upi id bhul gaye ho")
                        elif choice=='a' or choice=="A":
                            print(f"totalPayable Amount {bookCost+atmcharge}")
                            userEnterAtmId=input("enter your ATM Number :")
                            if userEnterAtmId==userAtmId:
                                userEnterATMpin=input("enter your pin :")
                                if userEnterATMpin==UserAtmPin:
                                    if(userBalance>=(bookCost+atmcharge)):
                                        print("-----Your ticket Has Been Successfully Book--")
                                        print()
                                        print(f"Name:   {userName}")
                                        print(f"Age :    {userAge}")
                                        print(f" seat :  {trainSeat}")
                                        print(f" PNR  :    121221")
                                        print()
                                        print("(: Thanks for using Carrycoder booking Platform)")
                                        userBalance-=(bookCost+upicharge)
                                    else:
                                        print("Apka balance kaam hai ")
                                else:
                                    print("atm pin hi bhul gaye")
                            else:
                                print("phir galat id dal deya")
                        else:
                            print('phir galat value diye aap na')
                else:
                    print("are are invalid")
        elif YesNo=="n" or YesNo=="no" or YesNo=="N0":
            print("thanking for using Carrycoder booking Platform")
        else:
            print()
            print("phir galat value de")
                    
    else:
        
        print("no end Location Found")
else:
    print("no start Location Found")