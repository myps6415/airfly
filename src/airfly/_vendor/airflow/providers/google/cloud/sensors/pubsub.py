# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


@immutable
class PubSubPullSensor(BaseSensorOperator):
    project_id: "str"
    subscription: "str"
    max_messages: "int"
    return_immediately: "bool"
    ack_messages: "bool"
    gcp_conn_id: "str"
    messages_callback: "typing.Union[typing.Callable[[typing.List[google.cloud.pubsub_v1.types.ReceivedMessage], typing.Dict[str, typing.Any]], typing.Any], NoneType]"
    delegate_to: "typing.Union[str, NoneType]"
    project: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
