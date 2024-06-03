from fastapi import FastAPI
from services.brevo import send_email
from services.ses import EmailService


app = FastAPI()


@app.get("/ses/")
async def root():
    send_email(
        to_email="youremail@gmail.com",
        subject="Is Python SDK work done?",
        text_content="Hi Sourabh,\nIs Python SDK work complete or not?")
    return {"message": "Hello World"}