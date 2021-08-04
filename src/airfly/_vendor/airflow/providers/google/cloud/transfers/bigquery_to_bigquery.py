# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class BigQueryToBigQueryOperator(BaseOperator):
    source_project_dataset_tables: "typing.Union[typing.List[str], str]"
    destination_project_dataset_table: "str"
    write_disposition: "str"
    create_disposition: "str"
    gcp_conn_id: "str"
    bigquery_conn_id: "typing.Union[str, NoneType]"
    delegate_to: "typing.Union[str, NoneType]"
    labels: "typing.Union[typing.Dict, NoneType]"
    encryption_configuration: "typing.Union[typing.Dict, NoneType]"
    location: "typing.Union[str, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
