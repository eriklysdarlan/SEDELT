from flask import Blueprint, render_template
from flask.views import MethodView
from app.controller.admin.routes_admin_panel import AdminPanel

professores = Blueprint('professores', __name__)

"""
    -- obter professores
    -- cadastrar professores 
    -- editar professores
    -- excluir professores
"""

class Professores(AdminPanel):
    def get(self):
        super().get()
        return render_template('admin/professores.html')
    
professores.add_url_rule('/', view_func=Professores.as_view('professores'))