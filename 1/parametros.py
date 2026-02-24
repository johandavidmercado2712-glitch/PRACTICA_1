import os

def obtener_configuracion():
    # Detectamos el entorno. Si no hay ninguno, por defecto es 'dev'
    entorno = os.environ.get('STAGE', 'dev').lower()
    
    print(f"--- Configurando sistema para: {entorno.upper()} ---")

    if entorno == 'pdn':
        # En PRODUCCIÓN: Usamos datos reales y máxima seguridad
        config = {
            "db_url": "pro-db-cluster.aws.com",
            "timeout": 5,        # Respuesta rápida
            "recursos": 5,       # "Aprovisionados: 5" como en tu ejemplo
            "debug": False       # No mostramos errores detallados al usuario
        }
    elif entorno == 'dev':
        # En DESARROLLO: Usamos datos de prueba y somos flexibles
        config = {
            "db_url": "localhost:5432",
            "timeout": 30,       # Más tiempo para debuguear
            "recursos": 1,       # "Aprovisionado: 1" (ahorro de costos)
            "debug": True        # Queremos ver todos los errores
        }
    else:
        config = {"error": "Entorno no reconocido"}
        
    return config

# --- SIMULACIÓN DE EJECUCIÓN ---
mi_config = obtener_configuracion()

print(f"Conectando a base de datos: {mi_config['db_url']}")
print(f"Potencia del servidor: {mi_config['recursos']} unidades")