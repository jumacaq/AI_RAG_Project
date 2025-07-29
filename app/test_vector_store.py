from vector_store import load_vector_store

vector_store = load_vector_store("nutricion_store")

if vector_store:
    print("\n✅ Vector store cargado exitosamente.")
    # Probar búsqueda con una consulta simple
    query = "¿Cuántas calorías tiene una manzana?"
    results = vector_store.similarity_search(query, k=2)
    
    print("\n🔎 Resultados de búsqueda:")
    for i, result in enumerate(results, 1):
        print(f"\nResultado {i}:\n{result.page_content}")
else:
    print("\n❌ No se pudo cargar el vector store.")
