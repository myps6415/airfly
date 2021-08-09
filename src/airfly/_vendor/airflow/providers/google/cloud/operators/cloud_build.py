# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class CloudBuildCreateBuildOperator(BaseOperator):
    body: "typing.Union[dict, str]"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"