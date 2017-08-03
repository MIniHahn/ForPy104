#有100辆车
cars =  100
#每辆车有4个座位
space_in_a_car =4.0


#有30位司机
drivers =  30
#90位乘客
passengers =  90
#不被开的车为100-30=70辆
cars_not_driven =  cars -  drivers
#被开的车有30辆
cars_driven =  drivers
#可坐人数为30*4.0=120.0人
carpool_capacity =  cars_driven * space_in_a_car
#平均每90/30=3人坐一辆车
average_passengers_per_car = passengers /  cars_driven


print  "There  are",  cars,  "cars available."
print  "There  are  only",  drivers, "drivers  available." 
print  "There  will  be", cars_not_driven,  "empty  cars  today."
print  "We  can  transport", carpool_capacity,  "people  today." 
print  "We  have",  passengers,  "to carpool  today."
print  "We  need  to  put  about", average_passengers_per_car,  "in  each  car."