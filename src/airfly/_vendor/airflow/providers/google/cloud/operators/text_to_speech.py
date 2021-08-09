# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class CloudTextToSpeechSynthesizeOperator(BaseOperator):
    input_data: "typing.Union[typing.Dict, google.cloud.texttospeech_v1.types.SynthesisInput]"
    voice: "typing.Union[typing.Dict, google.cloud.texttospeech_v1.types.VoiceSelectionParams]"
    audio_config: "typing.Union[typing.Dict, google.cloud.texttospeech_v1.types.AudioConfig]"
    target_bucket_name: "str"
    target_filename: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"