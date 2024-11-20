from flask import Blueprint

disciplinas = Blueprint('disciplinas',__name__)

"""
    -- obter disciplinas / (GET)
    -- editar disciplinas / (PUT)
    -- cadastrar disciplinas /new (POST)
    -- excluir disciplinas / (DELET)
"""

@disciplinas.route('/')
def getDisciplinas():
    pass

@disciplinas.route('/new', methods=['POST'])
def newDisciplinas():
    pass

@disciplinas.route('/<int:id>', methods=['PUT'])
def editDisciplinas(id):
    pass

@disciplinas.route('/<int:id>/delete')
def deleteDisciplinas(id):
    pass