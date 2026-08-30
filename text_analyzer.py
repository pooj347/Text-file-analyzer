import os
import collections
import string

from gtts import gTTS


def current_dir_and_files():
    """Display the current working directory and files."""
    cwd = os.getcwd()
    print("\n" + "-" * 55)
    print("Current Working Directory and Files")
    print("-" * 55)
    print(cwd)

    files = os.listdir(cwd)
    for index, filename in enumerate(files):
        print(f"{index} | {filename}")

    return cwd, files


def file_details(file_path):
    """Analyze and display details of a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()

        lines = data.count(os.linesep)
        characters = len(data.replace(" ", "")) - lines
        words = data.split()
        word_counter = collections.Counter(words)

        special_chars = sum(
            count
            for char, count in collections.Counter(data).items()
            if char in string.punctuation
        )

        lowercase = sum(char.islower() for char in data)
        uppercase = sum(char.isupper() for char in data)

        print("\n" + "-" * 55)
        print("File Details")
        print("-" * 55)
        print(f"File: {file_path}")
        print(f"Number of Lines: {lines}")
        print(f"Number of Characters: {characters}")
        print(f"Number of Words: {len(words)}")
        print(f"Number of Unique Words: {len(word_counter)}")
        print(f"Number of Special Characters: {special_chars}")
        print(f"Number of Lowercase Letters: {lowercase}")
        print(f"Number of Uppercase Letters: {uppercase}")

    except FileNotFoundError:
        print(f'File "{file_path}" cannot be found.')
    except OSError:
        print(f'File "{file_path}" cannot be opened.')


def find_string(file_path):
    """Search for a word or phrase in a text file."""
    search_text = input("Enter the word or phrase to search: ")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()

        if search_text in data:
            print("Your string is FOUND in the file.")
        else:
            print("Your string is NOT FOUND in the file.")

    except FileNotFoundError:
        print(f'File "{file_path}" cannot be found.')
    except OSError:
        print(f'File "{file_path}" cannot be opened.')


def text_to_voice(file_path):
    """Convert the selected text file into an MP3 using gTTS."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        speech = gTTS(text=text, lang="en", slow=False)
        output_file = "text_2_voice.mp3"
        speech.save(output_file)

        print(f"Audio saved as: {output_file}")
        print("Internet connection is required for gTTS.")

    except FileNotFoundError:
        print(f'File "{file_path}" cannot be found.')
    except OSError:
        print(f'File "{file_path}" cannot be opened.')


def choose_text_file(files):
    """Let the user choose a text file from the current directory."""
    text_files = [
        filename for filename in files
        if filename.lower().endswith(".txt")
    ]

    if not text_files:
        print("No .txt files found in the current directory.")
        return None

    print("\nAvailable text files:")
    for index, filename in enumerate(text_files):
        print(f"{index} | {filename}")

    try:
        choice = int(input("Enter file number: "))
        return text_files[choice]
    except (ValueError, IndexError):
        print("Invalid file selection.")
        return None


def project_menu():
    """Run the main menu."""
    while True:
        print("\n" + "-" * 55)
        print("TEXT FILE ANALYZER")
        print("-" * 55)
        print("1. Current Working Directory & Files")
        print("2. File Details")
        print("3. Find a String from the File")
        print("4. Text to Voice - Internet Required")
        print("5. Exit")
        print("-" * 55)

        choice = input("Select your option [1-5]: ")

        if choice == "1":
            current_dir_and_files()

        elif choice in {"2", "3", "4"}:
            cwd, files = current_dir_and_files()
            file_name = choose_text_file(files)

            if file_name is None:
                continue

            file_path = os.path.join(cwd, file_name)

            if choice == "2":
                file_details(file_path)
            elif choice == "3":
                find_string(file_path)
            else:
                text_to_voice(file_path)

        elif choice == "5":
            print("Thank you for using Text File Analyzer!")
            break

        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    project_menu()
