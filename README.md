# API Connect — Gerenciamento de Usuários

API REST desenvolvida como MVP (Produto Mínimo Viável) para uma plataforma de gerenciamento de usuários. O objetivo é fornecer ao time de front-end um conjunto de endpoints capazes de listar, buscar, cadastrar, atualizar e remover usuários, seguindo os padrões da arquitetura REST e trafegando dados exclusivamente em formato JSON.

## Objetivo

Servir como base back-end para a validação ágil de uma nova ideia de negócio, oferecendo operações CRUD completas sobre o recurso "usuário", com validação de entrada, códigos de status HTTP apropriados e respostas padronizadas.

## Tecnologias utilizadas

- **Python 3.14**
- **Flask** — microframework web
- **Persistência em memória** (lista Python), simulando um banco de dados para fins de prototipagem

## Estrutura do projeto

api-usuarios/
├── app.py # Ponto de entrada da aplicação
├── requirements.txt # Dependências do projeto
├── routes/
│ └── user_routes.py # Definição dos endpoints HTTP
├── controllers/
│ └── user_controller.py # Lógica de negócio e validação
└── data/
└── users.py # Persistência simulada em memória

## Como executar localmente

Clone o repositório e acesse a pasta do projeto:
```bash
git clone https://github.com/luizzfelipeh/api-connect-luiz-felipe.git
cd api-connect-luiz-felipe
```

Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Execute o servidor:
```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000`.

## Endpoints

| Método | Endpoint | Descrição | Corpo (JSON) | Sucesso | Erros |
|---|---|---|---|---|---|
| GET | `/usuarios` | Lista todos os usuários cadastrados | — | 200 OK | — |
| GET | `/usuarios/<id>` | Busca um usuário específico pelo ID | — | 200 OK | 404 (não encontrado) |
| POST | `/usuarios` | Cadastra um novo usuário | `{"nome": "string", "email": "string"}` | 201 Created | 400 (dados inválidos) |
| PUT / PATCH | `/usuarios/<id>` | Atualiza os dados de um usuário existente | `{"nome": "string", "email": "string"}` | 200 OK | 404 (não encontrado) |
| DELETE | `/usuarios/<id>` | Remove um usuário existente | — | 204 No Content | 404 (não encontrado) |

### Exemplo de requisição (POST)

```json
{
  "nome": "Ana",
  "email": "ana@email.com"
}
```

### Exemplo de resposta de sucesso

```json
{
  "data": {
    "id": 1,
    "nome": "Ana",
    "email": "ana@email.com"
  }
}
```

### Exemplo de resposta de erro

```json
{
  "error": "O campo 'email' é obrigatório e deve ser um e-mail válido."
}
```

## Autor

Luiz Felipe