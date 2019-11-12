import json
import unittest

import requests

import app
from api.login_API import Login
from parameterized import parameterized

from app import PRO_PATH


def read_json_file():
    # 创建一个空列表
    data = []
    with open(PRO_PATH + '/data/login_data.json', encoding='utf-8') as f:
        for i in json.load(f).values():
            mobile = i.get('mobile')
            password = i.get('password')
            success = i.get('success')
            code = i.get('code')
            message = i.get('message')
            ele = (mobile, password, success, code, message)
            data.append(ele)
    return data
    # 解析文件流，将数据追加进列表里


class Test_Login(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.login_obj = Login()

    def tearDown(self) -> None:
        self.session.close()

    @parameterized.expand(read_json_file())
    def test_login(self, mobile, password, success, code, message):
        # print('数据为',mobile, password, success, code, message)
        response=self.login_obj.login(self.session,mobile, password)
        print('登录的响应结果',response.json())
        #断言结果
        self.assertEqual(success,response.json().get('success'))
        self.assertEqual(code,response.json().get('code'))
        self.assertIn(message,response.json().get('message'))
        #编写一个登陆成功的测试函数
    def test_login_success(self):
        #通过提交正向数据发送请求业务
        responses=self.login_obj.login(self.session,"13800000002","123456")
        #断言业务
        print('登陆成功的结果',responses.json())
        self.assertEqual(True, responses.json().get('success'))
        self.assertEqual(10000, responses.json().get('code'))
        self.assertIn('操作成功', responses.json().get('message'))#'f31ff8d3-d542-45ab-82e0-3d38f9406261'
        token=responses.json().get('data')
        print('登录的token：',token)
        app.TOKEN=token