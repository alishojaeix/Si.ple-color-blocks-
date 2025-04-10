# 🎨 Color Blocks Matching Game

![Gameplay Demo](assets/gameplay.gif) *(add a GIF later)*  
*A vibrant color-matching puzzle game built with Python and Pygame*

## 🚀 Features

- 🧩 Classic match-3 puzzle gameplay
- 🎯 Score tracking system
- 🌈 6 vibrant colors
- 🖱️ Simple mouse controls
- 🔄 Dynamic block refilling
- 📊 Increasing difficulty

## 📋 Table of Contents
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [Controls](#-controls)
- [Customization](#-customization)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alishojaeix/color-blocks-game.git
   cd color-blocks-game

   2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. Click on a block to select it
2. Click an adjacent block to swap positions
3. Match 3+ blocks of the same color to make them disappear
4. Earn 10 points per block in a match
5. New blocks fall from the top to fill empty spaces
6. Play as long as you want - challenge yourself to beat your high score!

## 🕹️ Controls

| Control | Action |
|---------|--------|
| Left Click | Select/Swap blocks |
| Window Close | Quit game |

## 🛠️ Customization

Easily modify game parameters in `colorblocks/game.py`:

```python
# Change these values:
GRID_SIZE = 8        # Board size (8x8)
BLOCK_SIZE = 60      # Pixel size of blocks
COLORS = [           # RGB color values
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    # Add more colors!
]
```

## 📸 Screenshots

*(Add actual screenshots after creating them)*  
| Game Start | Match Made | Score Update |
|------------|-----------|-------------|
| ![Start](assets/screen1.png) | ![Match](assets/screen2.png) | ![Score](assets/screen3.png) |

## 🗺️ Roadmap

Planned future improvements:

- [ ] Add block sprites from free asset sites
- [ ] Implement high score saving
- [ ] Add sound effects and music
- [ ] Create special power-up blocks
- [ ] Develop level progression system

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

