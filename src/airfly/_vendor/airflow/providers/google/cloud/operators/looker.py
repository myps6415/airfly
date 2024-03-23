# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class LookerStartPdtBuildOperator(GoogleCloudBaseOperator):
    looker_conn_id: "str"
    model: "str"
    view: "str"
    query_params: "dict | None"
    asynchronous: "bool"
    cancel_on_kill: "bool"
    wait_time: "int"
    wait_timeout: "int | None"