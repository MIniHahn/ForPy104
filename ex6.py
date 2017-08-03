#给x赋值
x =  "There  are  %d  types  of  people." % 10
#给binary赋值
binary =  "binary"
#给do_not赋值
do_not =  "don't"
#给y赋值
y =  "Those  who  know  %s  and  those  who %s." %  (binary,  do_not)

#输出x
print x
#输出y
print y

print  "I  said:  %r." % x 
print  "I  also  said:  '%s'." % y 

#给hilarious赋值
hilarious =  False 
#给joke_evaluation赋值
joke_evaluation =  "Isn't  that  joke  so funny?!  %r" 

#是右边变量带到字符串中
print  joke_evaluation %  hilarious 

#给w赋值
w =  "This  is  the  left  side  of..."
#给e赋值
e =  "a  string  with a  right  side." 

#输出w和e 因为字符串和字符串可以相加
print w + e