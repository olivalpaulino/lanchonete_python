API REST em Python puro, usando apenas módulos nativos (http.server) para mostrar:
- Organização de código (estrutura de pastas)
- Separação de responsabilidades (modelo, serviço, controlador)
- Documentação (README.md e docstrings)
- Código limpo e testável

📦 Estrutura que vamos criar:
simple_api/
├── app/
│   ├── __init__.py
│   ├── server.py
│   ├── controller.py
│   ├── service.py
│   └── model.py
├── tests/
│   └── test_service.py
├── README.md
└── requirements.txt

Explicação Rápida:
- model.py: Representa os dados (Ex: Produto, Usuário, etc.).
- service.py: Regras de negócio (Ex: criar, listar, deletar).
- controller.py: Recebe as requisições HTTP e chama o serviço certo.
- server.py: Inicializa o servidor HTTP.
- tests/test_service.py: Teste de unidade para o serviço.
- README.md: Documentação do projeto.

Ideia da aplicação:
- Uma API de Produtos que permita:
-- Listar todos os produtos
-- Adicionar um novo produto
-- Buscar produto por ID

Tudo usando requisições HTTP (GET, POST) e JSON.

Exemplo de uso:
Com o servidor rodando:
- GET /products → lista todos os produtos
- POST /products → cria um novo produto
-- Exemplo de corpo da requisição:
{
  "name": "Hamburguer",
  "price": 25.0
}

GET /products/1 → busca o produto com ID 1

Espero que tenha gostado do exemplo e tenha dado tudo certo na prática.

[Olival Paulino no LinkedIn](https://www.linkedin.com/in/olivalpaulino/)
