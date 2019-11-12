"""
测试套件
按照需求组合被执行的测试函数
补充说明：
  关于测试套件的组织，接口业务测试中，需要保证测试套件中接口的执行顺序
  合法：逐一添加 不能直接添加类名因为无法保证执行的顺序
增--改--查--删
"""

#导包
import time
import  unittest
#实例化套件对象，组织被执行测试函数
import app
from case.test_IHRM_emp import Test_Emp
from case.test_login_ihrm import Test_Login
from tools.HTMLTestRunner import HTMLTestRunner

suite=unittest.TestSuite()
suite.addTest(Test_Login("test_login_success"))#登陆成功的函数
suite.addTest(Test_Emp("test_add"))#组织员工新增的测试函数
suite.addTest(Test_Emp('test_update'))
suite.addTest(Test_Emp('test_get'))
suite.addTest(Test_Emp('test_delete'))
#执行套件，生成测试报告
with open(app.PRO_PATH +'/report/report.html','wb') as f:
    runner=HTMLTestRunner(f,title='人力资源管理系统测试报告',
                          description='员工模块的增删改查')
    runner.run(suite)