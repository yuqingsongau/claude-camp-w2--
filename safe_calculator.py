def calculator():
    print("简单计算器 (输入 quit 退出)")
    print("支持: + - * /")
    
    while True:
        # 获取第一个数字，或退出指令
        num1_input = input("\n请输入第一个数字 (或输入 quit 退出): ").strip()
        if num1_input.lower() == "quit":
            print("再见！")
            break
        
        try:
            num1 = float(num1_input)
        except ValueError:
            print("❌ 输入的不是有效数字，请重新输入")
            continue
        
        operator = input("请输入运算符 (+ - * /): ").strip()
        if operator not in ("+", "-", "*", "/"):
            print("❌ 不支持的运算符，请输入 + - * / 之一")
            continue
        
        num2_input = input("请输入第二个数字: ").strip()
        try:
            num2 = float(num2_input)
        except ValueError:
            print("❌ 输入的不是有效数字，请重新输入")
            continue
        
        # 执行计算
        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2  # 可能触发 ZeroDivisionError
            
            print(f"✅ 结果: {num1} {operator} {num2} = {result}")
        
        except ZeroDivisionError:
            print("❌ 错误：除数不能为 0")


if __name__ == "__main__":
    calculator()