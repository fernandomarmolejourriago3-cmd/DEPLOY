from Chatbot import crear_interfaz

app = crear_interfaz()

# Render ejecuta en el puerto 8080
if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=8080)
