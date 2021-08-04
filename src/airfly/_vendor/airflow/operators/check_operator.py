# Auto generated by 'inv collect-airflow'
from airfly._ast import immutable
from airfly._vendor.airflow.operators.sql import (
    SQLCheckOperator,
    SQLIntervalCheckOperator,
    SQLThresholdCheckOperator,
    SQLValueCheckOperator,
)


@immutable
class CheckOperator(SQLCheckOperator):
    pass


@immutable
class IntervalCheckOperator(SQLIntervalCheckOperator):
    pass


@immutable
class ThresholdCheckOperator(SQLThresholdCheckOperator):
    pass


@immutable
class ValueCheckOperator(SQLValueCheckOperator):
    pass
