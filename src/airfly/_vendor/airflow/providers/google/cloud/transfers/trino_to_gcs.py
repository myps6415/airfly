# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.transfers.sql_to_gcs import (
    BaseSQLToGCSOperator,
)


class TrinoToGCSOperator(BaseSQLToGCSOperator):
    trino_conn_id: "str"