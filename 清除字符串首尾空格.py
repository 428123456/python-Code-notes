#清除字符串首尾空格
original_string = " 这是一个带有空格的字符串"
original_string = original_string.strip()
print(original_string)

#如果字符串有/n等，只想删除空格：
my_string = " /npython"
print(my_string.strip(" "))

#正则表达式清除字符串
import re
my_string = "hello python"
output = re.sub(r'^\s+|\s+$', '', my_string)

print(output)


#lstrip()--删除字符串开头的空格
#rstrip()--删除字符串末尾的空格


original_string = " 这是一个带有空格的字符串" 
left_stripped_string = original_string.lstrip() #删除开头空格
right_stripped_string = original_string.rstrip() #删除结尾空格

print(left_stripped_string)
print(right_stripped_string)