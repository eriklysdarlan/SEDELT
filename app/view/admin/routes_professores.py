from flask import Blueprint, render_template, request
from flask.views import View
from app.view.admin.routes_admin_panel import AdminPanel
from app.models.database_SEDELT import db

professores = Blueprint('professores', __name__)

"""
    -- obter professores
    -- cadastrar professores 
    -- editar professores
    -- excluir professores
"""

class Professores(AdminPanel):
    methods = ["GET", "POST"]

    def get_professores(self):
        """Obter todos os professores"""
        super().get()
        professores = db.session.execute(db.select(professores).all())
        return render_template('admin/professores.html', professores=professores)
    
    def creat_professores(self):
        if request.method == 'POST':
            pass
        """Cadastrar professores"""
        pass

    def patch_professores(self):
        """Editar professores"""
        pass

    def delete_professores(self):
        """Excluir professores"""
        pass
    
professores.add_url_rule('/', view_func=Professores.as_view('professores'))