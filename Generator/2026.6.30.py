def parse_log_file(log_path):
    line_num = 0
    with open(log_path, "r", encoding="utf-8") as f:
        #变量 f 是文件读取对象
        for line in f:
            stripped = line.strip()
            if not stripped:
                #strip() 去除一行首尾的空白：空格、制表符、换行符
                continue #跳过空行
            line_num += 1
            yield f"{line_num}: {stripped}"
            #暂停当前函数执行
            #外部下一次迭代时，代码从这一行后面继续执行，不会从头重跑函数
            

def parse_log_simple(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        return (f"{i+1}: {line.strip()}"
                for i, line in enumerate(f)#同时返回 索引下标 + 元素本身
                if line.strip())

if __name__ == "__main__":
    with open("test.log", "w", encoding="utf-8") as f:
        f.write("2024-01-01 登录成功\n\n")
        f.write("2024-01-01 查询数据\n")
        f.write("  \n")
        f.write("2024-01-01 退出登录\n")
        
    log_gen = parse_log_file("test.log")
    for log_line in log_gen:
        print(log_line)
    
    print("第二次遍历结果：", list(log_gen))