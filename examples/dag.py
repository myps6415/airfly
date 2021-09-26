# This file is auto-generated by airfly 0.6.0
from datetime import timedelta

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator
from airflow.utils.dates import days_ago

from examples.complex.catalog import _print_catalog
from examples.python_operator.workflow import (
    callable_virtualenv,
    my_sleeping_function,
    print_context,
)

# >>>>>>>>>> Include from 'params.py'
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
dag_kwargs = dict(
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["example"],
)
# <<<<<<<<<< End of code insertion
with DAG("examples", **dag_kwargs) as dag:
    examples_bash_operator_workflow_also_run_this = BashOperator(
        task_id="examples.bash_operator.workflow.also_run_this",
        bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
    )
    examples_bash_operator_workflow_run_this = BashOperator(
        task_id="examples.bash_operator.workflow.run_this", bash_command="echo 1"
    )
    examples_bash_operator_workflow_run_this_last = DummyOperator(
        task_id="examples.bash_operator.workflow.run_this_last"
    )
    examples_bash_operator_workflow_runme_0 = BashOperator(
        task_id="examples.bash_operator.workflow.runme_0",
        bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
    )
    examples_bash_operator_workflow_runme_1 = BashOperator(
        task_id="examples.bash_operator.workflow.runme_1",
        bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
    )
    examples_bash_operator_workflow_runme_2 = BashOperator(
        task_id="examples.bash_operator.workflow.runme_2",
        bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
    )
    examples_bash_operator_workflow_this_will_skip = BashOperator(
        task_id="examples.bash_operator.workflow.this_will_skip",
        bash_command='echo "hello world"; exit 99;',
    )
    examples_complex_catalog_search_catalog = PythonOperator(
        task_id="examples.complex.catalog.search_catalog",
        python_callable=_print_catalog,
    )
    examples_complex_catalog_search_catalog_result = BashOperator(
        task_id="examples.complex.catalog.search_catalog_result",
        bash_command="echo search_catalog_result",
    )
    examples_complex_entry_create_entry_gcs = BashOperator(
        task_id="examples.complex.entry.create_entry_gcs",
        bash_command="echo create_entry_gcs",
    )
    examples_complex_entry_create_entry_gcs_result = BashOperator(
        task_id="examples.complex.entry.create_entry_gcs_result",
        bash_command="echo create_entry_gcs_result",
    )
    examples_complex_entry_create_entry_gcs_result2 = BashOperator(
        task_id="examples.complex.entry.create_entry_gcs_result2",
        bash_command="echo create_entry_gcs_result",
    )
    examples_complex_entry_create_entry_group = BashOperator(
        task_id="examples.complex.entry.create_entry_group",
        bash_command="echo create_entry_group",
    )
    examples_complex_entry_create_entry_group_result = BashOperator(
        task_id="examples.complex.entry.create_entry_group_result",
        bash_command="echo create_entry_group_result",
    )
    examples_complex_entry_create_entry_group_result2 = BashOperator(
        task_id="examples.complex.entry.create_entry_group_result2",
        bash_command="echo create_entry_group_result2",
    )
    examples_complex_entry_delete_entry = BashOperator(
        task_id="examples.complex.entry.delete_entry", bash_command="echo delete_entry"
    )
    examples_complex_entry_delete_entry_group = BashOperator(
        task_id="examples.complex.entry.delete_entry_group",
        bash_command="echo delete_entry_group",
    )
    examples_complex_entry_get_entry = BashOperator(
        task_id="examples.complex.entry.get_entry", bash_command="echo get_entry"
    )
    examples_complex_entry_get_entry_group = BashOperator(
        task_id="examples.complex.entry.get_entry_group",
        bash_command="echo get_entry_group",
    )
    examples_complex_entry_get_entry_group_result = BashOperator(
        task_id="examples.complex.entry.get_entry_group_result",
        bash_command="echo get_entry_group_result",
    )
    examples_complex_entry_get_entry_result = BashOperator(
        task_id="examples.complex.entry.get_entry_result",
        bash_command="echo get_entry_result",
    )
    examples_complex_entry_lookup_entry = BashOperator(
        task_id="examples.complex.entry.lookup_entry", bash_command="echo lookup_entry"
    )
    examples_complex_entry_lookup_entry_result = BashOperator(
        task_id="examples.complex.entry.lookup_entry_result",
        bash_command="echo lookup_entry_result",
    )
    examples_complex_entry_update_entry = BashOperator(
        task_id="examples.complex.entry.update_entry", bash_command="echo update_entry"
    )
    examples_complex_tag_create_tag = BashOperator(
        task_id="examples.complex.tag.create_tag", bash_command="echo create_tag"
    )
    examples_complex_tag_create_tag_result = BashOperator(
        task_id="examples.complex.tag.create_tag_result",
        bash_command="echo create_tag_result",
    )
    examples_complex_tag_create_tag_result2 = BashOperator(
        task_id="examples.complex.tag.create_tag_result2",
        bash_command="echo create_tag_result2",
    )
    examples_complex_tag_create_tag_template = BashOperator(
        task_id="examples.complex.tag.create_tag_template",
        bash_command="echo create_tag_template",
    )
    examples_complex_tag_create_tag_template_field = BashOperator(
        task_id="examples.complex.tag.create_tag_template_field",
        bash_command="echo create_tag_template_field",
    )
    examples_complex_tag_create_tag_template_field_result = BashOperator(
        task_id="examples.complex.tag.create_tag_template_field_result",
        bash_command="echo create_tag_template_field_result",
    )
    examples_complex_tag_create_tag_template_field_result2 = BashOperator(
        task_id="examples.complex.tag.create_tag_template_field_result2",
        bash_command="echo create_tag_template_field_result2",
    )
    examples_complex_tag_create_tag_template_result = BashOperator(
        task_id="examples.complex.tag.create_tag_template_result",
        bash_command="echo create_tag_template_result",
    )
    examples_complex_tag_create_tag_template_result2 = BashOperator(
        task_id="examples.complex.tag.create_tag_template_result2",
        bash_command="echo create_tag_template_result2",
    )
    examples_complex_tag_delete_tag = BashOperator(
        task_id="examples.complex.tag.delete_tag", bash_command="echo delete_tag"
    )
    examples_complex_tag_delete_tag_template = BashOperator(
        task_id="examples.complex.tag.delete_tag_template",
        bash_command="echo delete_tag_template",
    )
    examples_complex_tag_delete_tag_template_field = BashOperator(
        task_id="examples.complex.tag.delete_tag_template_field",
        bash_command="echo delete_tag_template_field",
    )
    examples_complex_tag_get_tag_template = BashOperator(
        task_id="examples.complex.tag.get_tag_template",
        bash_command="echo get_tag_template",
    )
    examples_complex_tag_get_tag_template_result = BashOperator(
        task_id="examples.complex.tag.get_tag_template_result",
        bash_command="echo get_tag_template_result",
    )
    examples_complex_tag_list_tags = BashOperator(
        task_id="examples.complex.tag.list_tags", bash_command="echo list_tags"
    )
    examples_complex_tag_list_tags_result = BashOperator(
        task_id="examples.complex.tag.list_tags_result",
        bash_command="echo list_tags_result",
    )
    examples_complex_tag_rename_tag_template_field = BashOperator(
        task_id="examples.complex.tag.rename_tag_template_field",
        bash_command="echo rename_tag_template_field",
    )
    examples_complex_tag_update_tag = BashOperator(
        task_id="examples.complex.tag.update_tag", bash_command="echo update_tag"
    )
    examples_complex_tag_update_tag_template = BashOperator(
        task_id="examples.complex.tag.update_tag_template",
        bash_command="echo update_tag_template",
    )
    examples_complex_tag_update_tag_template_field = BashOperator(
        task_id="examples.complex.tag.update_tag_template_field",
        bash_command="echo update_tag_template_field",
    )
    examples_python_operator_workflow_run_this = PythonOperator(
        task_id="examples.python_operator.workflow.run_this",
        python_callable=print_context,
    )
    examples_python_operator_workflow_sleep_for_0 = PythonOperator(
        task_id="examples.python_operator.workflow.sleep_for_0",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 0},
    )
    examples_python_operator_workflow_sleep_for_1 = PythonOperator(
        task_id="examples.python_operator.workflow.sleep_for_1",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 1},
    )
    examples_python_operator_workflow_sleep_for_2 = PythonOperator(
        task_id="examples.python_operator.workflow.sleep_for_2",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 2},
    )
    examples_python_operator_workflow_sleep_for_3 = PythonOperator(
        task_id="examples.python_operator.workflow.sleep_for_3",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 3},
    )
    examples_python_operator_workflow_sleep_for_4 = PythonOperator(
        task_id="examples.python_operator.workflow.sleep_for_4",
        python_callable=my_sleeping_function,
        op_kwargs={"random_base": 4},
    )
    examples_python_operator_workflow_virtualenv_task = PythonVirtualenvOperator(
        task_id="examples.python_operator.workflow.virtualenv_task",
        python_callable=callable_virtualenv,
        requirements=["colorama==0.4.0"],
        system_site_packages=False,
    )
    examples_tutorial_demo_print_date = BashOperator(
        task_id="examples.tutorial.demo.print_date", bash_command="date"
    )
    examples_tutorial_demo_sleep = BashOperator(
        task_id="examples.tutorial.demo.sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )
    examples_tutorial_demo_templated = BashOperator(
        task_id="examples.tutorial.demo.templated",
        depends_on_past=False,
        bash_command="""
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
""",
        params={"my_param": "Parameter I passed in"},
    )
    (
        examples_bash_operator_workflow_also_run_this
        >> examples_bash_operator_workflow_run_this_last
    )
    (
        examples_bash_operator_workflow_run_this
        >> examples_bash_operator_workflow_run_this_last
    )
    examples_bash_operator_workflow_runme_0 >> examples_bash_operator_workflow_run_this
    examples_bash_operator_workflow_runme_1 >> examples_bash_operator_workflow_run_this
    examples_bash_operator_workflow_runme_2 >> examples_bash_operator_workflow_run_this
    (
        examples_bash_operator_workflow_this_will_skip
        >> examples_bash_operator_workflow_run_this_last
    )
    (
        examples_complex_catalog_search_catalog
        >> examples_complex_catalog_search_catalog_result
    )
    examples_complex_catalog_search_catalog >> examples_complex_entry_delete_entry
    examples_complex_catalog_search_catalog >> examples_complex_entry_delete_entry_group
    examples_complex_catalog_search_catalog >> examples_complex_tag_delete_tag
    examples_complex_catalog_search_catalog >> examples_complex_tag_delete_tag_template
    (
        examples_complex_catalog_search_catalog
        >> examples_complex_tag_delete_tag_template_field
    )
    examples_complex_entry_create_entry_gcs >> examples_complex_catalog_search_catalog
    (
        examples_complex_entry_create_entry_gcs
        >> examples_complex_entry_create_entry_gcs_result
    )
    (
        examples_complex_entry_create_entry_gcs
        >> examples_complex_entry_create_entry_gcs_result2
    )
    examples_complex_entry_create_entry_gcs >> examples_complex_entry_delete_entry
    examples_complex_entry_create_entry_gcs >> examples_complex_entry_get_entry
    examples_complex_entry_create_entry_gcs >> examples_complex_entry_lookup_entry
    examples_complex_entry_create_entry_gcs >> examples_complex_entry_update_entry
    examples_complex_entry_create_entry_gcs >> examples_complex_tag_create_tag_template
    examples_complex_entry_create_entry_group >> examples_complex_catalog_search_catalog
    examples_complex_entry_create_entry_group >> examples_complex_entry_create_entry_gcs
    (
        examples_complex_entry_create_entry_group
        >> examples_complex_entry_create_entry_group_result
    )
    (
        examples_complex_entry_create_entry_group
        >> examples_complex_entry_create_entry_group_result2
    )
    (
        examples_complex_entry_create_entry_group
        >> examples_complex_entry_delete_entry_group
    )
    examples_complex_entry_create_entry_group >> examples_complex_entry_get_entry_group
    examples_complex_entry_delete_entry_group >> examples_complex_entry_delete_entry
    examples_complex_entry_get_entry_group >> examples_complex_entry_delete_entry_group
    (
        examples_complex_entry_get_entry_group
        >> examples_complex_entry_get_entry_group_result
    )
    examples_complex_entry_get_entry >> examples_complex_entry_delete_entry
    examples_complex_entry_get_entry >> examples_complex_entry_get_entry_result
    examples_complex_entry_lookup_entry >> examples_complex_entry_delete_entry
    examples_complex_entry_lookup_entry >> examples_complex_entry_lookup_entry_result
    examples_complex_entry_update_entry >> examples_complex_entry_delete_entry
    (
        examples_complex_tag_create_tag_template_field
        >> examples_complex_catalog_search_catalog
    )
    (
        examples_complex_tag_create_tag_template_field
        >> examples_complex_tag_create_tag_template_field_result
    )
    (
        examples_complex_tag_create_tag_template_field
        >> examples_complex_tag_create_tag_template_field_result2
    )
    (
        examples_complex_tag_create_tag_template_field
        >> examples_complex_tag_delete_tag_template_field
    )
    (
        examples_complex_tag_create_tag_template_field
        >> examples_complex_tag_rename_tag_template_field
    )
    (
        examples_complex_tag_create_tag_template_field
        >> examples_complex_tag_update_tag_template_field
    )
    examples_complex_tag_create_tag_template >> examples_complex_catalog_search_catalog
    (
        examples_complex_tag_create_tag_template
        >> examples_complex_tag_create_tag_template_field
    )
    (
        examples_complex_tag_create_tag_template
        >> examples_complex_tag_create_tag_template_result
    )
    (
        examples_complex_tag_create_tag_template
        >> examples_complex_tag_create_tag_template_result2
    )
    (
        examples_complex_tag_create_tag_template
        >> examples_complex_tag_delete_tag_template_field
    )
    examples_complex_tag_create_tag_template >> examples_complex_tag_get_tag_template
    examples_complex_tag_create_tag_template >> examples_complex_tag_update_tag_template
    examples_complex_tag_create_tag >> examples_complex_catalog_search_catalog
    examples_complex_tag_create_tag >> examples_complex_tag_create_tag_result
    examples_complex_tag_create_tag >> examples_complex_tag_create_tag_result2
    examples_complex_tag_create_tag >> examples_complex_tag_delete_tag
    examples_complex_tag_create_tag >> examples_complex_tag_list_tags
    examples_complex_tag_create_tag >> examples_complex_tag_update_tag
    (
        examples_complex_tag_delete_tag_template_field
        >> examples_complex_tag_delete_tag_template
    )
    (
        examples_complex_tag_delete_tag_template
        >> examples_complex_entry_delete_entry_group
    )
    examples_complex_tag_delete_tag >> examples_complex_tag_delete_tag_template_field
    examples_complex_tag_get_tag_template >> examples_complex_tag_delete_tag_template
    (
        examples_complex_tag_get_tag_template
        >> examples_complex_tag_get_tag_template_result
    )
    examples_complex_tag_list_tags >> examples_complex_tag_delete_tag
    examples_complex_tag_list_tags >> examples_complex_tag_list_tags_result
    (
        examples_complex_tag_rename_tag_template_field
        >> examples_complex_tag_delete_tag_template_field
    )
    (
        examples_complex_tag_update_tag_template_field
        >> examples_complex_tag_rename_tag_template_field
    )
    examples_complex_tag_update_tag_template >> examples_complex_tag_delete_tag_template
    examples_complex_tag_update_tag >> examples_complex_tag_delete_tag
    (
        examples_python_operator_workflow_run_this
        >> examples_python_operator_workflow_sleep_for_0
    )
    (
        examples_python_operator_workflow_run_this
        >> examples_python_operator_workflow_sleep_for_1
    )
    (
        examples_python_operator_workflow_run_this
        >> examples_python_operator_workflow_sleep_for_2
    )
    (
        examples_python_operator_workflow_run_this
        >> examples_python_operator_workflow_sleep_for_3
    )
    (
        examples_python_operator_workflow_run_this
        >> examples_python_operator_workflow_sleep_for_4
    )
    examples_tutorial_demo_print_date >> examples_tutorial_demo_sleep
    examples_tutorial_demo_sleep >> examples_tutorial_demo_templated
