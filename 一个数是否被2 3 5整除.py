num = int(input("输入一个数字"))
if num%2 == 0:
    if num%3 == 0:
        if num%5 ==0:
            print("num能同时被2 3 5整除")
        else:
            print("num能被2 3整除,不能被5整除")
    else:
        if num%5 ==0:
            print("num能被2 5整除,不能被3整除")
        else:
            print("num能被2 整除,不能被3 5整除")
else:
    if num%3 == 0:
        if num%5 ==0:
            print("num能同时被 3 5整除,不能被2整除")
        else:
            print("num能被 3整除,不能被2 5整除")
    else:
        if num%5 ==0:
            print("num能被5整除,不能被2 3整除")
        else:
            print("num不能被2 3 5整除")
            
"0被同时整除,负数不能被整除."