from templates.get_email_footer import get_email_footer


def get_customer_email_template(customer_name: str) -> str:
    return f"""
    <table width="100%" cellpadding="0" cellspacing="0" style="font-family: Arial, sans-serif;">
        <tr>
            <td align="center">
                <table width="420" cellpadding="0" cellspacing="0">

                    <!-- Header -->
                    <tr>
                        <td align="center" style="padding: 24px 0;">
                            <p style="margin: 0; font-size: 20px; font-weight: bold; color: #111;">
                                ¡Hola, {customer_name}! 🖤
                            </p>
                        </td>
                    </tr>

                    <!-- Divider -->
                    <tr>
                        <td align="center">
                            <div style="width: 40px; height: 2px; background-color: #111; margin: 12px 0;"></div>
                        </td>
                    </tr>

                    <!-- Content -->
                    <tr>
                        <td style="padding: 12px 0; color: #555; font-size: 14px; line-height: 1.6;">
                            
                            <p>
                                Hemos recibido tu solicitud y estamos muy emocionados de trabajar contigo ✨
                            </p>

                            <p>
                                En breve, alguien de nuestro equipo te contactará para definir todos los detalles
                                y asegurarnos de que tu tatuaje quede exactamente como lo imaginas.
                            </p>

                            <p style="margin-top: 16px;">
                                Nos vemos pronto,<br/>
                                <strong>Stiven Tatu</strong>
                            </p>

                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>
    {get_email_footer()}
    """