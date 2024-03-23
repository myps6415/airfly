# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GoogleAdsToGcsOperator(BaseOperator):
    client_ids: "list[str]"
    query: "str"
    attributes: "list[str]"
    bucket: "str"
    obj: "str"
    gcp_conn_id: "str"
    google_ads_conn_id: "str"
    page_size: "int"
    gzip: "bool"
    impersonation_chain: "str | Sequence[str] | None"
    api_version: "str | None"