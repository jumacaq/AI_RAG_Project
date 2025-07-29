# initialize_vectors.py
from app.new_data_loader import load_data
from app.vector_store import initialize_vector_store

def main():
    print("\n===> Comenzando proceso de carga y vectorización <===")
    
    chunks = load_data()
    if not chunks:
        print("❌ No se pudo cargar el texto del PDF.")
        return

    store = initialize_vector_store(chunks)
    if store:
        print("✅ Vector store creado y guardado con éxito.")
    else:
        print("❌ Error al crear el vector store.")

if __name__ == "__main__":
    main()
