# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class MySqlOperator(BaseOperator):
    sql: "str"
    mysql_conn_id: "str"
    parameters: "typing.Union[typing.Mapping, typing.Iterable, NoneType]"
    autocommit: "bool"
    database: "typing.Union[str, NoneType]"
