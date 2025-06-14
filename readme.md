### Api store
A api de uma loja feita com django e django_rest

## Instalando
### Clonando o repositorio

``` bash
git clone https://github.com/Jose-GuilhermeG/loja_api
```

### criando um ambiente virtual
#### baixe o virtualenv
```bash
pip install virtualenv
```

#### criando
```bash
python -m virtualenv env
```

#### ativando
linux
```bash
source env/bin/activate
```

### Baixando as dependencias
```bash
pip install -r requirements.txt
```

### Criando o .env
no projeto ha um arquivo .env_exemple basta criar um .env copiar os dados do .env_exemple e prencher as informações

### Rodando
com o projeto e o ambiente virtual prontos

procure as migrações
```bash
python manage.py makemigrations
```
aplique as migrações
```bash
python manage.py migrate
```

por fim rode
```bash
python manage.py runserver
```