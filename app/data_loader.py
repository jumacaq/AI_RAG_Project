"""
data_loader.py
-------------
Este módulo se encarga de cargar y procesar el archivo PDF del gimnasio.
Convierte el contenido del PDF en un formato estructurado que puede ser 
utilizado por el sistema RAG (Retrieval Augmented Generation).

Principales funciones:
- load_data(): Carga y procesa el PDF, dividiendo el contenido en secciones
"""

# Importaciones necesarias para el procesamiento de PDFs
import pdfplumber  # Para extraer texto de PDFs
# import logging     # Logging import will be removed
import os         # Para operaciones del sistema de archivos

# Configuración básica del sistema de logging - THIS BLOCK WILL BE REMOVED
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__) # Logger initialization will be removed

def load_data():
    """
    Carga y procesa el PDF del gimnasio, extrayendo su contenido y 
    organizándolo en secciones estructuradas.

    Returns:
        list: Lista de diccionarios con el siguiente formato:
            {
                "text": str (contenido completo de la sección),
                "title": str (título de la sección)
            }
            
    Proceso:
    1. Abre el PDF usando pdfplumber
    2. Extrae el texto completo
    3. Divide el contenido en secciones basadas en títulos numerados
    4. Organiza el contenido en una estructura de datos manejable
    """
    try:
        # Inicialización de variables para almacenar datos procesados
        data = []                # Lista final de secciones
        current_section = ""     # Almacena el contenido de la sección actual
        current_title = ""       # Almacena el título de la sección actual
        
        # Abrir y procesar el PDF
        with pdfplumber.open("data/Gym_dream.pdf") as pdf:
            print("\n=== Iniciando carga de datos ===")
            
            # Extraer todo el texto del PDF y concatenarlo
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            
            # Dividir el texto en líneas para procesamiento
            sections = text.split('\n')
            
            # Procesar cada línea del texto
            for line in sections:
                line = line.strip() #elimina espacios en blanco al principio y al final
                if line:
                    # Detectar si la línea es un título de sección principal
                    # Los títulos comienzan con números del 1 al 8 seguidos de punto
                    if line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.')):
                        # Si hay una sección anterior pendiente, guardarla antes de la nueva
                        if current_section:
                            data.append({
                                "text": f"{current_title}\n{current_section.strip()}",
                                "title": current_title
                            })
                        # Iniciar nueva sección
                        current_title = line
                        current_section = ""
                    else:
                        # Agregar línea al contenido de la sección actual
                        current_section += line + "\n"
            
            # Guardar la última sección procesada (para no perder la última parte)
            if current_section:
                data.append({
                    "text": f"{current_title}\n{current_section.strip()}",
                    "title": current_title
                })
        
        # Mostrar las secciones procesadas para verificación
        print("\n=== Secciones procesadas ===")
        for i, item in enumerate(data, 1):
            print(f"\nSección {i}:")
            print("-" * 30)
            print(item['text'])
            print("-" * 30)
            
        return data
        
    except Exception as e:
        # En caso de error, registrar y devolver lista vacía
        print(f"\nERROR: {str(e)}")
        return []

# Punto de entrada para ejecución directa del script
if __name__ == "__main__":
    print("Ejecutando carga de datos directamente...")
    result = load_data()
    print(f"\nResultado final: {len(result)} secciones cargadas")
