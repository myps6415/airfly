# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.providers.microsoft.azure.operators.adls_list import (
    AzureDataLakeStorageListOperator,
)


@immutable
class ADLSToGCSOperator(AzureDataLakeStorageListOperator):
    src_adls: "str"
    dest_gcs: "str"
    azure_data_lake_conn_id: "str"
    gcp_conn_id: "str"
    google_cloud_storage_conn_id: "typing.Union[str, NoneType]"
    delegate_to: "typing.Union[str, NoneType]"
    replace: "bool"
    gzip: "bool"
    google_impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
