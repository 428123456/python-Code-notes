def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False
#测试字符串和数字
print(is_number('foo'))
print(is_number('1'))
print(is_number('1.3'))

#测试unicode
#阿拉伯语 5
print(is_number('。'))
#中文数字
print(is_number('四'))
#符号
print(is_number('@'))
