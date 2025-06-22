from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback
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
        retriever=vector_store.as_retriever(search_kwargs={"k": 10}),
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
        # Usar el callback para obtener las estadísticas
        with get_openai_callback() as cb:
            result = chain.invoke({
                "question": query,
                "chat_history": formatted_history
            })
            
            # Devolver un diccionario con la respuesta y las estadísticas
            return {
                "answer": result["answer"],
                "total_tokens": cb.total_tokens,
                "prompt_tokens": cb.prompt_tokens,
                "completion_tokens": cb.completion_tokens,
                "total_cost_usd": cb.total_cost
            }

    except Exception as e:
        # En caso de error, devolver un diccionario con valores por defecto
        return {
            "answer": "¡Hola! Soy DocuPy Bot. Disculpa, tuve un problema técnico. ¿Podrías reformular tu pregunta?",
            "total_tokens": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_cost_usd": 0
        }