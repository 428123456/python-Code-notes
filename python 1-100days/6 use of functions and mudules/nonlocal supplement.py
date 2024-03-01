def outer_function():
    outer_var = 10

    def inner_function():
        nonlocal outer_var
        outer_var = 20
        print("内部函数修改后的外部变量值：", outer_var)

    inner_function()
    print("外部函数中的变量值：", outer_var)

outer_function()
