# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class EmailOperator(BaseOperator):
    to: "list[str] | str"
    subject: "str"
    html_content: "str"
    from_email: "str | None"
    files: "list | None"
    cc: "list[str] | str | None"
    bcc: "list[str] | str | None"
    mime_subtype: "str"
    mime_charset: "str"
    conn_id: "str"
    custom_headers: "dict[str, Any] | None"