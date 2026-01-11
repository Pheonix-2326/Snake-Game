# 🐍 Snake Game (Python)

A classic **Snake Game** built using **Python and Pygame**, featuring smooth movement, sound effects, score tracking, and high-quality graphics. The game runs in a resizable full-screen window while maintaining a fixed gameplay area centered on the screen.

This project demonstrates:
- Object-Oriented Programming (OOP)
- Event-driven game loop
- Collision detection
- Asset handling (images, sounds, fonts)
- Core game development concepts in Python

---

## 🎮 Game Features

- 🟢 Smooth snake movement  
- 🍎 Randomly spawning fruit  
- 🔊 Sound effect on eating fruit  
- 📈 Live score display  
- 🧱 Wall collision detection  
- 🔁 Automatic game reset on failure  
- 🖥️ Resizable full-screen window  
- 🎨 Custom snake graphics (head, body, tail, curves)

---

## 🕹️ Controls

| Key | Action |
|----|-------|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |

---

## 🛠️ Technologies Used

- **Programming Language:** Python 3  
- **Game Library:** Pygame  

### Python Modules Used
- `pygame`
- `random`
- `sys`
- `ctypes`
- `platform`

---

## 📂 Project Structure

```
Snake-Game/
│
├── Main.py
├── images/
│ ├── apple.png
│ ├── icon.png
│ ├── snake_head_.png
│ ├── snake_body_.png
│ ├── snake_tail_.png
│ └── snake_curve_.png
│
├── sound/
│ └── crunch.wav
│
├── font/
│ └── PoetsenOne-Regular.ttf
│
└── README.md
```

---

## ▶️ How to Run the Game

### 1️⃣ Install Python
Make sure **Python 3.x** is installed on your system.

### 2️⃣ Install Pygame
```bash
pip install pygame
```

### 3️⃣ Run the Game
```bash
python Main.py
```

---

## 🧠 Game Logic Overview

- The snake grows when it eats fruit.
- Fruit spawns at random positions on the grid.
- The game resets when:
  - The snake hits the boundary
  - The snake collides with itself
- Score is calculated based on snake length.

---

## 📚 Learning Outcomes

- Understanding game loops and frame updates
- Grid-based movement using vectors
- Working with images, sounds, and fonts
- Applying OOP principles in Python
- Basic game state management

---

## 👤 Author

**Dhruv Patel**  
Pheonix-2326  
Personal Project

---

## 📜 License

This project is created for **educational purposes**.  
You are free to use and modify it for learning.
