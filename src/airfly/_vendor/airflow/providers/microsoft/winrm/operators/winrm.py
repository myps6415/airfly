# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class WinRMOperator(BaseOperator):
    winrm_hook: "typing.Union[airflow.providers.microsoft.winrm.hooks.winrm.WinRMHook, NoneType]"
    ssh_conn_id: "typing.Union[str, NoneType]"
    remote_host: "typing.Union[str, NoneType]"
    command: "typing.Union[str, NoneType]"
    ps_path: "typing.Union[str, NoneType]"
    output_encoding: "str"
    timeout: "int"
