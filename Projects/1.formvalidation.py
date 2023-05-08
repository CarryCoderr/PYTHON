#form validation
#data from database or file
userDataName="RamRam"
userName=input("enter Your Name :")
if len(userName)>=15:
    print("Name is Too long")
elif userName==userDataName:
    print("Username Already Exist")
else:
    userpass=input("enter the password :")
    if len(userpass)<8:
        print("Password must be greater than 8 character")
    else:
        userName=userName.rstrip()
        print(len(userName))
        print("Registration Successful")