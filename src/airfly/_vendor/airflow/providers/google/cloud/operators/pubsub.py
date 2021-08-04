# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class PubSubCreateSubscriptionOperator(BaseOperator):
    topic: "str"
    project_id: "typing.Union[str, NoneType]"
    subscription: "typing.Union[str, NoneType]"
    subscription_project_id: "typing.Union[str, NoneType]"
    ack_deadline_secs: "int"
    fail_if_exists: "bool"
    gcp_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    push_config: "typing.Union[typing.Dict, google.cloud.pubsub_v1.types.PushConfig, NoneType]"
    retain_acked_messages: "typing.Union[bool, NoneType]"
    message_retention_duration: "typing.Union[typing.Dict, google.protobuf.duration_pb2.Duration, NoneType]"
    labels: "typing.Union[typing.Dict[str, str], NoneType]"
    enable_message_ordering: "bool"
    expiration_policy: "typing.Union[typing.Dict, google.cloud.pubsub_v1.types.ExpirationPolicy, NoneType]"
    filter_: "typing.Union[str, NoneType]"
    dead_letter_policy: "typing.Union[typing.Dict, google.cloud.pubsub_v1.types.DeadLetterPolicy, NoneType]"
    retry_policy: "typing.Union[typing.Dict, google.cloud.pubsub_v1.types.RetryPolicy, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    topic_project: "typing.Union[str, NoneType]"
    subscription_project: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class PubSubCreateTopicOperator(BaseOperator):
    topic: "str"
    project_id: "typing.Union[str, NoneType]"
    fail_if_exists: "bool"
    gcp_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    labels: "typing.Union[typing.Dict[str, str], NoneType]"
    message_storage_policy: "typing.Union[typing.Dict, google.cloud.pubsub_v1.types.MessageStoragePolicy]"
    kms_key_name: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    project: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class PubSubDeleteSubscriptionOperator(BaseOperator):
    subscription: "str"
    project_id: "typing.Union[str, NoneType]"
    fail_if_not_exists: "bool"
    gcp_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    project: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class PubSubDeleteTopicOperator(BaseOperator):
    topic: "str"
    project_id: "typing.Union[str, NoneType]"
    fail_if_not_exists: "bool"
    gcp_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    project: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class PubSubPublishMessageOperator(BaseOperator):
    topic: "str"
    messages: "typing.List"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    project: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
