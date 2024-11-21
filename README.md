# Task - Projeto com Python & Django

Este é um projeto de gerenciamento de tarefas (Task) desenvolvido com Python e Django. O objetivo é fornecer uma plataforma simples para que os usuários possam criar, gerenciar e marcar tarefas como concluídas.

## Tecnologias utilizadas

- **Python**: Linguagem de programação para o backend.
- **Django**: Framework web para desenvolvimento rápido e eficiente.
- **SQLite**: Banco de dados utilizado por padrão no Django (pode ser alterado para outros como PostgreSQL ou MySQL).

## Pré-requisitos

- Python 3.x instalado.
- pip (gerenciador de pacotes do Python) instalado.

## Instalação

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/ronierisonmaciel/task.git
cd task
```

### Passo 2: Criar e ativar um ambiente virtual

Se estiver utilizando `venv`:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

### Passo 3: Instalar as dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configuração do Banco de Dados

O Django utiliza o banco de dados SQLite por padrão. Se quiser usar um banco de dados diferente, edite as configurações em `task/settings.py`.

Rodar as migrações do banco de dados:

```bash
python manage.py migrate
```

### Passo 5: Criar um superusuário

Para acessar o painel administrativo do Django, crie um superusuário com o seguinte comando:

```bash
python manage.py createsuperuser
```

Siga as instruções para definir o nome de usuário, e-mail e senha.

### Passo 6: Rodar o servidor

Para rodar o servidor local de desenvolvimento, execute o seguinte comando:

```bash
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`.

## Estrutura do Projeto

A estrutura básica do projeto é a seguinte:

```
task/
│
├── config/                # Pasta do projeto Django
│   ├── migrations/        # Arquivos de migração do banco de dados
│   ├── __init__.py        # Arquivo de inicialização do pacote
│   ├── settings.py        # Arquivo de configurações do Django
│   ├── urls.py            # Arquivo de URLs do projeto
│   └── wsgi.py            # Arquivo de inicialização WSGI
│
├── manage.py              # Script para rodar comandos do Django
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

## Funcionalidades

- **Cadastro de tarefas**: O usuário pode cadastrar novas tarefas.
- **Lista de tarefas**: O usuário pode visualizar todas as tarefas cadastradas.
- **Marcar tarefas como concluídas**: As tarefas podem ser marcadas como concluídas.
- **Excluir tarefas**: O usuário pode excluir tarefas quando não forem mais necessárias.
- **Administração**: O Django fornece um painel administrativo para gerenciar as tarefas.

## Contribuições

Se você deseja contribuir para o projeto, por favor, siga os seguintes passos:

1. Faça um fork deste repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature-nome-da-feature`).
3. Realize as alterações e faça commit (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature-nome-da-feature`).
5. Crie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
