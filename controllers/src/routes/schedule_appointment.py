from fastapi import APIRouter, Depends

from controllers.src.dependencies.schedule_appointment_dependencies import get_schedule_appointment_use_case
from controllers.src.dtos.schedule_request import ScheduleRequestDTO

schedule_appointment_router = APIRouter()

@schedule_appointment_router.post("/schedule")
async def schedule_appointment(schedule_request: ScheduleRequestDTO, schedule_appointment_use_case=Depends(get_schedule_appointment_use_case)):
    await schedule_appointment_use_case(schedule_request)
    return {"message": "Schedule appointment successfully received"}
