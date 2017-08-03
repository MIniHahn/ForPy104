name =  'mini'
age =  17 #  not a  lie
height =  64 #  inches

weight =  120 #  lbs
eyes =  'Black'
teeth =  'White'
hair =  'Black'

print  "Let's  talk  about  %r." %  name 
print  "She's  %r  inches  tall." % height 
print  "She's  %f  pounds  heavy." % weight
print  "Actually  that's  heavy." 
print  "She's  got  %s  eyes  and  %s  hair." % (eyes,  hair) 
print  "Her  teeth  are  usually  %s depending  on  the  coffee." %  teeth 

#  this  line  is  tricky,  try  to  get  it  exactly right 
print  "If I  add  %d,  %d,  and  %d I  get  %d." % ( 
age,  height, weight, age +  height +  weight)