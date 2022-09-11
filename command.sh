curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.4/docker-compose.yaml'
# after edit, remove some command in docker-compose.yaml
mkdir -p ./dags ./logs ./plugins
# khusus untuk linux jlnkan perintah ini (wnidows & mac tdk perlu)
echo -e "AIRFLOW_UID=$(id -u)" > .env

# build container
docker-compose up airflow-init

# run container
docker-compose up -d

docker ps