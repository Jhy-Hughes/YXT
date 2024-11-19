from datetime import datetime
from flask import Flask, request, jsonify
import json
from tokenize import Special
from userSession import UserSession
import jwt
from flask_sqlalchemy import SQLAlchemy
from baseTask import userTaskInfo
from SaveFile import add_data_to_file

admin = 'admin'
adminPassword= '123456'
adminData = {'username': 'admin'}

class baseTask:
    fuwushang: str
    value: str

class userTaskInfo:
    company: str
    username: str
    password: str
    isWhole: bool
    partialTasks: list[baseTask]

    def __str__(self) -> str:
        return f"username: {self.username}, password: {self.password}, company: {self.company}, isWhole:{self.isWhole}, self.pa"



app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin123456'  # 确保这个值是字符串

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # 本地 SQLite 数据库
# 若使用 MySQL 数据库，格式如下
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/dbname'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭警告信息
# db = SQLAlchemy(app)
def generate_token(username):
    # time = time.time() + 24 * 60 * 60
    payload = {
        "username": username
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')



@app.route('/login', methods=['GET'])
def login():

    username = request.args.get('username')
    password = request.args.get('password')

    if username != admin:
        return jsonify({"error": "账号不对"}), 400
    
    if password != adminPassword:
        return jsonify({"error": "密码不对"}), 400


    token = generate_token(username)
    return jsonify({'token': token})

@app.route('/taskList', methods=['GET'])
def get_jobs():
    # 将 jobList 转换为字典列表以便 JSON 序列化
    company = request.args.get('company')
    username = request.args.get('username')

    password = request.args.get('password')

    # username = request.json['username']
    # password = request.json['password']
    user_info = UserSession(company, username, password)
    user_info.login()
    # user_info.startLevelJobs()
    jobs_json = [job.__dict__ for job in user_info.jobMessages]

    return jsonify(jobs_json)


@app.route('/partialTasks', methods=['POST'])
# 入参：委托方+金额
def partialTasks():
    try:
        # 获取请求体中的 JSON 数据
        data = request.get_json()
        
        # 提取字段
        company_name = data.get('companyName')
        username = data.get('username')
        password = data.get('password')
        selected_tasks = data.get('selectedTasks')
        selected_jobs = data.get('selectedJobs')
        total_amount = data.get('totalAmount')
        partial_amount = data.get('partialAmount')

        # 打印接收到的数据
        print("公司名称:", company_name)
        print("用户名:", username)
        print("密码:", password)
        print("选中的任务:", selected_tasks)
        print("选中的工作:", selected_jobs)
        print("总金额:", total_amount)
        print("部分金额:", partial_amount)

        data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M")

        add_message = add_data_to_file(data)

        # 返回成功响应
        return jsonify(add_message), 200

    except Exception as e:
        print("处理请求时出错:", str(e))
        return jsonify({"status": "error", "message": "数据处理失败"}), 500

@app.route('/calculateAmount', methods= ['GET'])
def calculate_amount():
    data = request.get_json()
    
    # 获取请求中的数据
    company_name = data.get('companyName')
    username = data.get('username')
    password = data.get('password')
    user_info = UserSession(company_name, username, password)
    user_info.login()
    # user_info.startLevelJobs()
    for job in user_info.jobMessages:
        user_info.totalMoney += job.jobValue
    
    # 假设根据任务计算金额
    
    # 返回支付需要的数据（这是示例，实际支付数据应由支付平台提供）
    payment_data = {
        'totalAmount': user_info.totalMoney,
        'timeStamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'nonceStr': ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=32)),
        'package': 'prepay_id=1234567890',
        'signType': 'MD5',
        'paySign': 'abcdef1234567890',  # 这个签名由支付平台提供
    }
    
    return jsonify(payment_data)

@app.route('/savePaymentData', methods=['POST'])
def save_payment_data():
    data = request.get_json()
    
    # 获取支付后的数据
    company = data.get('company')
    username = data.get('username')
    password = data.get('password')
    tasks = data.get('tasks')
    total_amount = data.get('totalAmount')
    payment_status = data.get('paymentStatus')
    
    # 保存数据（在本地文件、数据库等保存，示例中存储到文件）
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    payment_record = {
        'timestamp': timestamp,
        'company': company,
        'username': username,
        'password': password,
        'tasks': tasks,
        'totalAmount': total_amount,
        'paymentStatus': payment_status,
    }
    
    # 将数据保存到文件
    result = add_data_to_file(payment_record,1)
    
    return jsonify(result), 200

if __name__ == '__main__':
    # 在应用启动前进行数据爬取
    app.run(debug=True)