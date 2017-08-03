# -*- coding: UTF-8 -*-   
#导入sys模块
from  sys  import  argv

#解包argv
script,  filename =  argv

#打开文件
txt =  open ( filename )

#输入
print  "Here's  your  file  %r:" % filename
#执行read命令
print  txt.read()
txt.close()

#输入
print  "Type  the  filename  again:" 
#赋值
file_again =  raw_input(">  ") 

#赋值
txt_again =  open(file_again) 

#执行read命令
print  txt_again.read()
txt_again.close()