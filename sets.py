# languages = set()
languages = {"english", "mandarin", "spanish", "spanish", "french"}
print(languages)

showroom = {"jaguar", "ford", "toyota", "honda"}
#LENGTH!
showroom_length = len(showroom)
print(showroom_length)
#ADD ONE!
showroom.add("mazda")
print(showroom)
#ADD MORE THAN ONE!
showroom.update({"tesla", "chevy"})
print(showroom)
#DELETE!
showroom.discard("mazda")
print(showroom)
#HOW MANY ARE IN BOTH LISTS?
junkyard = {"corvette", "honda","porsch", "land rover", "lexus", "bmw"}
print(showroom.intersection(junkyard))
#LET'S PUT THEM TOGETHER
lotsofcars = showroom.union(junkyard)
print(lotsofcars)
#DELETE ONCE MORE!
lotsofcars.discard("honda")
print(lotsofcars)