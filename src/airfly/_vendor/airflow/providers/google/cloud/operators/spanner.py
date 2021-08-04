# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class SpannerDeleteDatabaseInstanceOperator(BaseOperator):
    instance_id: "str"
    database_id: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class SpannerDeleteInstanceOperator(BaseOperator):
    instance_id: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class SpannerDeployDatabaseInstanceOperator(BaseOperator):
    instance_id: "str"
    database_id: "str"
    ddl_statements: "typing.List[str]"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class SpannerDeployInstanceOperator(BaseOperator):
    instance_id: "str"
    configuration_name: "str"
    node_count: "int"
    display_name: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class SpannerQueryDatabaseInstanceOperator(BaseOperator):
    instance_id: "str"
    database_id: "str"
    query: "typing.Union[str, typing.List[str]]"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class SpannerUpdateDatabaseInstanceOperator(BaseOperator):
    instance_id: "str"
    database_id: "str"
    ddl_statements: "typing.List[str]"
    project_id: "typing.Union[str, NoneType]"
    operation_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
