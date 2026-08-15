from flask import jsonify, request
from data import users as data_users


def listar_usuarios():
    lista = data_users.listar_todos()
    return jsonify({"success": True, "data": lista}), 200


def validar_dados_usuario(dados):
    if not dados:
        return "O corpo da requisição deve ser um JSON válido."
    if not dados.get("nome") or not str(dados["nome"]).strip():
        return "O campo 'nome' é obrigatório."
    if not dados.get("email") or "@" not in str(dados["email"]):
        return "O campo 'email' é obrigatório e deve ser um e-mail válido."
    return None


def cadastrar_usuario():
    dados = request.get_json(silent=True)

    erro = validar_dados_usuario(dados)
    if erro:
        return jsonify({"error": erro}), 400

    novo_usuario = data_users.adicionar(dados["nome"], dados["email"])
    return jsonify({"data": novo_usuario}), 201


def buscar_usuario(usuario_id):
    usuario = data_users.buscar_por_id(usuario_id)

    if usuario is None:
        return jsonify({"success": False, "message": "Usuário não encontrado."}), 404

    return jsonify({"success": True, "data": usuario}), 200


def atualizar_usuario(usuario_id):
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"success": False, "message": "Corpo da requisição deve ser um JSON válido."}), 400

    usuario_atualizado = data_users.atualizar(
        usuario_id,
        nome=dados.get("nome"),
        email=dados.get("email"),
    )

    if usuario_atualizado is None:
        return jsonify({"success": False, "message": "Usuário não encontrado."}), 404

    return jsonify({"success": True, "data": usuario_atualizado}), 200


def remover_usuario(usuario_id):
    removido = data_users.remover(usuario_id)

    if not removido:
        return jsonify({"success": False, "message": "Usuário não encontrado."}), 404

    return "", 204