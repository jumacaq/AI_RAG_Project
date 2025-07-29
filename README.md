# Nutrilac Bot: Tu Asistente Experto en nutrición preconcepcional, durante el embarazo y la lactancia.

Un chatbot inteligente que te permite "dialogar" con un documento sobre educación nutricional en la etapa preconcepcional, embarazo y lactancia.
En lugar de buscar manualmente, simplemente haz una pregunta y obtén respuestas precisas y contextualizadas sobre este tema, esta dirigido a padres primerizos o especialistas en nutrición que buscan mayor información de este tópico específico.

Este proyecto utiliza un pipeline de RAG (Retrieval Augmented Generation) con LangChain y OpenAI para ofrecer una herramienta de Q&A potente sobre un corpus de documentos extenso.

## 🚀 Características Clave

-   **Interfaz de Chat Intuitiva:** Construida con Streamlit para una experiencia de usuario limpia y sencilla.
-   **Q&A sobre Documentación:** Haz preguntas en lenguaje natural sobre la sintaxis, módulos, clases o funciones de Python.
-   **Respuestas Basadas en la Fuente:** El bot está instruido para basar sus respuestas únicamente en la documentación proporcionada, evitando invenciones.
-   **Procesamiento de Documentos Robusto:** Utiliza `RecursiveCharacterTextSplitter` de LangChain para dividir de forma inteligente documentos PDF complejos, manteniendo el contexto de código y párrafos.
-   **Monitorización de Costes:** Una barra lateral muestra en tiempo real los tokens utilizados y el coste en USD de cada consulta y del total de la sesión.

## 💻 Stack Tecnológico

-   **Frontend:** Streamlit
-   **Backend y Orquestación:** Python, LangChain
-   **Modelo de Lenguaje (LLM):** OpenAI gpt-4o-mini
-   **Base de Datos de Vectores:** ChromaDB
-   **Embeddings:** OpenAI Embeddings
-   **Procesamiento de Documentos:** PDFPlumber

## 🛠️ Instalación y Configuración

1.  **Clonar el Repositorio**
    ```bash
    git clone https://github.com/tu-usuario/docupy-bot.git
    cd docupy-bot
    ```

2.  **Crear y Activar un Entorno Virtual**
    ```bash
    # Crear el entorno
    python -m venv .venv

    # Activar en Windows
    .\.venv\Scripts\Activate.ps1

    # Activar en macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instalar Dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar tu API Key de OpenAI**
    -   Renombra el archivo `config.example.yaml` a `config.yaml`.
    -   Edita `config.yaml` y reemplaza `"your_openai_api_key"` con tu clave de API de OpenAI.

5.  **Añadir tu Documento**
    -   Coloca el archivo PDF que quieres que el bot analice dentro de la carpeta `data/`.
    -   Asegúrate de que el archivo `app/data_loader.py` apunte al nombre de tu documento (actualmente está configurado para `library.pdf`).

## 🚀 Ejecución

1.  **Borra la Base de Datos Antigua (Solo la primera vez o si cambias el PDF)**
    -   Si existe una carpeta llamada `vector_store/`, elimínala para forzar al sistema a re-indexar tu documento.

2.  **Iniciar la Aplicación**
    ```bash
    streamlit run app/app.py
    ```
    La primera vez que se ejecute, el proceso de indexación puede tardar varios minutos. En los siguientes inicios, la aplicación cargará la base de datos existente y arrancará casi al instante.

3.  **Chatea con tu Bot**
    -   Abre tu navegador y ve a `http://localhost:8501`.
    -   ¡Empieza a hacer preguntas sobre tu documento!

## 📁 Estructura del Proyecto

```
nutrilac-bot/
│
├── app/
│   ├── app.py               # Lógica del Frontend (Streamlit)
│   ├── backend.py           # Lógica del Backend (LangChain RAG)
│   ├── new_data_loader.py   # Carga y procesa el PDF
│   ├── new_prompts.py       # Contiene el prompt del sistema para el bot
|   ├── test_backend.py      # Archivo para probar el funcionamiento del backend
|   ├── test_vector_store.py # Archivo para probar el funcionamiento de la carga de archivos vectoriales en ChromaDB
│   └── vector_store.py      # Gestiona la creación y carga de la BD de vectores
│
├── data/
│   └── nutricion.pdf    # El documento fuente para el bot
│
├── vector_store/        # Directorio donde se guarda la BD de vectores (creado automáticamente)
│
├── config.example.yaml  # Tu fichero ejemplo de configuración con la API key
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Esta documentación
```

