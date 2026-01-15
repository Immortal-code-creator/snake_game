# Snake Game (Python)

A classic **Snake Game** built using **Python** and **Pygame**, featuring a custom home screen, background music, and highscore tracking.  

Grow your snake by eating apples, avoid collisions, and try to beat your highscore!

---

## Description

The Snake Game is a Python-based **console and GUI hybrid application** using Pygame. Players control a snake to collect apples, growing in size with each apple eaten. The game tracks **score** and **highscore** and includes:

- Custom **home screen** and **game-over screen**
- Background music and sound effects
- Real-time score and highscore display
- Collision detection with walls and self
- Smooth gameplay with increasing snake length

This project demonstrates **Python fundamentals** such as loops, conditionals, functions, file handling, and basic game logic.

---

## Dependencies

- Python 3.10 or above  
- Supported Operating Systems:
  - Windows
  - Linux
  - macOS  

## Python Modules Used:

- `pygame`
- `random`
- `os`
- `sys`  

> No external libraries beyond Pygame are required.

---

## Concepts Used

- Loops (`while`)  
- Conditional Statements (`if`, `elif`, `else`)  
- Functions  
- File Handling (`Highscore.txt`)  
- User Input Handling  
- Random Module (`random.randint`)  
- Pygame Graphics and Sound  
- Game Logic and Collision Detection  

---

## How the Program Works

1. Run the game.  
2. The **home screen** appears with background music.  
3. Press **Enter** to start the game.  
4. Control the snake using the **arrow keys**:
   - ⬆ Up  
   - ⬇ Down  
   - ⬅ Left  
   - ➡ Right  
5. Eat apples to grow your snake and increase your score.  
6. Avoid colliding with the **walls** or your **own tail**.  
7. When the game ends:
   - Your score and highscore are displayed  
   - Press **Enter** to restart  

The **highscore** is stored in `Highscore.txt` and persists across game sessions.


## Installation

 ### Clone the repository:

### git clone https://github.com/Immortal-code-creator/snake-game.git

## Navigate the Project directory:

 cd snake-game

### Install Pygame:

  ### -pip install pygame


Make sure Python 3.10+ is installed.

### Running the Game

Run the game from the terminal or command prompt:

 ### python snake_game.py


Alternatively, you can create an executable .exe using PyInstaller:

pyinstaller --onefile --windowed --icon snake_icon.ico \
--add-data "apple.png;." \
--add-data "snakehome.png;." \
--add-data "snakebackground.jpg;." \
--add-data "Snakeend.png;." \
--add-data "02. Clair-Obscur.mp3;." \
--add-data "gameover.wav;." \
--add-data "Highscore.txt;." \
snake_game.py


The .exe will be generated in the dist/ folder.

### Assets

snakehome.png – Home screen

snakebackground.jpg – Main game background

Snakeend.png – Game-over screen

apple.png – Food for the snake

02. Clair-Obscur.mp3 – Background music

gameover.wav – Game-over sound effect

Highscore.txt – Stores

### Author
Aeshan Chowdhury
### GitHub:-https://github.com/Immortal-code-creator
