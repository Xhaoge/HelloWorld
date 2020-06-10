from flask import render_template
# 导入蓝图程序users 用于构建路由
from . import users

# 首页的访问路由
@users.route('/users')
def users_views():
    return 'welcome to china....'