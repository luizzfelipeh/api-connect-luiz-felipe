usuarios = []
proximo_id = 1


def listar_todos():
    return usuarios


def buscar_por_id(usuario_id):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    return None


def adicionar(nome, email):
    global proximo_id
    novo_usuario = {
        "id": proximo_id,
        "nome": nome,
        "email": email,
    }
    usuarios.append(novo_usuario)
    proximo_id += 1
    return novo_usuario


def atualizar(usuario_id, nome=None, email=None):
    usuario = buscar_por_id(usuario_id)
    if usuario is None:
        return None
    if nome is not None:
        usuario["nome"] = nome
    if email is not None:
        usuario["email"] = email
    return usuario


def remover(usuario_id):
    usuario = buscar_por_id(usuario_id)
    if usuario is None:
        return False
    usuarios.remove(usuario)
    return True