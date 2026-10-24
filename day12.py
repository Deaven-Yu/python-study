while True:
    try:
        age =int(input("请输入年龄："))
        if age < 0:
            print("年龄不能小于 0 。")
        elif age >120:
            print("年龄看起来不合理 。 ")
        else:
            print(f"你的年龄是：{age}")
            break
    except ValueError:
        print("输入错误，请输入数字 。 ")

while True:
    try:
        weight = float(input("请输入体重："))
        if weight <= 0:
            print("体重必须大于 0 。")
        elif weight > 500:
            print("体重数据看起来不合理。")
        else:
            print(f"记录成功:{weight}kg")
            break
    except ValueError:
        print("请输入数字 。 ")
    finally:
        print("本次输入结束。")