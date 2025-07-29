"""
data_loader.py
-------------
Este módulo se encarga de cargar y procesar documentos PDF, en este caso,
contenido nutricional estructurado. Utiliza LangChain para dividir el texto
en fragmentos adecuados para un sistema RAG.

NUEVO: Se han añadido mejoras para:
- Conservar estructura por página
- Extraer tablas por separado
- Mejorar limpieza y separación semántica
"""

# Importaciones necesarias
import pdfplumber
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Ruta al documento PDF (ajústala si tu archivo tiene otro nombre o ubicación)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
PDF_PATH = os.path.join(PROJECT_ROOT, "data", "nutricion.pdf")  # ← Asegúrate de que esté ahí

def load_data():
    """
    Carga el PDF, extrae el texto y las tablas, y divide el contenido en chunks.

    Returns:
        list[str]: Lista de chunks de texto listos para procesamiento RAG.
    """
    if not os.path.exists(PDF_PATH):
        print(f"\nERROR: El archivo no se encuentra en la ruta: {PDF_PATH}")
        return []

    try:
        print("\n=== Iniciando carga de datos del PDF ===")

        pages_text = []

        # === EXTRAEMOS TEXTO Y TABLAS POR PÁGINA ===
        with pdfplumber.open(PDF_PATH) as pdf:
            for i, page in enumerate(pdf.pages):
                # 1. Extraer texto normal de la página
                text = page.extract_text()
                if text:
                    pages_text.append(f"=== Página {i+1} ===\n{text.strip()}")

                # 2. Extraer tablas, si existen, como bloques de texto legibles
                tables = page.extract_tables()
                for table in tables:
                    table_text = f"=== Tabla página {i+1} ===\n"
                    for row in table:
                        row_text = " | ".join(cell or "" for cell in row)
                        table_text += row_text + "\n"
                    pages_text.append(table_text.strip())

        # === UNIMOS TODO EL TEXTO Y LIMPIAMOS ESPACIOS INNECESARIOS ===
        full_text = "\n\n".join(pages_text)
        full_text = full_text.replace("\xa0", " ")  # Elimina espacios duros
        full_text = full_text.replace("  ", " ")    # Reemplaza dobles espacios

        print(f"Total de caracteres extraídos: {len(full_text)}")

        # === DIVIDIMOS EL TEXTO EN CHUNKS SEMÁNTICAMENTE COHERENTES ===
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,        # Aumentado para mantener contexto amplio
            chunk_overlap=150,      # Buen solapamiento entre fragmentos
            separators=["\n\n", "\n", ".", " "]  # De mayor a menor prioridad semántica
        )

        chunks = text_splitter.split_text(full_text)

        # === INFO DE EJEMPLO Y RETORNO ===
        print(f"\n=== Documento dividido en {len(chunks)} chunks ===")
        print("Ejemplo del primer chunk:")
        print("-" * 30)
        print(chunks[0])
        print("-" * 30)

        return chunks

    except Exception as e:
        print(f"\nERROR durante la carga o procesamiento del PDF: {str(e)}")
        return []

# Punto de entrada para pruebas locales
if __name__ == "__main__":
    print("Ejecutando carga de datos directamente...")
    result_chunks = load_data()
    if result_chunks:
        print(f"\nResultado final: {len(result_chunks)} chunks cargados exitosamente.")
