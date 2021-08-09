# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class DynamoDBToS3Operator(BaseOperator):
    dynamodb_table_name: "str"
    s3_bucket_name: "str"
    file_size: "int"
    dynamodb_scan_kwargs: "typing.Union[typing.Dict[str, typing.Any], NoneType]"
    s3_key_prefix: "str"
    process_func: "typing.Callable[[typing.Dict[str, typing.Any]], bytes]"