import json

FILENAME = "todos.json"

def load_todos():
    """程序启动时加载本地数据，文件不存在则返回空列表"""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    """每次修改后保存到本地"""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add_todo(todos):
    task = input("请输入待办内容：")
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"已添加：{task}")

def complete_todo(todos):
    show_todos(todos)
    if not todos:
        return
    try:
        idx = int(input("输入要完成的编号：")) - 1
        todos[idx]["done"] = True
        save_todos(todos)
        print("已标记完成！")
    except (ValueError, IndexError):
        print("编号无效")

def show_todos(todos):
    if not todos:
        print("暂无待办事项")
        return
    for i, t in enumerate(todos, 1):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['task']}")

def main():
    todos = load_todos()
    while True:
        print("\n1.添加待办 2.完成待办 3.查看清单 4.退出")
        choice = input("选择操作：")
        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            complete_todo(todos)
        elif choice == "3":
            show_todos(todos)
        elif choice == "4":
            break
        else:
            print("无效输入")

if __name__ == "__main__":
    main()