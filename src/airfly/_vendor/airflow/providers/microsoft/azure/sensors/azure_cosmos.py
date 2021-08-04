# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


@immutable
class AzureCosmosDocumentSensor(BaseSensorOperator):
    database_name: "str"
    collection_name: "str"
    document_id: "str"
    azure_cosmos_conn_id: "str"
