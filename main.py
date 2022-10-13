from fastapi import FastAPI, File, UploadFile
from inspect_anomalies import inspect_anomalies
from send_alert import send_email

app = FastAPI()


@app.post("/data")
def upload(data: UploadFile = File(...)):
    returned_values = inspect_anomalies(data.file)

    for flag, bool in returned_values:
        if bool:
            send_email(flag)
            return f"Anomalies found in {flag} transactions"
