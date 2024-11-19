import json
from datetime import datetime

# 保存数据的文件路径
PARTIAL_DATA_FILE = "partialTaskData.json"
ALL_DATA_FILE = "allTaskData.json"



def load_existing_data(file_path):
    """加载现有数据，如果文件不存在或为空，则返回空列表"""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(file_path, data):
    """将数据保存到文件"""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def add_data_to_file(data, type = 0):
    """将新数据插入文件，避免重复"""
    if type == 0:
        existing_data = load_existing_data(PARTIAL_DATA_FILE)
    else:
        existing_data = load_existing_data(ALL_DATA_FILE)


    # 检查重复的条件：username 和 selectedJobs 完全匹配
    for record in existing_data:
        if record["username"] == data["username"] and record["selectedJobs"] == data["selectedJobs"]:
            print("数据重复，跳过插入")
            return({"status": "error", "message": "已提交任务，正在打卡"})

    # 添加时间戳并插入新数据
    data["timestamp"] = datetime.now().isoformat()
    existing_data.append(data)

    # 保存到文件
    if type == 0:
        save_data(PARTIAL_DATA_FILE, existing_data)
        return({"status": "success", "message": "部分打卡成功"})

    else:
        save_data(ALL_DATA_FILE, existing_data)
        return({"status": "success", "message": "打卡成功，请耐心等待"})
