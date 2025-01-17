# Gym Assistant Bot 🤖

Un chatbot inteligente especializado para el gimnasio DreamGym, construido con tecnologías modernas de procesamiento de lenguaje natural.

## 🚀 Características

- Interfaz de chat intuitiva y amigable
- Respuestas contextuales basadas en la información del gimnasio
- Procesamiento de lenguaje natural avanzado
- Búsqueda semántica de información
- Persistencia del historial de conversación

## 💻 Tecnologías Utilizadas

- **Frontend:** Streamlit
- **Backend:** Python, LangChain
- **LLM:** OpenAI GPT-3.5-turbo
- **Vector Store:** Chroma
- **Embeddings:** OpenAI Embeddings
- **Procesamiento de Datos:** PDFPlumber

## 📋 Requisitos Previos

- Python 3.8+
- Cuenta de OpenAI con API key
- Entorno virtual de Python

## 🛠️ Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/gym-assistant-bot.git
   cd gym-assistant-bot
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv gym-assistant-env

   # Windows
   .\gym-assistant-env\Scripts\activate

   # macOS/Linux
   source gym-assistant-env/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar API key**
   - Copia `config.example.yaml` a `config.yaml`
   - Reemplaza "tu-api-key-aqui" con tu API key de OpenAI
   ```yaml
   cp config.example.yaml config.yaml
   # Edita config.yaml con tu API key
   ```

## 🚀 Uso

1. **Iniciar la aplicación**
   ```bash
   streamlit run app/app.py
   ```

2. **Acceder al chatbot**
   - Abrir navegador en `http://localhost:8501`
   - Comenzar a chatear con el asistente

## 💰 Costos de Uso

### Precios por 1M tokens:
- **GPT-3.5-turbo:**
  - Input: $0.50
  - Output: $1.50
- **Embeddings:** $0.50

### Costo por conversación típica (300 tokens):
- Primera conversación (con embeddings): $0.00075
- Conversaciones siguientes: $0.00035

## 📁 Estructura del Proyecto
gym-assistant-bot/
├── app/
│ ├── app.py # Interfaz de usuario Streamlit
│ ├── backend.py # Lógica de procesamiento
│ ├── data_loader.py # Carga de datos del PDF
│ ├── prompts.py # Templates de prompts
│ └── vector_store.py # Gestión de embeddings
├── data/
│ └── Gym_dream.pdf # Datos del gimnasio
├── config.yaml # Configuración
├── requirements.txt # Dependencias
└── README.md # Documentación



## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para detalles


---
⌨️ con ❤️ por [Tu Nombre](https://github.com/tu-usuario)