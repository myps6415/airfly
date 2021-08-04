# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class SqliteOperator(BaseOperator):
    sql: "str"
    sqlite_conn_id: "str"
    parameters: "typing.Union[typing.Mapping, typing.Iterable, NoneType]"
