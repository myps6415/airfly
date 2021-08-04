# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.sensors.sql import SqlSensor


@immutable
class MetastorePartitionSensor(SqlSensor):
    table: "str"
    partition_name: "str"
    schema: "str"
    mysql_conn_id: "str"
