# Flask Blog

基于 Flask 的个人博客系统实践项目。


## 项目介绍

本项目是在 AI 辅助开发过程中完成的 Web 应用实践项目。

通过学习 Flask 框架结构，结合 AI 工具辅助完成网站功能搭建，了解 Web 应用从设计、开发、调试到部署上线的完整流程。


## 技术与工具

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- MySQL
- HTML/CSS
- GitHub
- Render
- AI辅助开发工具


## 功能实现

### 用户功能

- 用户注册
- 用户登录
- 用户状态管理
- 个人信息页面


### 文章功能

- 文章列表展示
- 查看文章详情
- 发布文章
- 编辑文章


## 数据库设计

项目主要包含用户和文章数据。


### User 用户表

|字段|说明|
|-|-|
|id|用户ID|
|username|用户名|
|password|密码|
|email|邮箱|


### Article 文章表

|字段|说明|
|-|-|
|id|文章ID|
|title|文章标题|
|content|文章内容|
|created_at|创建时间|
|updated_at|更新时间|
|user_id|作者ID|


数据关系：

User 1 ---- N Article


## 项目过程

项目实践过程中：

- 学习 Flask 项目结构
- 使用 AI 工具辅助理解代码和解决问题
- 完成功能调整和测试
- 学习项目部署流程


## 在线访问

https://flask-blog-vfp1.onrender.com/articles


## 项目收获

通过本项目：

- 了解 Web 应用开发基本流程
- 掌握 AI 辅助学习和开发的方法
- 提升将想法转化为实际项目的能力
