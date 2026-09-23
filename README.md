# Flask Blog

基于 Flask 开发的个人博客系统。

## 项目介绍

本项目是一个个人博客 Web 应用，用于学习和实践 Python Flask 后端开发流程。

项目实现了用户注册登录、文章发布、文章编辑以及内容展示等功能，并完成线上部署。


## 技术栈

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- MySQL
- HTML/CSS
- Gunicorn
- Render

## 功能实现


### 用户模块

- 用户注册
- 用户登录
- 用户状态管理
- 个人信息页面


### 文章模块

- 文章列表展示
- 查看文章详情
- 创建文章
- 编辑文章


## 数据库设计

### User

|字段|说明|
|-|-|
|id|用户ID|
|username|用户名|
|password|密码|
|email|邮箱|


### Article

|字段|说明|
|-|-|
|id|文章ID|
|title|文章标题|
|content|文章内容|
|created_at|创建时间|
|updated_at|更新时间|
|user_id|作者ID|

 ## 项目收获

通过本项目学习：

- Flask 项目结构设计
- Blueprint 模块化开发
- Flask-Login 用户认证
- SQLAlchemy ORM 数据库操作
- Web 应用部署流程

数据关系：User 1 ---- N Article
