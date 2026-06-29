import time

class CodeTimer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        cost = time.time() - self.start_time
        print(f"代码块执行耗时：{cost:.4f} 秒")
        return False
    
if __name__ == "__main__":
    with CodeTimer():
        total = 0
        for i in range(1000000):
            total += 1
        print(f"计算结果：{total}")
