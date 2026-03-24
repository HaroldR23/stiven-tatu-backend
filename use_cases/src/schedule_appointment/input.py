from dataclasses import dataclass

from domain.src.entities.schedule_appointment import ScheduleAppointment

@dataclass
class ScheduleAppointmentInput(ScheduleAppointment):
    captcha_token: str
