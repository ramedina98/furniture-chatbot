#This is the main file of the chatboot...
import tkinter as tk
import os

from knowledge_base import knowledge_base

# Function to search an answer in the knowledge base...
def search_answer(qst):
    search_qst = qst.lower()

    for key, answer in knowledge_base.items():
        if key in search_qst:
            return answer
    return "No he entendido completamente tu pregunta. ¿Podrías proporcionar más detalles?"

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