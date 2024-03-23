# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class S3KeySensor(BaseSensorOperator):
    bucket_key: "str | list[str]"
    bucket_name: "str | None"
    wildcard_match: "bool"
    check_fn: "Callable[..., bool] | None"
    aws_conn_id: "str | None"
    verify: "str | bool | None"
    deferrable: "bool"
    use_regex: "bool"


class S3KeysUnchangedSensor(BaseSensorOperator):
    bucket_name: "str"
    prefix: "str"
    aws_conn_id: "str | None"
    verify: "bool | str | None"
    inactivity_period: "float"
    min_objects: "int"
    previous_objects: "set[str] | None"
    allow_delete: "bool"
    deferrable: "bool"