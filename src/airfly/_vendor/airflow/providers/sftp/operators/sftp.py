# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.models.baseoperator import BaseOperator


@immutable
class SFTPOperator(BaseOperator):
    ssh_hook: "_empty"
    ssh_conn_id: "_empty"
    remote_host: "_empty"
    local_filepath: "_empty"
    remote_filepath: "_empty"
    operation: "_empty"
    confirm: "_empty"
    create_intermediate_dirs: "_empty"
