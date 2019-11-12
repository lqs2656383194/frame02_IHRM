"""
框架搭建：
  核心 api+case+data
      api：封装请求业务
      case：集成unittest实现，调用api以及参数化解析data
      data：封装测试数据
  报告：report+tools+run——suite.py
       report：保存测试报告
       tools：封装工具文件
       run—suite：组织测试套件
  配置:app.py
  APP：封装程序敞亮以及配置信息
  日志：log
  app.py的封装数据
"""
#封装接口的URL前缀
import os
import logging
import logging.handlers
BASE_URL='http://182.92.81.159'
#封装项目路径
FILE_PATH=os.path.abspath(__file__)
PRO_PATH=os.path.dirname(FILE_PATH)

# print('动态获取的绝对路径',PRO_PATH)
#预期允许让其他文件调用token，可以扩大token的作用域（将token）

#日志模块实现：
#配置日志，默认的日志配置不能满足需求
def my_log_config():
    #获取日志的对象
    logger=logging.getLogger()
    #配置日志的级别--info以上
    logger.setLevel(logging.INFO)
    #输出到控制台
    th=logging.StreamHandler()
    #输出到文件
    sh=logging.handlers.TimedRotatingFileHandler(PRO_PATH+'/log/hello.log',
                                                 when='h',
                                                 interval=12,
                                                 backupCount=10,
                                         encoding='utf-8')
    #配置输出格式--年月日时分秒级别 函数行号
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    #组织配置并添加进日志对象
    th.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.addHandler(th)
    logger.addHandler(sh)
#调用，在需要的位置调用日志的输出
# my_log_config()
# logging.info('hello python')
#需求 ：微测试类的测试函数添加日志输出
#实现：
#步骤：1、包下的__init__.py 初始化日志配置
  # import app
  # app.my_log_config()
  #
  # 步骤：在测试函数中调用logging.xxx('日志信息')

TOKEN= None
USER_ID= None



