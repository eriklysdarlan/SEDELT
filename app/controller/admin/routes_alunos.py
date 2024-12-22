from flask import Blueprint, render_template
from app.controller.admin.routes_admin_panel import AdminPanel


alunos = Blueprint('alunos',__name__)

"""
    -- obter alunos / (GET)
    -- editar alunos / (PUT)
    -- cadastrar alunos /new (POST)
    -- excluir alunos / (DELET)
"""
class Alunos(AdminPanel):
    def get(self):
        super().get()
        return render_template('admin/alunos.html')
    
alunos.add_url_rule('/', view_func=Alunos.as_view('alunos'))