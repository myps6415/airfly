# airfly: auto generate Airflow's `dag.py` on the fly

Pipeline management is essential for data operation in company, many engineering teams rely on tools like Airflow to help them organize workflows, such as ETL, data analytic jobs or machine learning projects.

Airflow provides rich extensibility to let developers arrange workloads into a sequence of "operators", then they declare the task dependencies within a `DAG` context while writing the `dag.py` file. 

As workflow grows progressively, the increasing complexity of task relations prones to messing up the dag structure, leads to decrease of code maintainability, especially in collaborative scenarios.

`airfly` tries to mitigate such pain-points and brings automation to this development life cycle, it assumes all tasks are managed in certain python module, developers specify the dependencies while defining the task objects. During deployment, `airfly` can resolve the dependency tree and automatically build the `dag.py` for you.

## Usage

`airfly` expects the implementations are populated in a Python module(or package), the task dependencies are declared by assigning `upstreams` and `downstreams` attributes to each object. The task objects are actually wrappers for Airflow operators, when `airfly` walks through the entire module, all tasks are discovered and collected, the dependency tree and the `DAG` context are automatically built, with some `ast` helpers, `airfly` can wrap all these information, convert them into python code, and finally save them to `dag.py`.

<img src="assets/layout.png" width="500">


### Wrap Airflow operator with `AirflowTask`

In order to do codegen, collect the operator's metadata into a `AirflowTask` subclass as following(see [demo](./examples/demo.py)):

```python
# in demo.py
from airfly.model.airflow import AirflowTask


class print_date(AirflowTask):
    operator_class = "BashOperator" 
    params = dict(bash_command="date")
```

* `operator_class` specifies the class of the Airflow operator.
* The class name(`print_date`) will be mapped to `task_id` to the applied operator after code generation.
* `params` will be passed to operator as keyword argument.


### Declare task dependency

Use `upstreams` and `downstreams` to specify task dependencies.

```python
# in demo.py

from textwrap import dedent


templated_command = dedent(
    """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""
)

class templated(AirflowTask):
    operator_class = "BashOperator"
    params = dict(depends_on_past=False,
                  bash_command=templated_command,
                  params={"my_param": "Parameter I passed in"})


class sleep(AirflowTask):
    operator_class = "BashOperator"
    params = dict(depends_on_past=False, 
                  bash_command="sleep 5",
                  retries=3)

    upstreams = print_date
    downstreams = (templated,)
```


### Generate the `dag.py` file
By commandline interface:
```
$ airfly --name demo_dag --modname demo > dag.py
```

The outputs in `dag.py`:

```python
# This file is auto-generated by airfly 0.5.0
from airflow.models import DAG
from airflow.operators.bash import BashOperator

with DAG("demo_dag") as dag:
    demo_print_date = BashOperator(task_id="demo.print_date", bash_command="date")
    demo_sleep = BashOperator(
        task_id="demo.sleep", depends_on_past=False, bash_command="sleep 5", retries=3
    )
    demo_templated = BashOperator(
        task_id="demo.templated",
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
    demo_print_date >> demo_sleep
    demo_sleep >> demo_templated
```


## Inject parameters to `DAG`

If any additional arguments are needed, write and manage those configurations in a python file(see [demo](./examples/demo_params.py)), `airfly` can pass them to `DAG` during codegen.

```python
# in demo_params.py

from datetime import timedelta

from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag_kwargs = dict(
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["example"],
)
```

Inject those arguments by giving `--dag-params` option:
```
$ airfly --name demo_dag --modname demo --dag-params demo_params.py:dag_kwargs > dag.py
```

The outputs in `dag.py`:
```python
# This file is auto-generated by airfly 0.5.0
from datetime import timedelta

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# >>>>>>>>>> Include from 'demo_params.py'
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
with DAG("demo_dag", **dag_kwargs) as dag:
    demo_print_date = BashOperator(task_id="demo.print_date", bash_command="date")
    demo_sleep = BashOperator(
        task_id="demo.sleep", depends_on_past=False, bash_command="sleep 5", retries=3
    )
    demo_templated = BashOperator(
        task_id="demo.templated",
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
    demo_print_date >> demo_sleep
    demo_sleep >> demo_templated
```

`airfly` wraps required information including variables and imports into output python script, and pass the specified value to `DAG` object.


## Exclude tasks from codegen
By passing `--exclude-pattern` to match any unwanted objects with their `__qualname__`. then filter them out.
```
$ airfly --name demo_dag --modname demo --exclude-pattern templated > dag.py
excluding demo.templated
```

The outputs in `dag.py`:

```python
# This file is auto-generated by airfly 0.5.0
from airflow.models import DAG
from airflow.operators.bash import BashOperator

with DAG("demo_dag") as dag:
    demo_print_date = BashOperator(task_id="demo.print_date", bash_command="date")
    demo_sleep = BashOperator(
        task_id="demo.sleep", depends_on_past=False, bash_command="sleep 5", retries=3
    )
    demo_print_date >> demo_sleep
```

The `templated` task is gone.
