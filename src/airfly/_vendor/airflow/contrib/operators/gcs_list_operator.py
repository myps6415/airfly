# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.providers.google.cloud.operators.gcs import (
    GCSListObjectsOperator,
)


@immutable
class GoogleCloudStorageListOperator(GCSListObjectsOperator):
    pass
