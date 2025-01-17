import pdfplumber
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_data():
    try:
        data = []
        current_section = ""
        current_title = ""
        
        with pdfplumber.open("data/Gym_dream.pdf") as pdf:
            print("\n=== Iniciando carga de datos ===")
            
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            
            sections = text.split('\n')
            
            for line in sections:
                line = line.strip()
                if line:
                    # Si es un título de sección principal
                    if line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.')):
                        # Guardar sección anterior si existe
                        if current_section:
                            data.append({
                                "text": f"{current_title}\n{current_section.strip()}",
                                "title": current_title
                            })
                        current_title = line
                        current_section = ""
                    else:
                        current_section += line + "\n"
            
            # Guardar última sección
            if current_section:
                data.append({
                    "text": f"{current_title}\n{current_section.strip()}",
                    "title": current_title
                })
        
        print("\n=== Secciones procesadas ===")
        for i, item in enumerate(data, 1):
            print(f"\nSección {i}:")
            print("-" * 30)
            print(item['text'])
            print("-" * 30)
            
        return data
        
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        return []

if __name__ == "__main__":
    print("Ejecutando carga de datos directamente...")
    result = load_data()
    print(f"\nResultado final: {len(result)} secciones cargadas")
