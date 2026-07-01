from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

#FastAPI 服务实例
app = FastAPI(title = "智能设备管理接口", description = "RESTFUL 入门练习项目")
#给全局服务添加中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#允许所有域名跨域访问
    allow_credentials=True,
    allow_methods=["*"],# 允许所有 HTTP 请求方法
    allow_headers=["*"],# 允许所有请求头
)

#=================模拟数据库（内存存储

fake_user = { "admin:" "123456"}
fake_devices = {
    {"id": 1, "brand": "xiaomi", "model": "xiaomi14", "user": "akane", "battery_level": "80" },
    {"id": 2, "brand": "黑鲨", "model": "BlackShark 5 Pro", "user": "小刚", "battery_level": 100}
}

valid_tokens = {"test_token_abc123": "admin"}

#=======================请求体数据模型
class DeviceCreate(BaseModel):
    """新增设备的请求体格式：前端传的 JSON 必须符合这个结构"""
    brand: str
    model: str
    user: str
    battery_level: int

class DeviceUpdate(BaseModel):
    """修改设备的请求体格式"""
    brand: Optional[str] = None
    model: Optional[str] = None
    user: Optional[str] = None
    battery_level: Optional[int] = None

class LoginRequest(BaseModel):
    """登录请求体"""
    username: str
    password: str
    
# ========== 知识点3：Token 鉴权工具函数 ==========
def verify_token(authorization: str) -> str:
    """校验请求头中的 Token，返回用户名；校验失败抛 401 异常"""
    if not authorization or not authorization.startswith("Bearer "):
        #标准鉴权格式必须以 Bearer  开头
        raise HTTPException(status_code=401, detail="未提供有效鉴权凭证")
    token = authorization.split(" ")[1]
    #split(" ")：按空格把字符串切成列表
    
    if token not in valid_tokens:
        raise HTTPException(status_code=401, detail="Token 无效或已过期")
    return valid_tokens[token]
    
# ===================== 接口部分 =====================
# ========== 1. 登录接口：获取 Token ==========
@app.post("/api/login", summary = "用户登录，获取Token")
def login(req: LoginRequest, fake_users=None):
    if req.username not in fake_users or fake_users[req.username] != req.password:
        raise HTTPException(status_code=400, detail="用户名或密码错误")
    
    return {
        "code": 200,
        "msg": "登录成功",
        "data": {
            "token": "test_token_abc123",
            "username": req.username
            }
    }
    
# ========== 2. 查询设备列表 ==========
@app.get("/api/devices", summary = "查询设备列表")
def get_device_list(authorization: str = Header(None)):
    verify_token(authorization)
    return {
        "code": 200,
        "msg": "success",
        "data": fake_devices
    }
    
#========== 3. 查询单个设备 ==========
@app.get("/api/device/{device_id", summary = "查询单个设备详情")
def get_device(device_id: DeviceCreate, authorization: str = Header(None)):
    verify_token(authorization)
    for dev in fake_devices:
        if dev["id"] == device_id:
            return {"code": 200, "msg": "success", "data": dev}
        raise HTTPException(status_code=404, detail="设备不存在")
    
# ========== 4. 新增设备 ==========
@app.post("/api/devices", status_code=201, summary="新增设备")
def create_device(device: DeviceCreate, authorization: str = Header(None)):
    verify_token(authorization)
    # 生成新ID
    new_id = max(d["id"] for d in fake_devices) + 1 if fake_devices else 1
    new_device = {"id": new_id, **device.dict()}
    fake_devices.append(new_device)
    return {
        "code": 201,
        "msg": "设备创建成功",
        "data": new_device
    }
    
# ========== 5. 修改设备 ==========
#只改 name，原有其他数据保留不变。

@app.put("/api/devices/{device_id}", summary="修改设备信息")
def update_device(device_id: int, device: DeviceUpdate, authorization: str = Header(None)):
    verify_token(authorization)
    for dev in fake_devices:
        if dev["id"] == device_id:
            # 更新非空字段
            
            #把前端传参的 Pydantic 模型，转换成普通字典，
            #加了 exclude_unset=True：只得到 {"name":"新设备"}
            update_data = device.dict(exclude_unset=True)
            dev.update(update_data)
            #字典自带 update() 方法，用键值对，覆盖更新 dev 字典里对应字段
            return {"code": 200, "msg": "修改成功", "data": dev}
    raise HTTPException(status_code=404, detail="设备不存在")

# ========== 6. 删除设备 ==========
@app.delete("/api/devices/{device_id}", status_code=204, summary="删除设备")
"""/api/devices/{device_id}是接口地址，{device_id} 是路径参数："""
def delete_device(device_id: int, authorization: str = Header(None)):
    """
    对应知识点：
    - HTTP 方法：DELETE，删除资源
    - 状态码：删除成功返回 204 No Content（无响应体）
    """
    verify_token(authorization)
    global fake_devices
    for i, dev in enumerate(fake_devices):
        if dev["id"] == device_id:
            del fake_devices[i]
            return  # 204 状态码不需要返回内容
    raise HTTPException(status_code=404, detail="设备不存在")
    
    
    
    
    

