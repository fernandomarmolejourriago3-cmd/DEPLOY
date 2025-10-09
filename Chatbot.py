from nltk.chat.util import Chat, reflections

pares = [
    [r"hola|hi|hello", ["¡Hola! ¿Qué deseas hacer?"]],
    [r"1", ["Opción 1 seleccionada: Información sobre el chatbot"]],
    [r"2", ["Opción 2 seleccionada: Saludos personalizados"]],
    [r"3", ["Opción 3 seleccionada: Despedida"]],
    [r"(.*) adiós", ["¡Hasta luego!"]],
]

chat = Chat(pares, reflections)

def responder(mensaje):
    if mensaje.lower() in ["menu", "opciones", "hola"]:
        return "Selecciona una opción:\n1️⃣ Información\n2️⃣ Saludos\n3️⃣ Despedida"
    return chat.respond(mensaje) or "No entendí, intenta con otra opción."
