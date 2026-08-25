import random as r

c=[True,False]

    
cart1={"name":"milk","price":r.randint(150,300),"availability":r.choice(c)}
cart2={"name":"egg","price":r.randint(150,637),"availability":r.choice(c)}
cart3={"name":"bread","price":r.randint(173,224),"availability":r.choice(c)}
cart4={"name":"rice","price":r.randint(150,300),"availability":r.choice(c)}
carts=[cart1,cart2,cart3,cart4]
edit={"cart1":cart1,"cart2":cart2,"cart3":cart3,"cart4":cart4}
def check (item):
    print(item["name"],item["price"],item["availability"])
    if item["availability"]:
        if item["price"]<=200:
            print("okay its affordable ")
        else:
            print ("i cant buy it")
    else:
        print("okay I'll try else where")
for item in carts:
    check(item)
while True:
    while True:
        try:
            choice=int(input("1.input 1 to edit a cart\n"))
            break
        except:
            print("invalid input\n")
        continue
    if choice==1:
        the_cart=input("input the name of the cart you want to edit")
        if the_cart in edit:
            print(the_cart)
        
