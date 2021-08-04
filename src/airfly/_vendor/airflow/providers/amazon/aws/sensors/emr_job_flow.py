# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.providers.amazon.aws.sensors.emr_base import EmrBaseSensor


@immutable
class EmrJobFlowSensor(EmrBaseSensor):
    job_flow_id: "str"
    target_states: "typing.Union[typing.Iterable[str], NoneType]"
    failed_states: "typing.Union[typing.Iterable[str], NoneType]"
