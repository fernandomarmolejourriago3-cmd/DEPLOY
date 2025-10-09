import os
import gradio as gr
from Chatbot import responder


port = int(os.environ.get("PORT", 7860))

# función que maneja el chat (Gradio maneja el historial internamente)
def chat_function(mensaje, historia):
    respuesta = responder(mensaje)
    return respuesta

# Interfaz moderna
demo = gr.ChatInterface(
    fn=chat_function,
    title="🤖 Chatbot en Render",
    description="Chat simple con opciones de texto",
    theme="soft",
)

demo.launch(server_name="0.0.0.0", server_port=port)

