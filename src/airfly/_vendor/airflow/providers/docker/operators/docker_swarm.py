# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.providers.docker.operators.docker import DockerOperator


@immutable
class DockerSwarmOperator(DockerOperator):
    image: "str"
    enable_logging: "bool"
