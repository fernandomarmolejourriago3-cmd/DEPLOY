from nltk.chat.util import Chat, reflections

pares = [
    [r"hola|hi|hello|pola profe|hola profe fernando|hola fernando|fernando|compañero|hoa",
     ["¡Hola! ¿Cómo puedo ayudarte? 😊 Para conocer las opciones de asesoría escribe 'menú'."]],

    [r"profe|como estas",
     ["Bien 😄 ¿y tú cómo estás?"]],

    [r"1",
     ["Opción 1 seleccionada:\n👉 Abre este enlace para consultar las calificaciones:\n"
      "https://forms.office.com/r/YOURFORMID"]],

    [r"2",
     ["Opción 2 seleccionada: 🗓️ Agenda con el profe para que te explique la actividad."]],

    [r"3",
     ["Opción 3 seleccionada: ✍️ Escribe en el formulario, en el campo 'observación', el detalle (Nombre de Evidencia) que deseas validar nota."]],

    [r"(.*)adiós|luego hablamos",
     ["¡Hasta luego! 👋 Escríbeme a este número de WhatsApp: 3052546933"]]
]

chat = Chat(pares, reflections)

def responder(mensaje):
    mensaje = mensaje.lower().strip()

    if mensaje == "menú":
        return ("Selecciona una opción:\n"
                "1️⃣ Calificaciones\n"
                "2️⃣ No comprende la actividad\n"
                "3️⃣ Reclamo de nota")

    respuesta = chat.respond(mensaje)
    return respuesta or "No entendí, intenta con otra opción. 😅"


# Ejemplo de prueba:
if __name__ == "__main__":
    print("Chatbot iniciado (escribe 'salir' para terminar)\n")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == "salir":
            print("Chatbot: ¡Hasta luego! 👋")
            break
        print("Chatbot:", responder(entrada))



