import datetime
import time

def lambda_handler(event, context):
    # Gracias a la variable TZ, datetime.now() ya devuelve la hora local
    hora_actual = datetime.datetime.now()
    
    # También afecta a la librería time
    zona_nombre = time.tzname 

    print(f"La hora en Bogotá es: {hora_actual}")
    print(f"Zona horaria detectada: {zona_nombre}")
    
    return {
        'statusCode': 200,
        'body': f"Registro creado a las: {hora_actual}"
    }
    
    # Evita hacer esto manualmente si puedes usar la variable TZ
from datetime import timezone, timedelta
hora_bogota = datetime.datetime.now(timezone(timedelta(hours=-5)))
print(f" hora de bogota es {hora_bogota}")