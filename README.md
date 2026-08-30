# Text File Analyzer

A Python-based menu-driven application for analyzing `.txt` files, searching for text, and converting text into speech.

## Features

- Display the current working directory and available files
- Analyze a text file
- Count lines, characters, words, and unique words
- Count special characters
- Count lowercase and uppercase letters
- Search for a word or phrase in a text file
- Convert text-file content to speech using Google Text-to-Speech (gTTS)
- Simple interactive menu

## Tech Stack

- Python
- `os`
- `collections`
- `string`
- `gTTS`

## Project Structure

```text
text-file-analyzer/
├── text_analyzer.py
├── sample.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Install Python 3.7 or above.
2. Clone this repository.
3. Install the required package:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python text_analyzer.py
```

Place a `.txt` file in the project directory and select the required option from the menu.

## Menu

1. Current Working Directory & Files
2. File Details
3. Find a String from the File
4. Text to Voice
5. Exit

> The Text to Voice feature requires an internet connection because it uses gTTS.

## Learning Outcomes

This project demonstrates practical use of Python file handling, strings, collections, operating-system utilities, text analysis, and text-to-speech functionality.

## Author

**S.T. Poojaa**

GitHub: [@pooj347](https://github.com/pooj347)
