
echo " BUILD START"
python3.9 -m virtualenv .env 
source .env/bin/activate
pip install -r requirements.txt
python3.9 manage.py migrate
# python3.9 manage.py collectstatic  --noinput --clear
echo " BUILD END"