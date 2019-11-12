"""
测试员工的增删改查
"""
# 导包
import logging
import unittest
import requests

# 创建测试类
import app
from api.emp_api import EmpCRUD


class Test_Emp(unittest.TestCase):

    # 初始化函数
    def setUp(self) -> None:
        self.session = requests.session()
        self.emp_obj = EmpCRUD()

    # 资源加载函数
    def tearDown(self) -> None:
        self.session.close()

    # 测试函数1-增
    def test_add(self):
        logging.warning('增加员工信息')
        #请求业务
        response=self.emp_obj.add(self.session,username='sqas12345',mobile='17611212134')
        print('员工响应结果',response .json())
        #断言业务
        #直接执行该测试函数失败，为什么
        #原因：限制性登陆操作，还需提交银行卡（token）
        #解决：使用测试套件套件组织接口的执行程序
        #核心步骤：token的提取
            #token的提交
        #新增员工的ID
        id=response.json().get('data').get('id')
        app.USER_ID=id
        print('新增员工的ID',id)
        self.assertEqual(True,response.json().get('success'))
        self.assertEqual(10000,response.json().get('code'))
        self.assertIn('操作成功',response.json().get('message'))

    # 测试函数1-改
    def test_update(self):
        logging.warning('修改的员工信息')
        response1 = self.emp_obj.update(self.session,app.USER_ID,'gangtie')
        print('修改员工响应结果', response1.json())
        self.assertEqual(True, response1.json().get('success'))
        self.assertEqual(10000, response1.json().get('code'))
        self.assertIn('操作成功', response1.json().get('message'))

    # 测试函数1-查
    def test_get(self):
        logging.info('查看员工信息')
        response2=self.emp_obj.get(self.session,app.USER_ID)
        print('查看的信息',response2.json())
        self.assertEqual(True, response2.json().get('success'))
        self.assertEqual(10000, response2.json().get('code'))
        self.assertIn('操作成功', response2.json().get('message'))

    # 测试函数1-删
    def test_delete(self):
        logging.warning('删除员工的信息')
        response3=self.emp_obj.delete(self.session,app.USER_ID)
        print('删除的信息', response3.json())
        self.assertEqual(True, response3.json().get('success'))
        self.assertEqual(10000, response3.json().get('code'))
        self.assertIn('操作成功', response3.json().get('message'))
