
import shutil
import os
from pathlib import Path

# Configuración: Lista de patrones a OMITIR (usando la lógica de tu ejemplo)
# Si empieza con '!', lo ignoramos.
PATRONES_A_IGNORAR = [
    "__pycache__",
    "node_modules",
    ".vscode",
    "devenv",
    "admin_lib.zip",
    "package-lock.json",
    "!1.1.py"
]

def preparar_despliegue(origen, destino):
    # Borramos la carpeta de destino si ya existe para empezar de cero
    if os.path.exists(destino):
        shutil.rmtree(destino)
    
    # Función interna que decide qué ignorar
    def ignore_files(dir, files):
        ignorar = []
        for f in files:
            # Si el archivo o carpeta está en nuestra lista negra, lo añadimos
            if f in PATRONES_A_IGNORAR or f.endswith('.bat'):
                ignorar.append(f)
        return ignorar

    # Copiamos todo el proyecto aplicando el filtro
    shutil.copytree(origen, destino, ignore=ignore_files)
    print(f"✅ Proyecto listo en: {destino}")
    print(f"🚀 Archivos omitidos según tus reglas: {', '.join(PATRONES_A_IGNORAR)}")

# Ejecución
preparar_despliegue(origen='.', destino='./dist_para_subir')