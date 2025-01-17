from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import yaml
import os
import logging

# Cargar configuración desde config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

logger = logging.getLogger(__name__)

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
        
        vector_store = Chroma.from_texts(
            texts=texts,
            embedding=embeddings,
            persist_directory="vector_store"
        )
        
        vector_store.persist()
        print("\nVector Store creado y persistido correctamente")
        return vector_store
        
    except Exception as e:
        print(f"\nERROR al crear vector store: {str(e)}")
        return None

def load_vector_store():
    """
    Carga el almacén vectorial persistido.
    """
    try:
        embeddings = OpenAIEmbeddings(openai_api_key=config["openai_api_key"])
        vector_store = Chroma(
            persist_directory="vector_store",
            embedding_function=embeddings
        )
        logger.info("Vector store cargado exitosamente")
        return vector_store
    except Exception as e:
        logger.error(f"Error al cargar vector store: {str(e)}")
        return None
