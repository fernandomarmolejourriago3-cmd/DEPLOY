from nltk.chat.util import Chat, reflections

pares = [
    [r"hola|hi|hello|pola profe|hola profe fernando|hola fernando|fernando|compañero|hoa|hola instructor|instructor",
     ["¡Hola! ¿Cómo puedo ayudarte? 😊 Para conocer las opciones de asesoría escribe '0'."]],

    [r"profe|como estas",
     ["Bien 😄 ¿y tú cómo estás?"]],

    [r"1",
     ["Opción 1 seleccionada:\n✍️ Busca tu ficha en la pagina y consulta la nota en la pestaña Como Vamos"]],

    [r"2",
     ["Opción 2 seleccionada: 🗓️ Agenda con el profe para que te explique la actividad."]],

    [r"3",
     ["Opción 3 seleccionada:\n👉 Abre este enlace para consultar las calificaciones:\n"
      "https://docs.google.com/forms/d/e/1FAIpQLScT5XPto_HT4yC2GtXfhQFGKfznb47PgOnJDe3Zthm53Z3vrA/viewform?usp=dialog"]],

    [r"(.*)adiós|luego hablamos",
     ["¡Hasta luego! 👋 Escríbeme a este número de WhatsApp: 3052546933"]]
]

chat = Chat(pares, reflections)

def responder(mensaje):
    mensaje = mensaje.lower().strip()

    if mensaje == "1":
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







