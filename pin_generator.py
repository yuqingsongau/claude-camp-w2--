import random

# PIN 生成器

length = input("请输入PIN码长度: ")

try:
    pin_length = int(length)
    if pin_length <= 0:
        print("长度必须是正整数哦~")
    else:
        pin = "".join(str(random.randint(0, 9)) for _ in range(pin_length))
        print(f"生成的PIN码是: {pin}")
except ValueError:
    print("请输入有效的数字哦~")