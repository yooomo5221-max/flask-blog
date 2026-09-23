from flask import Flask, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # MySQL 数据库连接配置
    # SQLite 数据库配置
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

    # 关闭 SQLAlchemy 的事件追踪
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Flask-Login 配置
    app.config["SECRET_KEY"] = "blog-secret-key"

    # 初始化数据库
    db.init_app(app)

    # 初始化 Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    # 用户加载函数
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return db.session.get(User, int(user_id))

    # 创建数据库表
    with app.app_context():
        from .models import User
        db.create_all()

    # 注册路由
    from .routes import main_bp
    app.register_blueprint(main_bp)

    from flask import redirect

    @app.route("/")
    def index():
        return redirect("/articles")