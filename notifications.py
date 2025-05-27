from prefect.events import Event, emit_event
from prefect import flow

def notify_success(flow_name: str):
  emit_event(
    event="prefect.flow-run.success",
    resource={"prefect.resource.id": f"flow/{flow_name}"},
    payload={"message": f"O flow '{flow_name}' foi concluído com sucesso!"},
  )

def notify_failure(flow_name: str):
  emit_event(
    event="prefect.flow-run.failed",
    resource={"prefect.resource.id": f"flow/{flow_name}"},
    payload={"message": f"O flow '{flow_name}' falhou!"},
  )