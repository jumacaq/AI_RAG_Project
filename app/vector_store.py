from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import yaml
import os
# import logging # Logging import will be removed as we are switching to print

# Determine the absolute path to the directory containing the current script (vector_store.py)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Go one level up to the project root directory
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
# Construct the absolute path to config.yaml
CONFIG_PATH = os.path.join(PROJECT_ROOT, "config.yaml")
# Construct the absolute path for the Chroma vector store persistence
VECTOR_STORE_DIR = os.path.join(PROJECT_ROOT, "vector_store")

# Load configuration from YAML file
# This section reads the 'config.yaml' file to get necessary configurations,
# like the OpenAI API key. It's crucial for the application to connect to OpenAI services.
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)

# logger = logging.getLogger(__name__) # Logger initialization will be removed

def initialize_vector_store(data):
    """
    Crea un almacén vectorial desde datos iniciales.
    """
    print("\n=== Inicializando Vector Store ===")
    
    if not data:
        print("ERROR: No hay datos para inicializar el vector store")
        return None
    
    try:
        embeddings = OpenAIEmbeddings(openai_api_key=config["openai_api_key"])
        
        # Crear chunks más pequeños para mejor búsqueda
        texts = []
        for item in data:
            # Dividir el texto en párrafos
            paragraphs = item['text'].split('\n\n')
            for paragraph in paragraphs:
                if paragraph.strip():
                    texts.append(paragraph.strip())
        
        print("\n=== Contenido a indexar ===")
        for i, text in enumerate(texts, 1):
            print(f"\nChunk {i}:")
            print("-" * 30)
            print(text)
            print("-" * 30)
        
        # Ensure the persist directory exists
        os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

        vector_store = Chroma.from_texts(
            texts=texts,
            embedding=embeddings,
            persist_directory=VECTOR_STORE_DIR
        )
        
        #vector_store.persist()
        print("\nVector Store creado y persistido correctamente en:", VECTOR_STORE_DIR)
        return vector_store
        
    except Exception as e:
        print(f"\nERROR al crear vector store: {str(e)}")
        return None

def load_vector_store():
    """
    Carga el almacén vectorial para búsqueda semántica
    """
    try:
        # Check if the vector store directory exists
        if not os.path.exists(VECTOR_STORE_DIR) or not os.listdir(VECTOR_STORE_DIR):
            # Using print instead of logger.warning
            print(f"ADVERTENCIA: El directorio de Vector Store ({VECTOR_STORE_DIR}) no existe o está vacío. Es posible que necesite inicialización.")
            return None

        embeddings = OpenAIEmbeddings(openai_api_key=config["openai_api_key"])
        vector_store = Chroma(
            persist_directory=VECTOR_STORE_DIR,
            embedding_function=embeddings
        )
        # Using print instead of logger.info
        print(f"INFO: Vector store cargado exitosamente desde: {VECTOR_STORE_DIR}")
        return vector_store
    except Exception as e:
        # Using print instead of logger.error
        print(f"ERROR: Error al cargar vector store desde {VECTOR_STORE_DIR}: {str(e)}")
        return None
