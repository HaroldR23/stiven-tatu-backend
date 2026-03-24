from domain.src.ports.EmailVerifierService import EmailVerifierService
from domain.src.ports.CaptchaService import CaptchaService
from domain.src.ports.EmailSenderService import EmailSenderService
from use_cases.src.schedule_appointment.use_case import ScheduleAppointmentUseCase

class TurnstileCaptchaAdapter(CaptchaService):
    async def verify(self, token: str) -> dict:
        # Implementación de la verificación con Turnstile
        return {"success": True}  # Simulación de éxito
    
class EmailVerifierAdapter(EmailVerifierService):
    async def verify_email(self, email: str) -> bool:
        # Implementación de la verificación de correo electrónico
        return True  # Simulación de correo válido

class EmailSenderAdapter(EmailSenderService):
    async def send_email(self, body: str, recipient: str, subject: str) -> None:
        # Implementación del envío de correo electrónico
        pass  # Simulación de envío exitoso


def get_schedule_appointment_use_case():
    return ScheduleAppointmentUseCase(
        email_sender=EmailSenderAdapter(),
        captcha_verifier=TurnstileCaptchaAdapter(),
        email_verifier=EmailVerifierAdapter()
    )
