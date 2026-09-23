from flask import Blueprint, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from . import db
from .models import User, Article


main_bp = Blueprint("main", __name__)


# ==================== 数据库测试 ====================

@main_bp.route("/db-test")
def db_test():

    result = db.session.execute(
        db.text("SELECT 1")
    ).scalar()

    if result == 1:
        return "MySQL 数据库连接成功！"

    return "MySQL 数据库连接失败！"


# ==================== 注册 ====================

@main_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")

    if not username or not password or not email:
        return "用户名、密码和邮箱不能为空！"

    # 检查用户名是否已经存在
    existing_user = User.query.filter_by(
        username=username
    ).first()

    if existing_user:
        return "用户名已经存在！"

    # 密码哈希
    password_hash = generate_password_hash(password)

    user = User(
        username=username,
        password=password_hash,
        email=email
    )

    db.session.add(user)
    db.session.commit()

    return "注册成功！"

# ==================== 登录 ====================

@main_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "用户名和密码不能为空！"

    # 根据用户名查询用户
    user = User.query.filter_by(
        username=username
    ).first()

    # 检查用户是否存在，以及密码是否正确
    if user is None or not check_password_hash(
        user.password,
        password
    ):
        return "用户名或密码错误！"

    # 登录用户
    login_user(user)

    return f"登录成功！当前用户：{user.username}"


# ==================== 退出登录 ====================

@main_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return "已退出登录！"


# ==================== 个人中心 ====================

@main_bp.route("/profile")
@login_required
def profile():

    return render_template("profile.html")


# ==================== 发布文章 ====================

@main_bp.route("/article/create", methods=["GET", "POST"])
@login_required
def create_article():

    if request.method == "GET":
        return render_template("create_article.html")

    title = request.form.get("title")
    content = request.form.get("content")

    if not title or not content:
        return "标题和内容不能为空！"

    article = Article(
        title=title,
        content=content,
        user_id=current_user.id
    )

    db.session.add(article)
    db.session.commit()

    return render_template(
        "article_detail.html",
        article=article
    )

# ==================== 文章列表 ====================

@main_bp.route("/articles")
def article_list():

    articles = Article.query.order_by(
        Article.created_at.desc()
    ).all()

    return render_template(
        "articles.html",
        articles=articles
    )


# ==================== 文章详情 ====================

@main_bp.route("/article/<int:article_id>")
def article_detail(article_id):

    article = Article.query.get_or_404(article_id)

    return render_template(
        "article_detail.html",
        article=article
    )


# ==================== 编辑文章 ====================

@main_bp.route(
    "/article/<int:article_id>/edit",
    methods=["GET", "POST"]
)
@login_required
def edit_article(article_id):

    article = Article.query.get_or_404(article_id)

    # 只能编辑自己的文章
    if article.user_id != current_user.id:
        return "你没有权限编辑这篇文章！"

    # GET：显示编辑页面
    if request.method == "GET":

        return render_template(
            "edit_article.html",
            article=article
        )

    # POST：保存修改
    title = request.form.get("title")
    content = request.form.get("content")

    if not title or not content:
        return "标题和内容不能为空！"

    article.title = title
    article.content = content

    db.session.commit()

    # 修改成功后直接回到文章详情页
    return render_template(
        "article_detail.html",
        article=article
    )


# ==================== 删除文章 ====================

@main_bp.route(
    "/article/<int:article_id>/delete",
    methods=["POST"]
)
@login_required
def delete_article(article_id):

    article = Article.query.get_or_404(article_id)

    # 只能删除自己的文章
    if article.user_id != current_user.id:
        return "你没有权限删除这篇文章！"

    db.session.delete(article)
    db.session.commit()

    return """
    <h2>文章删除成功！</h2>

    <p>
        <a href="/articles">
            返回文章列表
        </a>
    </p>
    """