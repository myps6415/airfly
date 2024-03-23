# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.amazon.aws.operators.base_aws import (
    AwsBaseOperator,
)


class AppflowBaseOperator(AwsBaseOperator):
    flow_name: "str"
    flow_update: "bool"
    source: "str | None"
    source_field: "str | None"
    filter_date: "str | None"
    poll_interval: "int"
    max_attempts: "int"
    wait_for_completion: "bool"


class AppflowRunOperator(AppflowBaseOperator):
    flow_name: "str"
    source: "str | None"
    poll_interval: "int"
    wait_for_completion: "bool"


class AppflowRunFullOperator(AppflowBaseOperator):
    source: "str"
    flow_name: "str"
    poll_interval: "int"
    wait_for_completion: "bool"


class AppflowRunBeforeOperator(AppflowBaseOperator):
    source: "str"
    flow_name: "str"
    source_field: "str"
    filter_date: "str"
    poll_interval: "int"
    wait_for_completion: "bool"


class AppflowRunAfterOperator(AppflowBaseOperator):
    source: "str"
    flow_name: "str"
    source_field: "str"
    filter_date: "str"
    poll_interval: "int"
    wait_for_completion: "bool"


class AppflowRunDailyOperator(AppflowBaseOperator):
    source: "str"
    flow_name: "str"
    source_field: "str"
    filter_date: "str"
    poll_interval: "int"
    wait_for_completion: "bool"