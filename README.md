# AIRFLOW -> DATA PIPELINE

It is an open-source platform used for programming, scheduling, and monitoring workflows. Developed with Python, it uses the Python language to define data processing workflows, known as Directed Acyclic Graphs (DAGs). A DAG represents the steps in a data processing workflow and the dependencies between these steps.
The DAG folder is moved into Airflow with the help of GitlabSync. It synchronizes with the Airflow WebUI every 10 seconds.

## TechStack
- Airflow 2.8.2
- Redis
- Postgresql


# INSTALL

- sudo apt install golang-docker-credential-helpers
- docker logout
- docker login
- mkdir -p ./dags ./logs ./plugins ./config
- echo -e "AIRFLOW_UID=$(id -u)" > .env

##  Metadata create
docker compose up airflow-init   

## Application run
docker compose up

# CONFIGURATIONS
https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html

# POC
- Oracle to Postgresql
- Postgresql to Oracle
- Postgresql Enum Type convert Oracle Enum Table
- Generic Transfer
- Callback methods
- Failover Scenario
- Paralel Dags
- Logging
