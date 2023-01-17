import pygame
# imports the Pygame library, which is a set of modules for game development in Python.
import math
#  imports the math module, which provides mathematical functions and constants.
# First, the code initializes Pygame and sets the display size, caption, and FPS. It uses the pygame.init() function to initialize the Pygame library, and the pygame.display.set_mode() function to set the display size to 800x600 pixels. It also uses the pygame.display.set_caption() function to set the caption of the game window to "Brick Breaker".

pygame.init()
# initializes the Pygame library.
# Display the size
WIDTH, HEIGHT = 800, 600
# sets the width and height of the game window to 800x600 pixels.
win = pygame.display.set_mode((WIDTH, HEIGHT))
# creates the game window with the specified width and height.
pygame.display.set_caption("Brick Breaker")
# sets the caption of the game window to "Brick Breaker".

# Configure the paddle and the ball
FPS = 60
# sets the frames per second (FPS) of the game to 60.
PADDLE_WIDTH = 100
#  sets the width of the paddle to 100 pixels.
PADDLE_HEIGHT = 15
# sets the height of the paddle to 15 pixels.
BALL_RADIUS = 10
# sets the radius of the ball to 10 pixels.

LIVES_FONT = pygame.font.SysFont("comicsans", 40)
# pygame.font.SysFont("comicsans", 40) sets the font of the lives text to "comicsans" and the font size to 40.

# Then, the code defines three classes: Paddle, Ball, and Brick. Each class has its own properties, methods, and behavior.
# The Paddle class has a VEL class variable, which is set to 5, and an init method that is used to initialize the object. This method takes in the x and y position, width, height, and color of the paddle as arguments. It also has a draw method, which is used to draw the paddle on the screen, and a move method which is used to move the paddle in the specified direction.


class Paddle:
    # The Paddle class has a VEL class variable
    # which is set to 5, and an init method that is used to initialize the object.
    # This method takes in the x and y position, width, height, and color of the paddle as arguments.
    # It also has a draw method, which is used to draw the paddle on the screen.
    # A move method which is used to move the paddle in the specified direction.
    VEL = 5

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction=1):
        self.x = self.x + self.VEL * direction

# The Ball class has a VEL class variable, which is set to 5, and an init method that is used to initialize the object.
# This method takes in the x and y position, radius, and color of the ball as arguments. It also has a move method that updates the ball's position based on its current velocity, a set_vel method that sets the velocity of the ball, and a draw method that is used to draw the ball on the screen.


class Ball:
    # The Ball class has a VEL class variable
    # which is set to 5, and an init method that is used to initialize the object.
    # This method takes in the x and y position, radius, and color of the ball as arguments.
    # It also has a move method that updates the ball's position based on its current velocity
    # a set_vel method that sets the velocity of the ball, and a draw method that is used to draw the ball on the screen.
    VEL = 5

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_vel = 0
        self.y_vel = -self.VEL

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# The Brick class has an init method that takes in the x and y position, width, height, health, and colors of the brick as arguments. It has a draw method that is used to draw the brick on the screen, a collide method that detects when the ball collides with the brick, and a hit method that decrements the brick's health and changes its color based on its remaining health.
# It also has a static method interpolate that takes in the color_a, color_b and the t as argument and it is used to interpolate the color of the brick based on the health.


class Brick:
    # The Brick class has an init method that takes in the x and y position, width, height, health, and colors of the brick as arguments.
    # It has a draw method that is used to draw the brick on the screen.
    # A collide method that detects when the ball collides with the brick.
    # A hit method that decrements the brick's health and changes its color based on its remaining health.
    # It also has a static method interpolate that takes in the color_a, color_b and the t as argument.
    # It is used to interpolate the color of the brick based on the health.
    def __init__(self, x, y, width, height, health, colors):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.colors = colors
        self.color = colors[0]

    def draw(self, win):
        # The draw method is used to draw the brick on the screen using the pygame.draw.rect function.
        # It takes in a window and the brick's coordinates, width, height and color as arguments.
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))

    def collide(self, ball):
        # The collide method takes in a ball as an argument, it checks if the ball collides with the brick.
        # If it does it calls the hit method and updates the ball's velocity.
        if not (ball.x <= self.x + self.width and ball.x >= self.x):
            return False
        if not (ball.y - ball.radius <= self.y + self.height):
            return False

        self.hit()
        ball.set_vel(ball.x_vel, ball.y_vel * -1)
        return True

    def hit(self):
        self.health -= 1
        self.color = self.interpolate(
            *self.colors, self.health/self.max_health)

    @staticmethod
    def interpolate(color_a, color_b, t):
        # The interpolate static method takes in color_a, color_b and t as arguments.
        # and it is used to interpolate the color of the brick based on the health.
        # It calculates a new color by linearly interpolating the RGB values of color_a and color_b based on the value of t.
        # which should be a value between 0.0 and 1.0.
        # 'color_a' and 'color_b' are RGB tuples
        # 't' is a value between 0.0 and 1.0
        # this is a naive interpolation
        return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))


