from flask import Flask
from flask_login import LoginManager

from app.models.database_SEDELT import db

from app.home import bp_home

from app.controller.admin.routes_admin_panel import admin
from app.controller.admin.routes_alunos import alunos
from app.controller.admin.routes_professores import professores
from app.controller.admin.routes_disciplinas import disciplinas
from app.controller.admin.route_relatorio import relatorio
from app.controller.auth import bp_auth, login_manager

from app.controller.student_reg_management.routes_reg_management import registration_management

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SEDELT.db'
app.config['SECRET_KEY'] = '123'

#configurando a base de dados
db.init_app(app)

#configurando o gerenciamento de login
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

#pagina com os links de acesso as demais funcionalidades
app.register_blueprint(bp_home, url_prefix='/')

#blueprint para logar no sistema
app.register_blueprint(bp_auth)

#nestas rotas os administradores terão acesso
admin.register_blueprint(professores, url_prefix='/professores')
admin.register_blueprint(alunos, url_prefix='/alunos')
admin.register_blueprint(disciplinas, url_prefix='/disciplinas')
admin.register_blueprint(relatorio, url_prefix='/relatorio')
app.register_blueprint(admin, url_prefix='/admin')

#nestas rotas os professores poderão matricular os alunos nas disciplinas
app.register_blueprint(registration_management, url_prefix='/matricula')

with app.app_context():
    db.create_all()