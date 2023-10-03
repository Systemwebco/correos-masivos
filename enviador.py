import smtplib
import time
from email.message import EmailMessage

# Configuración del servidor SMTP y credenciales
smtp_server = 'tu_servidor_smtp'
smtp_port = 587  # Puerto del servidor SMTP
smtp_username = 'tu_direccion_de_correo@gmail.com'
smtp_password = 'tu_contrasena'

# Leer el asunto y cuerpo del correo desde archivos de texto
with open('asunto.txt', 'r') as archivo_asunto, open('cuerpo.txt', 'r') as archivo_cuerpo:
    asunto = archivo_asunto.read()
    cuerpo = archivo_cuerpo.read()

# Leer las direcciones de correo electrónico desde un archivo de texto
with open('lista_de_correos.txt', 'r') as archivo:
    direcciones_correo = archivo.readlines()

# Función para enviar el correo electrónico a una lista de destinatarios
def enviar_correo(destinatario):
    mensaje = EmailMessage()
    mensaje.set_content(cuerpo)
    mensaje['Subject'] = asunto
    mensaje['From'] = smtp_username
    mensaje['To'] = destinatario

    try:
        # Establecer conexión con el servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Iniciar cifrado TLS
        server.login(smtp_username, smtp_password)  # Iniciar sesión en el servidor SMTP
        server.send_message(mensaje)  # Enviar el correo electrónico
        server.quit()  # Cerrar la conexión con el servidor SMTP
        print(f'Correo enviado exitosamente a {destinatario}')
    except Exception as e:
        print(f'Error al enviar el correo a {destinatario}: {str(e)}')

# Bucle para enviar correos a cada dirección de correo en la lista
intervalo_segundos = 3600  # Intervalo de tiempo entre correos (por ejemplo, 1 hora)

while True:
    for direccion_correo in direcciones_correo:
        enviar_correo(direccion_correo.strip())  # Eliminar espacios en blanco y saltos de línea
        time.sleep(intervalo_segundos)  # Esperar el intervalo de tiempo antes de enviar el próximo correo
