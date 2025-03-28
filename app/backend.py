from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from vector_store import load_vector_store
from langchain.prompts import PromptTemplate
import yaml
from prompts import SYSTEM_TEMPLATE

# Cargar configuración desde config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

def handle_query(query, messages):
    # 1. CONFIGURACIÓN DEL LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=config["openai_api_key"]
    )
    
    # 2. RETRIEVAL: Obtener el vector store para búsqueda
    vector_store = load_vector_store()
    
    # 3. AUGMENTATION: Configurar el prompt que combinará el contexto recuperado
    prompt = PromptTemplate(
        template=SYSTEM_TEMPLATE,
        input_variables=["context", "chat_history", "question"]
    )
    
    # 4. GENERATION: Crear la cadena que combina recuperación y generación
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        # RETRIEVAL: Configura la búsqueda de documentos relevantes
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        # AUGMENTATION: Usa el prompt para combinar contexto y pregunta
        combine_docs_chain_kwargs={"prompt": prompt},
        return_source_documents=True,
        verbose=True
    )
    
    # Formatear el historial
    formatted_history = []
    for msg in messages[1:]:
        if isinstance(msg, dict) and msg["role"] == "user":
            formatted_history.append((msg["content"], ""))
    
    try:
        result = chain.invoke({
            "question": query,
            "chat_history": formatted_history
        })
        
        return result["answer"]
    except Exception as e:
        return """¡Hola! Soy el asistente especializado de DreamGym. 
Disculpa, tuve un problema técnico. ¿Podrías reformular tu pregunta?"""