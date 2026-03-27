from adapters.services.EmailSenderAdapter import EmailSenderAdapter
from adapters.services.EmailVerifierAdapter import EmailVerifierAdapter
from adapters.services.TurnstileCaptchaAdapter import TurnstileCaptchaAdapter
from use_cases.src.schedule_appointment.use_case import ScheduleAppointmentUseCase

def get_schedule_appointment_use_case():
    return ScheduleAppointmentUseCase(
        email_sender=EmailSenderAdapter(),
        captcha_verifier=TurnstileCaptchaAdapter(),
        email_verifier=EmailVerifierAdapter()
    )
