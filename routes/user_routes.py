from flask import Blueprint
from controllers.user_controller import listar_usuarios, cadastrar_usuario
from controllers.user_controller import listar_usuarios, cadastrar_usuario, buscar_usuario
from controllers.user_controller import (
    listar_usuarios,
    cadastrar_usuario,
    buscar_usuario,
    atualizar_usuario,
    remover_usuario,
)

user_bp = Blueprint("usuarios", __name__)


@user_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    return listar_usuarios()


@user_bp.route("/usuarios", methods=["POST"])
def post_usuario():
    return cadastrar_usuario()


@user_bp.route("/usuarios/<int:usuario_id>", methods=["GET"])
def get_usuario(usuario_id):
    return buscar_usuario(usuario_id)


@user_bp.route("/usuarios/<int:usuario_id>", methods=["PUT", "PATCH"])
def put_usuario(usuario_id):
    return atualizar_usuario(usuario_id)


@user_bp.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
def delete_usuario(usuario_id):
    return remover_usuario(usuario_id)