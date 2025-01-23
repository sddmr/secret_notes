import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64


def encrypt_message(message, key):
    key = key.ljust(32)[:32].encode('utf-8')  # Align the key to 32 bytes
    iv = os.urandom(16)  # Generate random IV

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode('utf-8')) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_message_base64 = base64.b64encode(iv + encrypted_message).decode('utf-8')
    return encrypted_message_base64


def decrypt_message(encrypted_message_base64, key):
    key = key.ljust(32)[:32].encode('utf-8')
    encrypted_message = base64.b64decode(encrypted_message_base64)

    iv = encrypted_message[:16]
    encrypted_message = encrypted_message[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_message) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode('utf-8')


def save_note():
    title = title_entry.get().strip()
    note_content = text_box.get("1.0", tk.END).strip()
    key = master_key_entry.get().strip()

    if not title or not note_content or not key:
        messagebox.showerror("Error", "Please enter title, note content, and master key.")
        return

    encrypted_message = encrypt_message(note_content, key)

    file_name = "secret.txt"
    file_path = os.path.join(os.getcwd(), file_name)

    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"\n{title}\n")
            file.write(encrypted_message)
        messagebox.showinfo("Success", f"Note saved as '{file_path}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}")


def decrypt_note():
    key = master_key_entry.get().strip()

    if not key:
        messagebox.showerror("Error", "Please enter the master key to decrypt.")
        return

    file_name = "secret.txt"
    file_path = os.path.join(os.getcwd(), file_name)

    if not os.path.exists(file_path):
        messagebox.showerror("Error", "The file does not exist.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            title = file.readline().strip()
            encrypted_message = file.read()

        decrypted_message = decrypt_message(encrypted_message, key)
        messagebox.showinfo("Decrypted Note", f"Title: {title}\n\n{decrypted_message}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decrypt file:\n{e}")


root = tk.Tk()
root.geometry("350x600")
root.title("Secret Notes")

# Add image
image_path = "top_secret.png"
image = Image.open(image_path)
image = image.resize((250, 150))
tk_image = ImageTk.PhotoImage(image)

label = tk.Label(root, image=tk_image)
label.pack(padx=10, pady=10)

# Title entry
tk.Label(root, text="Enter your title").pack(padx=10, pady=10)
title_entry = tk.Entry(root, width=30)
title_entry.pack()

# Note text box
tk.Label(root, text="Enter your secret").pack(padx=10, pady=10)
text_box = tk.Text(root, wrap=tk.WORD, width=40, height=10, font=("Arial", 10))
text_box.pack(padx=10, pady=10)

# Master key entry
tk.Label(root, text="Enter master key").pack(padx=10, pady=10)
master_key_entry = tk.Entry(root, width=30, show="*")
master_key_entry.pack()

# Save & Encrypt button
tk.Button(root, text="Save & Encrypt", command=save_note).pack(padx=7, pady=7)

# Decrypt button
tk.Button(root, text="Decrypt", command=decrypt_note).pack(padx=7, pady=7)

root.mainloop()
