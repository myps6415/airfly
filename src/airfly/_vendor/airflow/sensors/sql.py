# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


@immutable
class SqlSensor(BaseSensorOperator):
    conn_id: "_empty"
    sql: "_empty"
    parameters: "_empty"
    success: "_empty"
    failure: "_empty"
    fail_on_empty: "_empty"
