def is_palindrome(num):
    '''判断一个属时不是回文数'''
    temp = num 
    total = 0
    while temp > 0:
        total = total *10 + temp % 10
        temp //= 10
        return total == num
