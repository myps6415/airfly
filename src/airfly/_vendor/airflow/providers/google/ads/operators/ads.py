# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GoogleAdsListAccountsOperator(BaseOperator):
    bucket: "str"
    object_name: "str"
    gcp_conn_id: "str"
    google_ads_conn_id: "str"
    gzip: "bool"
    impersonation_chain: "str | Sequence[str] | None"
    api_version: "str | None"