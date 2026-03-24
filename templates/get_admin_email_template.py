from domain.src.entities.schedule_appointment import ScheduleAppointment

def get_admin_email_template(customer_data: ScheduleAppointment) -> str:
    styles = ", ".join(customer_data.styles) if customer_data.styles else "N/A"
    return f"""
        <h2>Nueva solicitud de cotización recibida</h2>

        <h3>Datos del cliente</h3>
        <p><strong>Nombre:</strong> {customer_data.full_name}</p>
        <p><strong>Correo electrónico:</strong> {customer_data.email}</p>
        <p><strong>Teléfono:</strong> {customer_data.phone}</p>

        <h3>Detalles del tatuaje</h3>
        <p><strong>Estilos:</strong> {styles}</p>
        <p><strong>Color:</strong> {customer_data.color}</p>
        <p><strong>Ubicación:</strong> {customer_data.location}</p>
        <p><strong>Tamaño:</strong> {customer_data.size}</p>
        <p><strong>Idea:</strong> {customer_data.idea}</p>
        <p><strong>Artista solicitado:</strong> {customer_data.artist}</p>
        <p><strong>Referencia:</strong> {customer_data.reference}</p>

        <h3>Información adicional</h3>
        <p><strong>Alergias:</strong> {customer_data.allergies}</p>
        <p><strong>Fecha preferida:</strong> {customer_data.preferred_date}</p>
        <p><strong>Mayor de 18 años:</strong> {"Sí" if customer_data.is_over_18 else "No"}</p>
        <p><strong>Acepta política de privacidad:</strong> {"Sí" if customer_data.accepts_privacy else "No"}</p>
    """
