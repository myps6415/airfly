# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class FacebookAdsReportToGcsOperator(BaseOperator):
    bucket_name: "str"
    object_name: "str"
    fields: "list[str]"
    parameters: "dict[str, Any] | None"
    gzip: "bool"
    upload_as_account: "bool"
    api_version: "str | None"
    gcp_conn_id: "str"
    facebook_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"