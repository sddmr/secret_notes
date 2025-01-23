

# Secret Notes Application

This is a simple Python application built using **Tkinter** for the graphical user interface (GUI), and **cryptography** for secure encryption and decryption of notes. The application allows users to enter a title, secret message, and a master key, which are then encrypted and saved into a file. Users can later decrypt the message by providing the correct master key.

## Features

- **Encryption**: The application uses AES encryption with CBC mode to secure the content of the note.
- **Decryption**: Users can decrypt the saved notes by entering the correct master key.
- **Graphical Interface**: The app is built using Tkinter and includes an image for visual appeal.
- **Persistent Storage**: Notes are saved in a text file (`secret.txt`) in the current directory.

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Install the required dependencies using the following command:

   ```bash
   pip install pillow cryptography
   ```

3. Download the project files or clone the repository:

   ```bash
   git clone <your-repository-link>
   ```

4. Run the application:

   ```bash
   python secret_notes.py
   ```

## How to Use

1. **Enter your title**: Type the title of your note.
2. **Enter your secret**: Write the content of your secret note.
3. **Enter master key**: Provide a master key that will be used to encrypt and later decrypt the note.
4. **Save & Encrypt**: Click the "Save & Encrypt" button to save the note with encryption.
5. **Decrypt**: Enter the correct master key and click "Decrypt" to reveal the original content of the note.

## Note

- The file where the encrypted notes are stored is named `secret.txt`. 
- Each note is appended to the file, so multiple notes can be stored.
- The notes are saved in an encrypted format to ensure privacy.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
