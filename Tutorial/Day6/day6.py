i=16
if(i<20):
    print("good boy")
    if(i>15):
        print("okk next best luck")
    elif 5<i<10:
        print(f"{i}")
    else:
        print("go")
else:
    print("bye bye")
age=int(input("enter the value"))
if 18<age<60:
    print("go to vote")
    if 20<age<25:
        print("blood donation")
    elif 25<age<55:
        print("election")
    else:
        print("bye")
else:
    print(f"you are{age} thats way you are not eligible")
like=0
dislike=0
like+=1
click=dislike
if click==like:
    like=like+1
    print(like)
elif click==dislike:
    lie=like-1
    print(like)
else:
    print("kuch to karo")
time="night"
sleepy="sleep"
watching="rs"
if time=="night" and sleepy=="sleep" and watching=="movie":
    print("watch movie")
elif time=="night" and sleepy=="sleep" and watching=="comedy show":
    print("watch")
else:
    print("go to bed")
product_price=int(input("enter the amount"))
if product_price>1000:
    print(f"the price of product after removing discount{product_price*0.7}")
else:
    print(f"the price of product after removing discount{product_price*0.8}")