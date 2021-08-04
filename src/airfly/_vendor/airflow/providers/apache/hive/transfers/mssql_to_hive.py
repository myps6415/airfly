# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class MsSqlToHiveOperator(BaseOperator):
    sql: "str"
    hive_table: "str"
    create: "bool"
    recreate: "bool"
    partition: "typing.Union[typing.Dict, NoneType]"
    delimiter: "str"
    mssql_conn_id: "str"
    hive_cli_conn_id: "str"
    tblproperties: "typing.Union[typing.Dict, NoneType]"
