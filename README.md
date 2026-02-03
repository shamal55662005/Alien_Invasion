# Alien Invasion

A simple Pygame-based space shooter where you control a ship, fire bullets, and face an alien fleet.

## Requirements
- Python 3.8+ (recommended)
- pip

## Install (Windows, macOS, Linux)
1. **Clone the repo**:
   ```bash
   git clone <your-repo-url>
   cd Alien_Invasion
   ```
2. **Create and activate a virtual environment** (recommended):
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install pygame
   ```

## Run the game
```bash
python Alien_invasion.py
```

## Controls
- **Left / Right Arrow**: Move ship
- **Space**: Fire
- **Esc**: Quit

## Troubleshooting
- If `python` does not resolve correctly, use `python3`.
- On Windows, you may need to allow the script to run in PowerShell:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
