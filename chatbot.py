#This is the main file of the chatboot...
import tkinter as tk
import os

from knowledge_base import knowledge_base as kb
from utils.search import find_key_or_synonyms as sks

# Function to search an answer in the knowledge base...
def search_answer(qst):

    if qst is None:
        return "No has proporcionado nada"

    search_qst = qst.lower()

    word = sks(search_qst)

    # if the function returns none, I indicate that the question was not understood...
    if word is None:
        return "No entendi tu pregunta, ¿podrías proporcionar más información?"

    # if the function returned a word, I search taht word in the knowledge base the key to obtain the answer...
    # and return the answer to the user...
    for key, answer in kb.items():
        if key == word:
            return answer



# function for handling the interaction with the user in the GUI...
def send_msg():
    qst = input_user.get()
    answer = search_answer(qst)
    output_answer.config(state=tk.NORMAL)
    output_answer.insert(tk.END, "Tú: " + qst + "\n")
    output_answer.insert(tk.END, "Chatbot: " + answer + "\n\n")
    output_answer.config(state=tk.DISABLED)
    input_user.delete(0, tk.END)

# window configuration...
window = tk.Tk()
window.title("Chatboot de muebles y decoración")
window.geometry("500x600")

# output...
output_answer = tk.Text(window, height=30, width=60, state=tk.DISABLED, bg="white", fg="black")
output_answer.pack(pady=10)

#input user..
input_user = tk.Entry(window, width=40)
input_user.pack(pady=10)

# send button...
send_botton = tk.Button(window, text="Enviar", command=send_msg)
send_botton.pack()

# Iniciar la interfaz gráfica
window.mainloop()