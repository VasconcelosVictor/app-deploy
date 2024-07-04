
echo " BUILD START"
# Atualiza o pip
python3.10 -m pip install --upgrade pip

# Instala as dependências Python
pip install -r requirements.txt
python3.10 -m pip install -r requirements.txt
python3.10 manage.py makemigrations
python3.10 manage.py migrate 

# python3.9 manage.py collectstatic  --noinput --clear
echo " BUILD END"