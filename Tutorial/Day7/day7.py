# Question 1
product_price = int(input("enter the amount"))
if product_price > 3000:
    if product_price == 4000:
        print("Congratulations you get a goa trip")
    print(f"the price of product after removing dicount{product_price*0.8}")
elif product_price >= 2000 and product_price <= 3000:
    if product_price == 2999:
        print("you get a additional gift")
    print(f"the price of product after removing discount{product_price*0.7}")
elif product_price >= 100 and product_price < 2000:
    print(f"the price of product after removing discount{product_price*0.6}")
else:
    print("lets drink the tea")
    print("enjoy")


# Question 2

side = str(input("enter the side"))
per = float(input("enter the per"))
if side == "science":
    if per >= 95 and per < 100:
        print(f"a divison and per{per}")
    elif per >= 80 and per < 95:
        print(f"b divison and per{per}")
    elif per >= 60 and per < 80:
        print(f"c divison and per{per}")
    elif per >= 40 and per < 60:
        print(f"d divison and per{per}")
    else:
        print("fail")
if side == "art":
    if per >= 95 and per < 100:
        print(f"a divison and per{per}")
    elif per >= 80 and per < 95:
        print(f"b divison and per{per}")
    elif per >= 60 and per < 80:
        print(f"c divison and per{per}")
    elif per >= 40 and per < 60:
        print(f"d divison and per{per}")
    else:
        print("fail")
if side == "commerce":
    if per >= 95 and per < 100:
        print(f"a divison and per{per}")
    elif per >= 80 and per < 95:
        print(f"b divison and per{per}")
    elif per >= 60 and per < 80:
        print(f"c divison and per{per}")
    elif per >= 40 and per < 60:
        print(f"d divison and per{per}")
    else:
        print("fail")
