# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class GlueJobSensor(BaseSensorOperator):
    job_name: "str"
    run_id: "str"
    verbose: "bool"
    aws_conn_id: "str | None"