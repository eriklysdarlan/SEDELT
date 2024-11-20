from flask import Blueprint

professores = Blueprint('professores',__name__)

"""
    -- obter professores
    -- cadastrar professores 
    -- editar professores
    -- excluir professores
"""

@professores.route('/')
def geteprofessores():
    pass

@professores.route('/new', methods=['POST'])
def neweprofessores():
    pass

@professores.route('/<int:id>', methods=['PUT'])
def editeprofessoresid():
    pass

@professores.route('/<int:id>/delete')
def deleteprofessores(id):
    pass