# snake-game-python
Implenting he Snake Game, a classic arcade game where the player controls a "snake" that moves around a rectangular grid. The objective is to collect food, which increases the length of the snake and the player's score. However, the game ends if the snake collides with the boundaries of the grid or its own body.

# How the game works
1. Game Start:
- The game starts with a short snake positioned in the center of the screen.
- A piece of food is randomly placed on the screen.
2. Player Control:
- The player uses the arrow keys (UP, DOWN, LEFT, RIGHT) to move the snake.
- The snake moves continuously in the direction of the last arrow key pressed.
3. Objective:

- The snake "eats" the food by colliding with it, which increases its length and the player's score.
- After eating food, a new piece of food is randomly placed.
4. Game Over:

    The game ends if the snake:
- Hits the screen boundaries.
- Collides with its own body.
- The player is then given the option to restart the game or quit.

# How the code works
1. Setup and initialization
- `pygame.init()` initializes the Pygame library.
- Colors are defined as RGB tuples for use in rendering the game screen.
- The game window dimensions (`dis_width`, `dis_height`) are set, and the display is initialized.
- `clock` is used to control the frame rate (speed of the game).
`- snake_block` defines the size of each snake segment, and snake_speed controls how fast the snake moves.
2. Helper Functions
`message`: Displays messages (e.g., game over messages) on the screen.
Uses the `font_style` to render text.
3. Main Game Loop (`gameLoop`)
Initialization:

The snake starts in the center of the screen (x1, y1).
The food is randomly positioned.
`snake_List` tracks the snake's body, and Length_of_snake starts at 1.
The score is initialized to 0.
Game Logic:

Handling Events:

The game listens for player inputs (QUIT, KEYDOWN) to control the snake's movement or exit the game.
Arrow keys (K_LEFT, K_RIGHT, K_UP, K_DOWN) change the direction of the snake.
Boundary Collision:

If the snake moves outside the game window, game_close is set to True, and the game ends.
Snake Movement:

The snake's head coordinates are updated based on the direction of movement.
The head is appended to snake_List, which represents the body.
The oldest segment of the snake is removed if the snake hasn't eaten food (to keep its length constant).
Self-Collision:

The game checks if the snake's head collides with any part of its body (snake_List[:-1]).
Food Collision:

If the snake's head collides with the food, the snake grows (Length_of_snake increases), and the score increments by 1.
A new piece of food is placed randomly on the screen.
Rendering:

The screen is cleared and redrawn in every frame:
The background is filled with blue.
The food is drawn as a green block.
Each segment of the snake is drawn as a black block.
The score is displayed at the top-left corner.
Game Over Screen:

When the game ends, the screen shows a message with options to quit (Q) or restart (C).
4. Game Termination
When the player quits, pygame.quit() is called to clean up and close the game window.
