"""
封装类：
 封装请求函数(只有一个登陆函数)
"""
import app


class Login:
    #调用初始化函数，封装URL
    def __init__(self):
        self.login_url=app.BASE_URL+'/api/sys/login'
    # 编写登录函数
    def login(self,session,mobile,password):
        my_login={"mobile":mobile,
                  "password": password

        }
        return session.post(self.login_url,json=my_login)
    