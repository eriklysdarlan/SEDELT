from flask import Blueprint, render_template, jsonify


alunos = Blueprint('alunos',__name__)

"""
    -- obter alunos / (GET)
    -- editar alunos / (PUT)
    -- cadastrar alunos /new (POST)
    -- excluir alunos / (DELET)
"""

""" @alunos.route('/')
def getAlunos():
    return jsonify(bdalunos)

@alunos.route('/new', methods=['POST'])
def newAlunos():
    pass

@alunos.route('/<int:id>', methods=['PUT'])
def editAlunos(id):
    pass

@alunos.route('/<int:id>/delete')
def deleteAlunos(id):
    pass """