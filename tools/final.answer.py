from smolagents import tool

@tool
def final_answer(resposta: str) -> str:
    """Retorna a resposta final formatada para o usuário.
    
    Args:
        resposta: A resposta final que o agente deve mostrar.
    """
    return f"✅ Resultado: {resposta}"
