class ConfigError(Exception):
    #Exception 是 Python 内置通用异常父类
    #配置相关基类
    pass
class ConfigNotFoundError(ConfigError):
    """配置文件不存在异常"""
    pass
class ConfigEmptyError(ConfigError):
    """配置文件内容为空异常"""
    pass

def load_user_config(file_path):
    if isinstance(file_path, str) or len(file_path.strip()) == 0:
        raise ValueError("文件路径参数非法，必须是非空字符串")
    
    try:
        #核心代码
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            
    except FileNotFoundError as e:
        raise ConfigNotFoundError(f"配置文件 {file_path} 不存在") from e
    else:
        if len(content) == 0:
            raise ConfigEmptyError("配置文件内容为空")
        return content
    finally:
        #无论是否报错一定执行
        print("配置读取流程结束")
        
if __name__ == "__main__":
    try:
        config = load_user_config("config.txt")
        print(f"读取成功：{config}")
    except ConfigNotFoundError as e:
        print(f"【业务异常】{e}")
    except ConfigEmptyError as e:
        print(f"【业务异常】{e}")
    except ValueError as e:
        print(f"【参数异常】{e}")
    except Exception as e:
        print(f"【兜底异常】未知错误：{e}")