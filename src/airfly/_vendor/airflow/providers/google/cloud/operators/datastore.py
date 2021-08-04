# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class CloudDatastoreExportEntitiesOperator(BaseOperator):
    bucket: "str"
    namespace: "typing.Union[str, NoneType]"
    datastore_conn_id: "str"
    cloud_storage_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    entity_filter: "typing.Union[dict, NoneType]"
    labels: "typing.Union[dict, NoneType]"
    polling_interval_in_seconds: "int"
    overwrite_existing: "bool"
    project_id: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


@immutable
class CloudDatastoreImportEntitiesOperator(BaseOperator):
    bucket: "str"
    file: "str"
    namespace: "typing.Union[str, NoneType]"
    entity_filter: "typing.Union[dict, NoneType]"
    labels: "typing.Union[dict, NoneType]"
    datastore_conn_id: "str"
    delegate_to: "typing.Union[str, NoneType]"
    polling_interval_in_seconds: "float"
    project_id: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
