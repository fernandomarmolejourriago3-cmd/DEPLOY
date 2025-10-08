import os
import gradio as gr
from Chatbot import chat_function  # ejemplo de import

port = int(os.environ.get("PORT", 7860))

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    msg.submit(chat_function, msg, chatbot)

demo.launch(server_name="0.0.0.0", server_port=port)
