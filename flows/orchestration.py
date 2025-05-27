from prefect import flow
from scripts.pipeline_flow import spotify_pipeline
from flows.transform_from_s3 import transform_from_s3_flow
from notifications import notify_success, notify_failure
from datetime import date

@flow(name="orchestrator_flow")
def orchestrator_flow():
		try:
			today_str = date.today().isoformat()

			spotify_pipeline(date_str=today_str)
			transform_from_s3_flow(date_str=today_str)

			notify_success("orchestrator_flow")

		except Exception as e:
			notify_failure("orchestrator_flow")
			raise e
    

if __name__ == "__main__":
    orchestrator_flow()