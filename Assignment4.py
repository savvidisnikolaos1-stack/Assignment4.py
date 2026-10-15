cart_total = 131
user_status = "regular"
has_promo_code = True
loyality_points = 71
delivery_city = "თბილისი"#, "ქუთაისი", "ბათუმი", "რეგიონი"
is_account_active = True
discount = 0
#CHecking is account active or mot
if not is_account_active:
    print ("Account is not active")
#What do we have in cart ? Checknig the cart(if not)
#minimum_cost = 0
#if minimum_cost <= 0 : 
#print("Payment declined") - ეს და ზემო ორი ეწერა. შევამჩნიე, რომ შეცდომით მქონდა გამოყვანილი. სულ უარყოფას ბეჭდავდა, ჭეშმარიტიც, რომ ყოფილიყო. უკეთ უნდა გავარკვიო რატომ...
#Discount 
else:
    if user_status == "vip":
        discount = 20
    elif loyality_points >= 500:
        discount = 25
    elif user_status == "regular":
        if has_promo_code or cart_total >= 150:
            discount = 10
 #else: - ეს ეწერა მანამდე, ამის წაშლით მგონი არც არაფერი იცვლება და ზედმეტად მქონდა დამატებული :P
 #discount = 0
    elif user_status == "admin":
        discount = 50
#jamuri datvla
price_after_discount = cart_total - cart_total * discount / 100
#mitanis servisi da fasi
if delivery_city in ["თბილისი"]:
    if price_after_discount >= 100:
        delivery = 0
    else:
        delivery = 5

else:
    delivery = 15
#jami
total = price_after_discount + delivery

#bolo "shtrixi"

print("   < Invoice >   ")
print("Starting price:", cart_total)
print("Discount (%):", discount)
print("Price afte discount:", price_after_discount)
print("Delivery price",":", delivery)
print("Total Price:", total)
