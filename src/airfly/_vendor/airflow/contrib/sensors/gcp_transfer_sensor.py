# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.providers.google.cloud.sensors.cloud_storage_transfer_service import (
    CloudDataTransferServiceJobStatusSensor,
)


@immutable
class GCPTransferServiceWaitForJobStatusSensor(CloudDataTransferServiceJobStatusSensor):
    pass
