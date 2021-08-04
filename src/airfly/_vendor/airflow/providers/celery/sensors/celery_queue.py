# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


@immutable
class CeleryQueueSensor(BaseSensorOperator):
    celery_queue: "str"
    target_task_id: "typing.Union[str, NoneType]"
