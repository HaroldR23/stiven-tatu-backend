def get_customer_email_template(customer_name: str) -> str:
    return f"""
        <h2>¡Hola, {customer_name}! Hemos recibido tu solicitud 🎉</h2>
        <p>Muchas gracias por contactarnos y por confiar en nosotros para tu próximo tatuaje. Nos alegra mucho tenerte aquí.</p>
        <p>En breve, alguien de nuestro equipo se pondrá en contacto contigo personalmente para conocer más detalles sobre tu idea, coordinar la cita y asegurarse de que todo quede exactamente como lo imaginas.</p>
        <p>Mientras tanto, si tienes alguna pregunta o quieres compartir más referencias, no dudes en respondernos este correo.</p>
        <p>¡Nos vemos pronto! 🖤<br/>El equipo de Stiven Tatu</p>
    """