def draw(win, paddle, ball, bricks, lives):
    # he game window is first filled with the color white using the fill() method of the win object.
    # Then, the paddle object is drawn on the window using the draw() method of the paddle object.
    # Similarly, the ball object is drawn on the window using the draw() method of the ball object.

    # This is the code for the draw() function which is responsible for drawing the various elements of the game on the screen.
    # This function takes in several arguments: win,
    # which is the game window, paddle, which is the paddle object, ball, which is the ball object, bricks,
    # which is a list of brick objects, and lives,
    # which is an integer representing the number of lives the player has left.

    win.fill("white")
    paddle.draw(win)
    ball.draw(win)

    for brick in bricks:
        brick.draw(win)
        # The function then uses a for loop to iterate through the list of brick objects
        # draw each brick on the window using the draw() method of the brick object.

    lives_text = LIVES_FONT.render(f"Lives: {lives}", 1, "black")
    win.blit(lives_text, (10, HEIGHT - lives_text.get_height() - 10))
    #  the number of lives the player has left is rendered as text and drawn on the window at
    #  the top right corner using the render() method of the LIVES_FONT object,
    #  the update() method of the pygame.display module is called to update the game window with the new elements.

    pygame.display.update()


def ball_collision(ball):
    # The function ball_collision(ball) checks if the ball has collided with the left or right edge of the screen.
    # If so, it reverses the x velocity of the ball.
    # It also checks if the ball has collided with the top or bottom edge of the screen.
    # If so, it reverses the y velocity of the ball.
    # This causes the ball to "bounce" off the edges of the screen.
    if ball.x - BALL_RADIUS <= 0 or ball.x + BALL_RADIUS >= WIDTH:
        ball.set_vel(ball.x_vel * -1, ball.y_vel)
    if ball.y + BALL_RADIUS >= HEIGHT or ball.y - BALL_RADIUS <= 0:
        ball.set_vel(ball.x_vel, ball.y_vel * -1)


def ball_paddle_collision(ball, paddle):
    # The function ball_paddle_collision(ball, paddle) is used to check if the ball object collides with the paddle object.
    # If the collision is detected, the function calculates the angle of the ball's reflection off the paddle using
    # the distance of the ball's x position to the center of the paddle.
    # Then it uses trigonometry (sine and cosine) to calculate the new x and y velocities of the ball,
    # which are then set using the ball.set_vel(x_vel, y_vel) method.
    # This way the ball will be reflected off the paddle
    # at an angle that depends on where the ball hit the paddle.
    if not (ball.x <= paddle.x + paddle.width and ball.x >= paddle.x):
        return
    if not (ball.y + ball.radius >= paddle.y):
        return

    paddle_center = paddle.x + paddle.width/2
    distance_to_center = ball.x - paddle_center

    percent_width = distance_to_center / paddle.width
    angle = percent_width * 90
    angle_radians = math.radians(angle)

    x_vel = math.sin(angle_radians) * ball.VEL
    y_vel = math.cos(angle_radians) * ball.VEL * -1

    ball.set_vel(x_vel, y_vel)


def generate_bricks(rows, cols):
    # This function generates a grid of bricks with the specified number of rows and columns.
    # It calculates the width and height of each brick based on the total width and height of the window,
    # and the number of columns.
    # It creates a 2 pixel gap between each brick. Each brick is created using the Brick class
    # and passed the calculated x and y position, width and height, starting health of 2,
    # and a tuple of colors representing the brick's color when it has full health and when it has no health left.
    # The bricks are appended to a list and the list is returned.
    gap = 2
    brick_width = WIDTH // cols - gap
    brick_height = 20

    bricks = []
    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * brick_width + gap * col, row * brick_height +
                          gap * row, brick_width, brick_height, 2, [(0, 255, 0), (255, 0, 0)])
            bricks.append(brick)

    return bricks


