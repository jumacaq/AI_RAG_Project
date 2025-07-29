from backend import handle_query

messages = [
    {"role": "bot", "content": "¡Hola! Soy Nutrilac - Bot. ¿En qué puedo ayudarte hoy?"},
    {"role": "user", "content": "¿Qué alimentos son ricos en ácido fólico?"},
    {"role": "bot", "content": "Los alimentos ricos en ácido fólico incluyen...(respuesta de ejemplo)"},
]

query = "¿Qué alimentos aconsejados en la etapa preconcepcional?"

result = handle_query(query, messages)

print("Respuesta del bot:", result["answer"])
print("\n Estadísticas:")
print("Total de tokens:", result["total_tokens"])
print("Tokens del prompt:", result["prompt_tokens"])
print("Tokens de la respuesta:", result["completion_tokens"])
print("Coste total (USD):", result["total_cost_usd"])