# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


@immutable
class RedisPubSubSensor(BaseSensorOperator):
    channels: "typing.Union[typing.List[str], str]"
    redis_conn_id: "str"
