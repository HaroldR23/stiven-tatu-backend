from domain.src.entities.schedule_appointment import ScheduleAppointment
from templates.get_email_footer import get_email_footer


def get_admin_email_template(customer_data: ScheduleAppointment) -> str:
    styles = ", ".join(customer_data.styles) if customer_data.styles else "N/A"

    def card(title, content):
        return f"""
        <table width="100%" cellpadding="0" cellspacing="0" 
               style="border: 1px solid #eee; border-radius: 8px;">
            <tr>
                <td style="padding: 14px;">
                    <p style="margin: 0 0 8px 0; font-weight: bold; color: #111;">
                        {title}
                    </p>
                    <div style="font-size: 13px; color: #555; line-height: 1.5;">
                        {content}
                    </div>
                </td>
            </tr>
        </table>
        """

    return f"""
    <table width="100%" cellpadding="0" cellspacing="0" style="font-family: Arial, sans-serif;">
        <tr>
            <td align="center">
                <table width="420" cellpadding="0" cellspacing="0">

                    <!-- Header -->
                    <tr>
                        <td align="center" style="padding: 20px 0;">
                            <p style="margin: 0; font-size: 18px; font-weight: bold;">
                                Nueva solicitud 💥
                            </p>
                        </td>
                    </tr>

                    <!-- GRID -->
                    <tr>
                        <td>

                            <table width="100%" cellpadding="0" cellspacing="0">
                                <tr>

                                    <!-- LEFT COLUMN -->
                                    <td width="50%" valign="top" style="padding-right: 6px;">
                                        {card("👤 Cliente", f'''
                                            <p><strong>Nombre:</strong> {customer_data.full_name}</p>
                                            <p><strong>Email:</strong> {customer_data.email}</p>
                                            <p><strong>Tel:</strong> {customer_data.phone}</p>
                                        ''')}
                                    </td>

                                    <!-- RIGHT COLUMN -->
                                    <td width="50%" valign="top" style="padding-left: 6px;">
                                        {card("🎨 Tatuaje", f'''
                                            <p><strong>Estilos:</strong> {styles}</p>
                                            <p><strong>Color:</strong> {customer_data.color}</p>
                                            <p><strong>Ubicación:</strong> {customer_data.location}</p>
                                            <p><strong>Tamaño:</strong> {customer_data.size}</p>
                                        ''')}
                                    </td>

                                </tr>

                                <!-- SECOND ROW -->
                                <tr>
                                    <td colspan="2" style="padding-top: 12px;">
                                        {card("📌 Información adicional", f'''
                                            <p><strong>Alergias:</strong> {customer_data.allergies}</p>
                                            <p><strong>Fecha:</strong> {customer_data.preferred_date}</p>
                                            <p><strong>Horario:</strong> {customer_data.preferred_time}</p>
                                            <p><strong>+18:</strong> {"Sí" if customer_data.is_over_18 else "No"}</p>
                                        ''')}
                                    </td>
                                </tr>

                            </table>

                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>

    {get_email_footer()}
    """
