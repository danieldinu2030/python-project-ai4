# Python Project for Applied Informatics 4

## Platformer Game

> Add introduction here

## Features

> Describe what happens

- **main menu** (animated play and quit buttons)
- **level timer**
- **loss menu**
- **background decorations** (trees, etc)
- coin sound to become self.object sound
- spikes
- chest with hearts
- enemies
- level ending

Insane things:
- game story (accessible from main menu)
- item store (power-ups)
- bonus level (as wild as possible)

## Playing the Game

Running the game requires the module `pygame`, which is not a standard one.
It is recommended to create a **virtual environment** and install `pygame` there.
Ensure you have `virtualenv` installed:

```c
sudo apt install virtualenv
```

Then, create the virtual environment, activate it and install the module:

```c
virtualenv .venv
source ./.venv/bin/activate
pip install pygame
```

If you are using an IDE like VSCode, you may need to change the Python interpreter to the one located inside the virtual environment: 
`./.venv/bin/python`