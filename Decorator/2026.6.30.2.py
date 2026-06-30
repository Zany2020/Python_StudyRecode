import functools

#装饰器的作用：不修改原有函数内部代码，给函数「额外增加通用功能」
def log_exec(level = "INFO"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] 开始执行 {func.__name__}")
            
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                print(f"[{level}] {func.__name__} 执行异常：{e}")
                raise
            
            print(f"[{level}] {func.__name__} 执行完成，返回值：{result}")
            return result
        return wrapper
    return decorator

#写 @log_exec(xxx) 这一行代码的时候，就会立刻先执行外层装饰器函数
#写 add(10,20) 调用业务函数时，才会执行最内层 wrapper 包装逻辑
@log_exec(level = "DEBUG")
def add(a, b):
    return a+b
@log_exec()
def divide(a, b):
    return a/b

if __name__ == "__main__":
    add(10, 20)
    print("原函数名：", add.__name__)  # 不加functools.wraps会显示wrapper
    
    try:
        divide(10, 0)
    except ZeroDivisionError:
        pass
