def get_email_footer() -> str:
    return """
    <br/>
    <table width="100%" cellpadding="0" cellspacing="0" style="margin-top: 24px; font-family: Arial, sans-serif;">
        <tr>
            <td align="center">
                <table width="420" cellpadding="0" cellspacing="0" style="border-top: 1px solid #eaeaea; padding-top: 20px;">
                    
                    <!-- Brand -->
                    <tr>
                        <td align="center" style="padding-bottom: 12px;">
                            <p style="margin: 0; font-size: 18px; font-weight: bold; color: #111;">
                                STIVEN TATU
                            </p>
                            <p style="margin: 4px 0 0 0; font-size: 13px; color: #888;">
                                Tattoo Artist
                            </p>
                        </td>
                    </tr>

                    <!-- Divider -->
                    <tr>
                        <td align="center">
                            <div style="width: 40px; height: 2px; background-color: #111; margin: 12px 0;"></div>
                        </td>
                    </tr>

                    <!-- Contact -->
                    <tr>
                        <td align="center" style="font-size: 13px; color: #555; line-height: 1.6;">
                            
                            <p style="margin: 6px 0;">
                                📸 
                                <a href="https://www.instagram.com/stiventatu" target="_blank" 
                                   style="color: #111; text-decoration: none; font-weight: bold;">
                                   @stiventatu
                                </a>
                            </p>

                            <p style="margin: 6px 0;">
                                📞 +54 9 11 7364-7165
                            </p>

                        </td>
                    </tr>

                    <!-- Footer note -->
                    <tr>
                        <td align="center" style="padding-top: 14px;">
                            <p style="margin: 0; font-size: 11px; color: #aaa;">
                                © 2026 Stiven Tatu. All rights reserved.
                            </p>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>
    """