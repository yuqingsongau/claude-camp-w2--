import re
def count_words(text: str) -> dict:
    """统计文本中每个单词出现的次数，忽略大小写"""
    # 转小写，去除大小写差异
    text = text.lower()

    # 用正则提取单词（只保留字母、数字、下划线组成的单词）
    words = re.findall(r"[a-zA-Z']+", text)

    # 用字典存储统计结果
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def sort_word_count(word_count: dict):
    """按出现次数从高到低排序，返回列表 [(word, count), ...]"""
    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)


def print_result(sorted_words):
    """格式化打印结果"""
    print(f"{'单词':<15}{'出现次数'}")
    print("-" * 25)
    for word, count in sorted_words:
        print(f"{word:<15}{count}")


def main():
    print("=== 文本词频统计器 ===")
    text = input("请输入一段文字：\n")

    word_count = count_words(text)
    sorted_words = sort_word_count(word_count)

    print("\n统计结果（按出现次数从高到低排序）：\n")
    print_result(sorted_words)


if __name__ == "__main__":
    main()