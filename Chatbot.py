from nltk.chat.util import Chat, reflections

# Pares de patrones y respuestas
pares = [
    [r"hola|hi|hello", ["¡Hola! ¿Qué deseas hacer?"]],
    [r"1", ["Opción 1 seleccionada: Información sobre el chatbot"]],
    [r"2", ["Opción 2 seleccionada: Saludos personalizados"]],
    [r"3", ["Opción 3 seleccionada: Despedida"]],
    [r"(.*) adiós", ["¡Hasta luego!"]],
]

chat = Chat(pares, reflections)

# Función para responder
def responder(mensaje):
    if mensaje.lower() in ["menu", "opciones", "hola"]:
        return "Selecciona una opción:\n1️⃣ Información\n2️⃣ Saludos\n3️⃣ Despedida"
    return chat.respond(mensaje) or "No entendí, intenta con otra opción."

# ✅ Esta función usa el nuevo formato requerido por Gradio (type="messages")
def chat_function(mensaje, historia):
    if historia is None:
        historia = []

    # Agregar mensaje del usuario
    historia.append({"role": "user", "content": mensaje})

    # Generar respuesta
    respuesta = responder(mensaje)

    # Agregar respuesta del bot
    historia.append({"role": "assistant", "content": respuesta})

    # Gradio espera una tupla: (nuevo_texto, nueva_historia)
    return "", historia
