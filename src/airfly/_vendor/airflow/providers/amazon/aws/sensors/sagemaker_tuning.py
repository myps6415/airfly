# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.sensors.sagemaker_base import (
    SageMakerBaseSensor,
)


class SageMakerTuningSensor(SageMakerBaseSensor):
    job_name: "str"