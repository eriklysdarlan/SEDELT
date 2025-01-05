from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from flask.views import View

admin = Blueprint('admin', __name__)
""" admin.register_blueprint(professores, url_prefix='/professores') """
"""
Os administradores deverão gerenciar todo fluxo de trabalho escolar.
isso inclui:
-- Inserir os alunos e professores na base de dados
-- Criar disciplinas
-- Criar turmas
-- associar professores as turmas
-- associar alunos as turmas
-- criar ano letivo
-- Gerar boletins
"""

class AdminPanel(View):
    decorators = [login_required]

    def dispatch_request(self):
        if not current_user.has_access('admin'):
            abort(403)
        return render_template('admin/admin.html')

admin.add_url_rule('/', view_func=AdminPanel.as_view('admin_panel'))
