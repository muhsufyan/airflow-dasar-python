# INSTALL
# step 1) formatnya 
python -m venv {name directory virtual environment}
python -m venv env

# step 2) windows
.\env\Scripts\activate.bat
# linux or mac
 source env/bin/activate

# update dulu
pip install --upgrade pip

pip install wheel


# step 3)
python --version
# step 4 install with pypi
# dlm 2 baris
pip install 'apache-airflow==2.3.4' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.4/constraints-{versi python kita}.txt"
# dalam 1 baris
pip install 'apache-airflow==2.3.4' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.4/constraints-{versi python kita}.txt"
# versi python kita 3.10.4 so 
pip install 'apache-airflow==2.3.4' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.4/constraints-3.8.txt"
#  if error caused pip not found
python -m ensurepip
# NOTE JIKA ERROR GUNAKAN CARA SELANJUTNYA YAITU LEWAT DOCKER

# step 5) set ke environment variable
# linux/mac
export AIRFLOW_HOME=.
# if error when airflow db init use this command 
export AIRFLOW_HOME=~/airflow
# windows
SET AIRFLOW_HOME=.

# step 6) dlm kasus ini sql lite
airflow db init

# step 7)
# cek dulu env apa yg dibthkan untuk membuat account
airflow users create --help
# buat account baru as admin
airflow users create --username admin --firstname dummy --lastname bebas --role Admin --email admin@domain.com
# step 8) kita gunakan port 7000
airflow webserver -p 7000

# step 9) make sure
export AIRFLOW_HOME=.
# windows
SET AIRFLOW_HOME=.
# scheduler
airflow scheduler


# BASH OPERATOR
airflow webserver -p 7000

# if use docker, hapus container (agar dag jd kosong)
docker-compose down -V 
# di file docker-compose pd bagian example ubah jd false
docker-compose up

# buat file baru
touch first_dag.py
