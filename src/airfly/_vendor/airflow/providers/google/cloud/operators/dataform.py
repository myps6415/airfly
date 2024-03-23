# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class DataformCreateCompilationResultOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    compilation_result: "CompilationResult | dict"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformGetCompilationResultOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    compilation_result_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformCreateWorkflowInvocationOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workflow_invocation: "WorkflowInvocation | dict"
    retry: "Retry | _MethodDefault"
    timeout: "int | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    asynchronous: "bool"
    wait_time: "int"


class DataformGetWorkflowInvocationOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workflow_invocation_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformQueryWorkflowInvocationActionsOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workflow_invocation_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformCancelWorkflowInvocationOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workflow_invocation_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformCreateRepositoryOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformDeleteRepositoryOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    force: "bool"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformCreateWorkspaceOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workspace_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformDeleteWorkspaceOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workspace_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformWriteFileOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workspace_id: "str"
    filepath: "str"
    contents: "bytes"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformMakeDirectoryOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workspace_id: "str"
    directory_path: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformRemoveFileOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workspace_id: "str"
    filepath: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformRemoveDirectoryOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workspace_id: "str"
    directory_path: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class DataformInstallNpmPackagesOperator(GoogleCloudBaseOperator):
    project_id: "str"
    region: "str"
    repository_id: "str"
    workspace_id: "str"
    retry: "Retry | _MethodDefault"
    timeout: "float | None"
    metadata: "Sequence[tuple[str, str]]"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"