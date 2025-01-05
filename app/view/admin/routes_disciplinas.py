from flask import Blueprint, render_template
from app.view.admin.routes_admin_panel import AdminPanel

disciplinas = Blueprint('disciplinas',__name__)

"""
    -- obter disciplinas / (GET)
    -- editar disciplinas / (PUT)
    -- cadastrar disciplinas /new (POST)
    -- excluir disciplinas / (DELET)
"""

class Disciplinas(AdminPanel):
    def get(self):
        super().get()
        return render_template('admin/disciplinas.html')
    
disciplinas.add_url_rule('/', view_func=Disciplinas.as_view('disciplinas'))