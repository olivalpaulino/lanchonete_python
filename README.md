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
Com o servidor rodando você pode fazer uma requisição web para localhost:8000:
- GET /products → lista todos os produtos (localhost:8000/products)
- POST /products → cria um novo produto (localhost:8000/products)
-- Exemplo de corpo da requisição, seria interessante usar postman com o corpo da requisição:
{
  "name": "Hamburguer",
  "price": 25.0
}

Passo 1: Fazer uma requisição com o método http post, usando a rota localhost:8000/products com o corpo da requisição acima.
Passo 2: Fazer uma requisição com o método http get, para analisar todos os produtos cadastrados, pela rota: localhost:8000/products
Passo 3: Caso cadastre mais de um produto via método http post, seguindo as instruções do passo 1, você agora pode pesquisar produtos cadastrados pelo id, usando o método http, na rota: localhost:8000/products/id, onde id é o substituido pelo código de identificação do produto que se deseja ver (esse código é gerado quando se cadastra um produto via método http post).

GET /products/1 → busca o produto com ID 1

Se você tivesse cadastrado só o produto acima, Hambuguer com o preço 25.0, o código id seria 1. Logo, o retorno da requisição GET localhost:8000/products/1 seria:

{
    "id": 1,
    "name": "Hamburguer",
    "price": 25.0
}

Espero que tenha gostado do exemplo e tenha dado tudo certo na prática.

[Olival Paulino no LinkedIn](https://www.linkedin.com/in/olivalpaulino/)
