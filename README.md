# django-todo

Um aplicativo de tarefas simples construído com Django

### Configuração

Atualize o Sistema
bash
sudo apt-get update


Para obter este repositório, execute o seguinte comando no seu terminal com git habilitado
bash
git clone https://github.com/Pessoa1998/ultima_cartada_deploy_aws


Você precisará do Django instalado no seu computador para executar este aplicativo.

Baixe o Django usando pip
bash
sudo apt install python3-pip -y

bash
pip install django


Depois de baixar o Django, vá para o diretório do repositório clonado e execute o seguinte comando
bash
python3 manage.py makemigrations
"A tag de cima é coerente pois estamos usando a biblioteca DJANGO, caso tivesse-mos usado o flask conforme instrução do professor em sala de aula não seria necessário"

Isso criará todos os arquivos de migração (migrações de banco de dados) necessários para executar este aplicativo.

Agora, para aplicar essas migrações, execute o seguinte comando
bash
python3 manage.py migrate


Um último passo e então nosso aplicativo de tarefas estará ativo. Precisamos criar um usuário admin para executar este aplicativo. No terminal, digite o seguinte comando e forneça nome de usuário, senha e e-mail para o usuário admin
bash
python3 manage.py createsuperuser


Após ter feito todo o trâmite acima basta apenas iniciar o servidor agora e então podemos começar a usar nosso aplicativo de tarefas simples. Inicie o servidor com o comando a seguir
bash
python3 manage.py runserver


Uma vez que o servidor estiver hospedado, vá para http://127.0.0.1:8000/todos para acessar o aplicativo.

Att, Gabriel Pessoa e Lucas Origa.
