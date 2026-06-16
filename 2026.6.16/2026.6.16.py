
def count_text(file_path):
    try:#try 包裹可能报错的代码
        with open(file_path, 'r', encoding = 'utf-8') as f:
            content = f.read()

        char_count = len(content)
        line_count = len(content.split())#不带参数 split()自动以所有空白字符切割
        word_count = len(content.splitlines())

        chinese_count = 0
        for char in content:
            if '\u4e00' <= char <= '\u9fff':
                chinese_count += 1
        return{
            "总字符数": char_count,
            "行数": line_count,
            "英文单词数": word_count,
            "中文字数": chinese_count
        }
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    path = input("请输入TXT文件路径：")
    result =  count_text(path)
    if result:
        for k, v in result.items():
            print(f"{k},{v}" )

