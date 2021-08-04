# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class JdbcOperator(BaseOperator):
    sql: "str"
    jdbc_conn_id: "str"
    autocommit: "bool"
    parameters: "typing.Union[typing.Mapping, typing.Iterable, NoneType]"
