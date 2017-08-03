# -*- coding: utf-8-8 -*-??
#创建函数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
    print "We can just give the function numbers directly:"

#赋值
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
#赋值
amount_of_cheese = 10
#赋值
amount_of_crackers = 50

#赋值
cheese_and_crackers(amount_of_cheese, amount_of_cheese)


print "We can even do math inside too:"
#赋值
cheese_and_crackers(10 + 20, 5 +6)


print "And we can combine the two, variables and math:"
#赋值
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)