# 🐍 Snake AI with Pygame

A classic Snake game built using **Python** and **Pygame**, featuring an **AI bot** that can play automatically using **Greedy** and **A*** search algorithms.  

---

## 🚀 Features
- Play manually with arrow keys 🕹️  
- Toggle **Autoplay AI** mode (Greedy or A*) 🤖  
- Dynamic **food spawning** that avoids the snake and walls 🍎  
- Adjustable **speed control** ⚡  
- Path visualization when AI is enabled 🟩  
- Simple **score system** and **Game Over** screen 💀  

---

## 🎮 Controls
| Key | Action |
|-----|--------|
| `Arrow Keys` | Move snake (manual mode) |
| `A` | Pause/Unpause |
| `I` | Toggle Autoplay AI |
| `O` | Increase speed |
| `P` | Decrease speed |
| `R` | Restart game |
| `Q` | Quit game |

---

## 🧠 AI Algorithms
- **Greedy Search** → always moves closer to the food (short-sighted, can trap itself).  
- **A*** Search → smarter pathfinding that balances distance and cost.  
- Fallback: **tail-following** and **safe random moves** to avoid crashing.

---

## 🗂️ Project Structure
```
├── main.py       # Entry point – runs the game loop
├── snake.py      # Snake logic (movement, growth, collisions)
├── food.py       # Food spawning & drawing
├── grid.py       # Grid rendering, coordinate handling, path drawing
├── algo.py       # Snake AI algorithms (Greedy, A*)
```

---

## ⚡ Installation & Run
1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd snake
   ```
2. Install dependencies:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python main.py
   ```

---

## 🖼️ Screenshots
*(Add screenshots or GIFs of gameplay here!)*

---

## 📝 To-Do / Improvements
- Smarter AI (Hamiltonian cycle, survival strategies).  
- Add multiple difficulty levels.  
- High-score saving system.  
- Sound effects & animations.  