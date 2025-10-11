from nltk.chat.util import Chat, reflections

pares = [
    [r"hola|hi|hello|Hola Profe|Hola Profe fernando|Hola Fernando|Fernando|fernando|compañero|Compañero", ["¡Hola! ¿Como puedo Ayudarte?, para conocer las opciones de asesoria escribe "Menú""]],
    [r"Profe|Como estas", ["Bien y tu como estas"]],
    [r"1", ["Opción 1 seleccionada: En el formulario introduce el número de la Fase de la que desea conocer la calificación"]],
    [r"2", ["Opción 2 seleccionada: Agenda con el profe para que te explique la Actividad"]],
    [r"3", ["Opción 3 seleccionada: Escribe en el formulario campo observación el detalle (Nombre de Evidencia) que desea vaidar nota"]],
    [r"(.*) adiós|Luego hablamos", ["¡Hasta luego escribeme a este numero de Whatsapp = 3052546933!"]],
]

chat = Chat(pares, reflections)

def responder(mensaje):
    if mensaje.lower() in ["menu"]:
        return "Selecciona una opción:\n1️⃣ Calificaciones\n2️⃣ No Comprende la Actividad\n3️⃣ Reclamo de Nota"
    return chat.respond(mensaje) or "No entendí, intenta con otra opción."

