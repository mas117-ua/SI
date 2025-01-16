# 🎮 A* Pathfinding Project with Pygame


This project implements an A* pathfinding algorithm visualization using Pygame. The application allows users to find optimal paths between two points on a grid-based map with different terrain types, considering both distance and terrain costs. 🗺️

## ✨ Features

- **Interactive GUI**: Click-based interface for selecting start and end points 🖱️
- **Multiple Terrain Types** 🏞️:
  - 🌱 Grass (Light brown)
  - 💧 Water (Light blue)
  - 🗿 Rock (Brown)
  - 🧱 Walls (Dark blue)
- **Two Pathfinding Algorithms** 🧮:
  - Classic A* algorithm
  - ε-admissible A* variant for better caloric optimization
- **Multiple Heuristics** 📐:
  - Manhattan distance
  - Euclidean distance
  - Octile distance
- **Real-time Visualization**: Path finding process shown with yellow highlighting ⚡
- **Cost Metrics** 📊: 
  - Path length cost
  - Caloric expenditure based on terrain

<img src="/api/placeholder/600/300" alt="Algorithm in Action" />

## 📁 Files Structure

- `main.py`: Main application file containing GUI implementation and algorithm calls
- `mapa.py`: Map class implementation for terrain handling and movement validation
- `estado.py`: State class for A* algorithm node representation
- `casilla.py`: Cell class for grid position management

## 💪 Terrain Costs

- 🌱 **Grass**: 2 calories
- 💧 **Water**: 4 calories
- 🗿 **Rock**: 6 calories
- 🧱 **Walls**: Impassable


## ⚖️ Movement Costs

- **Orthogonal Movement** (Up, Down, Left, Right): 1 unit
- **Diagonal Movement**: 1.5 units

## 🎮 How to Use

1. **Launch the Application** 🚀:
   ```
   python main.py [map_file]
   ```
   If no map file is specified, it defaults to 'mapa.txt'

2. **Select Points** 🎯:
   - Left-click to set starting point (🐰 rabbit icon)
   - Right-click to set destination point (🥕 carrot icon)

3. **Choose Algorithm** 🤖:
   - Left button: Classic A* algorithm
   - Right button: ε-admissible A* variant

4. **View Results** 📊:
   - Yellow path shows the optimal route
   - Bottom left: Total caloric cost
   - Bottom right: Path cost

<img src="/api/placeholder/600/300" alt="GUI Interface Demo" />

## 📝 Map Format

Maps are text files with the following symbols:
- `.`: Grass (traversable) 🌱
- `#`: Wall (impassable) 🧱
- `~`: Water (high cost) 💧
- `*`: Rock (very high cost) 🗿

## 🔧 Implementation Details

### A* Algorithm Features
- Priority queue-based implementation 📊
- Multiple heuristic functions (Manhattan, Euclidean, Octile) 📐
- Comprehensive node exploration tracking 🔍
- Path reconstruction with both cost and caloric expenditure calculation ⚡


### ε-admissible Variant
- Uses a focal list for nodes within (1+ε) * f_min
- Optimizes for caloric expenditure within bounded optimality
- Maintains admissibility while improving solution quality

## 🛠️ Requirements

- Python 3.x 🐍
- Pygame library 🎮
- Required assets:
  - boton1.png 🔘
  - boton2.png 🔘
  - rabbit.png 🐰
  - carrot.png 🥕

## ⚠️ Error Handling

The program includes comprehensive error checking for:
- ❌ Invalid map files
- ❌ Invalid cell selections
- ❌ Unreachable destinations
- ❌ Missing start/end points

## 📊 Performance

- Tracks and displays number of explored nodes
- Shows node exploration order
- Real-time path cost and caloric expenditure updates


## 📝 Technical Notes

- Uses object-oriented design with separate classes for map, state, and cell management 🏗️
- Implements multiple heuristic functions for different distance calculations 📐
- Supports custom map loading through command-line arguments 📂
- Provides visual feedback for all user interactions 🖥️



- Your Name 👨‍💻
- Contributors 👥

### 🙏 Acknowledgments

- Thanks to everyone who has contributed to this project! 🌟
- Special thanks to the Pygame community 🎮