def main():
    # the main elements of the game, including the paddle, ball, and bricks.
    # It also sets the initial number of lives the player has to 3.
    # The paddle and ball are positioned in the middle of the screen,
    # and the bricks are generated using the generate_bricks() function, creating 3 rows and 10 columns of bricks.
    # The clock is also initialized to keep track of the frame rate.

    clock = pygame.time.Clock()

    paddle_x = WIDTH/2 - PADDLE_WIDTH/2
    paddle_y = HEIGHT - PADDLE_HEIGHT - 5
    paddle = Paddle(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT, "black")
    ball = Ball(WIDTH/2, paddle_y - BALL_RADIUS, BALL_RADIUS, "black")

    bricks = generate_bricks(3, 10)
    lives = 3

    def reset():
        # This function resets the position of the paddle and ball to their initial positions when called.
        # The paddle's x and y position is set to the initial x and y position,
        # and the ball's x and y position is set to the center of the screen and just above the paddle.
        paddle.x = paddle_x
        paddle.y = paddle_y
        ball.x = WIDTH/2
        ball.y = paddle_y - BALL_RADIUS

    def display_text(text):
        # This function is used to display a message on the screen for a certain amount of time.
        # The text of the message is passed as a parameter,
        # and the message is rendered in red color using the LIVES_FONT font.
        # The message is then blitted to the center of the screen, and the display is updated.
        # The function then waits for 3 seconds (3000 milliseconds) before continuing.
        text_render = LIVES_FONT.render(text, 1, "red")
        win.blit(text_render, (WIDTH/2 - text_render.get_width() /
                               2, HEIGHT/2 - text_render.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)

    run = True
    while run:
        # a while loop that runs as long as the variable "run" is set to true.
        # Within the loop, it checks for any pygame events (such as the user quitting the game),
        # updates the position of the paddle based on user input, and
        # updates the position of the ball while also checking for collisions.
        # The code also has some other helper function such as reset, display_text,
        # and generate_bricks but it's not used in this loop.
        # If put the code in the main function, it will run the game continuously until the user quits.
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and paddle.x - paddle.VEL >= 0:
            paddle.move(-1)
        if keys[pygame.K_RIGHT] and paddle.x + paddle.width + paddle.VEL <= WIDTH:
            paddle.move(1)

        ball.move()
        ball_collision(ball)
        ball_paddle_collision(ball, paddle)

        # The above code is the main game loop of the program.
        # It runs while the run variable is set to true.
        # Within the loop, it checks for the QUIT event,
        # which allows the user to close the game window.
        # Then it checks for keyboard input and moves the paddle accordingly.
        # Then the ball's position is updated with the move() method
        # and its collision with the edges of the screen and the paddle are checked.
        # it iterates through the bricks, checking for collision with the ball
        # and removing any bricks that have a health value of 0.
        # Then it checks if the ball has passed the paddle,
        # reducing the lives by 1 and resetting the ball's position and velocity if necessary.
        # If lives reach 0, it calls the reset() function and displays a "You Lost!" message for 3 seconds.
        # If there are no bricks remaining, it calls the reset() function and displays a "You Won!" message for 3 seconds.
        # Finally, it calls the draw() function to update the game screen.

        for brick in bricks[:]:
            brick.collide(ball)

            if brick.health <= 0:
                bricks.remove(brick)

        # lives check
        if ball.y + ball.radius >= HEIGHT:
            lives -= 1
            ball.x = paddle.x + paddle.width/2
            ball.y = paddle.y - BALL_RADIUS
            ball.set_vel(0, ball.VEL * -1)

        if lives <= 0:
            bricks = generate_bricks(3, 10)
            lives = 3
            reset()
            display_text("You Lost!")

        if len(bricks) == 0:
            bricks = generate_bricks(3, 10)
            lives = 3
            reset()
            display_text("You Won!")

        draw(win, paddle, ball, bricks, lives)

    pygame.quit()
    quit()
    # these two commands are used together to exit the game loop
    # and close the pygame window when the game is over or the user closes the window.
# The code also defines a draw function that takes in the window, paddle, ball, bricks, and lives as arguments. This function is used to update the display with the current state of the game. It uses the fill() function to fill the background with white color, the draw() method of the Paddle and Ball class to draw the paddle and ball on the screen, and a for loop to iterate through the list of bricks and draw each brick on the screen. It also uses the pygame.font.SysFont() function to create a font object for the text that displays the number of lives, the render() method of the font object to render the text, and the blit() function to draw the text on the screen. Finally, it uses the pygame.display.update() function to update the display.


if __name__ == "__main__":
    main()
    # This is the final command to run the main function of the program.
    # It checks if the current script is being run as the main program
    # (as opposed to being imported as a module into another script). If it is, it runs the main() function.
    # This is a common pattern in Python to ensure that code in the script is only executed when the script is run,
    # and not when it's imported as a module.

# The code also defines a ball_collision function that takes in the ball as an argument. This function is used to handle the ball's movement and collision with the walls and bricks. It checks if the ball has collided with the left or right wall, and if so, it changes the x velocity of the ball.
