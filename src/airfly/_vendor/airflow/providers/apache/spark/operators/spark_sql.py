# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class SparkSqlOperator(BaseOperator):
    sql: "str"
    conf: "typing.Union[str, NoneType]"
    conn_id: "str"
    total_executor_cores: "typing.Union[int, NoneType]"
    executor_cores: "typing.Union[int, NoneType]"
    executor_memory: "typing.Union[str, NoneType]"
    keytab: "typing.Union[str, NoneType]"
    principal: "typing.Union[str, NoneType]"
    master: "typing.Union[str, NoneType]"
    name: "str"
    num_executors: "typing.Union[int, NoneType]"
    verbose: "bool"
    yarn_queue: "typing.Union[str, NoneType]"
