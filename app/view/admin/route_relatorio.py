from flask import Blueprint, render_template
from app.view.admin.routes_admin_panel import AdminPanel

relatorio = Blueprint('relatorios',__name__)

class Relatorio(AdminPanel):
    def dispatch_request(self):
        super().get()
        return render_template('admin/relatorios.html')
    
relatorio.add_url_rule('/', view_func=Relatorio.as_view('relatorios'))