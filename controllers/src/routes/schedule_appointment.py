from fastapi import APIRouter, Depends, Request

schedule_appointment_router = APIRouter()

@schedule_appointment_router.post("/quote-request")
async def schedule_appointment():
    return {"message": "Schedule appointment endpoint"}
