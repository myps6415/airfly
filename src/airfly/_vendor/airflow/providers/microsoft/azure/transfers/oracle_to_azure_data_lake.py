# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class OracleToAzureDataLakeOperator(BaseOperator):
    filename: "str"
    azure_data_lake_conn_id: "str"
    azure_data_lake_path: "str"
    oracle_conn_id: "str"
    sql: "str"
    sql_params: "typing.Union[dict, NoneType]"
    delimiter: "str"
    encoding: "str"
    quotechar: "str"
    quoting: "str"