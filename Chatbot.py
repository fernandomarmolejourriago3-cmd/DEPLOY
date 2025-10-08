
import gradio as gr
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

# Función de respuesta
def responder(mensaje):
    if mensaje.lower() in ["menu", "opciones", "hola"]:
        return "Selecciona una opción:\n1️⃣ Información\n2️⃣ Saludos\n3️⃣ Despedida"
    return chat.respond(mensaje) or "No entendí, intenta con otra opción."

# Interfaz con entrada de texto y botones
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Chatbot con Opciones")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Escribe tu mensaje o selecciona una opción")
    botones = gr.Row()
    b1 = gr.Button("1️⃣ Información")
    b2 = gr.Button("2️⃣ Saludos")
    b3 = gr.Button("3️⃣ Despedida")

    def respuesta_bot(mensaje, historia):
        historia.append(("Tú", mensaje))
        r = responder(mensaje)
        historia.append(("Bot", r))
        return "", historia

    msg.submit(respuesta_bot, [msg, chatbot], [msg, chatbot])
    b1.click(lambda h: respuesta_bot("1", h), [chatbot], [msg, chatbot])
    b2.click(lambda h: respuesta_bot("2", h), [chatbot], [msg, chatbot])
    b3.click(lambda h: respuesta_bot("3", h), [chatbot], [msg, chatbot])

demo.launch()