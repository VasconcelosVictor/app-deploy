
echo " BUILD START"
# Atualiza o pip
# Atualiza o pip
/usr/bin/python3.9 -m ensurepip
/usr/bin/python3.9 -m pip install --upgrade pip

# Cria e ativa o ambiente virtual (opcional, se necessário)
# /usr/bin/python3.9 -m venv myenv
# source myenv/bin/activate

# Instala as dependências do projeto
/usr/bin/python3.9 -m pip install -r requirements.txt

# Executa as migrações do Django
/usr/bin/python3.9 manage.py migrate

# Coleta os arquivos estáticos
/usr/bin/python3.9 manage.py collectstatic --noinput --clear


# python3.9 manage.py collectstatic  --noinput --clear
echo " BUILD END"