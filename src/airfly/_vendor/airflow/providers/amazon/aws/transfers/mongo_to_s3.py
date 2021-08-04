# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class MongoToS3Operator(BaseOperator):
    s3_conn_id: "typing.Union[str, NoneType]"
    mongo_conn_id: "str"
    aws_conn_id: "str"
    mongo_collection: "str"
    mongo_query: "typing.Union[list, dict]"
    s3_bucket: "str"
    s3_key: "str"
    mongo_db: "typing.Union[str, NoneType]"
    replace: "bool"
    allow_disk_use: "bool"
    compression: "typing.Union[str, NoneType]"
