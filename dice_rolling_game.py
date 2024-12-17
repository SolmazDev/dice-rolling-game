import random
import pygame
import sys
import time

pygame.init()

# Window settings
win_width = 400
win_height = 400
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Dice Rolling Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (74, 74, 74)
green = (0, 100, 0)
green2 = (143, 188, 143)
light_gray = (170, 170, 170)

# Fonts
name_font = pygame.font.Font("C:/Windows/Fonts/FREESCPT.TTF", 30)
button_font = pygame.font.Font(None, 36)

# Player names
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

# Dice images
dice_images = {
    1: pygame.image.load("dice_imgs/dice1.png"),
    2: pygame.image.load("dice_imgs/dice2.png"),
    3: pygame.image.load("dice_imgs/dice3.png"),
    4: pygame.image.load("dice_imgs/dice4.png"),
    5: pygame.image.load("dice_imgs/dice5.png"),
    6: pygame.image.load("dice_imgs/dice6.png"),
}

# Resize dice images
dice_size = (80, 80)
for key in dice_images:
    dice_images[key] = pygame.transform.scale(dice_images[key], dice_size)

# Button start
button_start = pygame.Rect((win_width // 2) - 50, 300, 100, 30)

def draw_dice(number1, number2):
    screen.fill(green)

    # Draw player name boxes
    name_box1 = pygame.Rect(50, 80, 100, 25)
    name_box2 = pygame.Rect(250, 80, 100, 25)
    pygame.draw.rect(screen, green2, name_box1)
    pygame.draw.rect(screen, green2, name_box2)

    # Draw start button with hover effect
    if button_start.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, gray, button_start)  # Darker color on hover
    else:
        pygame.draw.rect(screen, light_gray, button_start)

    button_text = button_font.render("Start", True, black)
    screen.blit(button_text, (button_start.x + 20, button_start.y + 5))

    # Render player names
    name1_text = name_font.render(player1_name, True, gray)
    screen.blit(name1_text, (name_box1.x+5 , name_box1.y-5 ))

    name2_text = name_font.render(player2_name, True, gray)
    screen.blit(name2_text, (name_box2.x+5 , name_box2.y-5 ))

    # Render dice images
    screen.blit(dice_images[number1], (100, 150))
    screen.blit(dice_images[number2], (220, 150))

    pygame.display.flip()

def roll_animation():
    for _ in range(10):
        temp1 = random.randint(1, 6)
        temp2 = random.randint(1, 6)
        draw_dice(temp1, temp2)
        time.sleep(0.1)

# Main loop
running = True
rolling = False
output1, output2 = 1, 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for KEYDOWN event (pressing 'Y' or 'N')
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:  # 'Y' key to roll dice
                roll_animation()
                output1 = random.randint(1, 6)
                output2 = random.randint(1, 6)
                draw_dice(output1, output2)
            elif event.key == pygame.K_n:  # 'N' key to exit
                print("Thank you for playing!")
                running = False
            else:
                print("Invalid key! Please press 'y' to roll or 'n' to exit.")

        # Check for MOUSEBUTTONDOWN event (clicking the Start button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_start.collidepoint(event.pos):
                roll_animation()
                output1 = random.randint(1, 6)
                output2 = random.randint(1, 6)
                draw_dice(output1, output2)

    # Draw the initial state or updated state
    if not rolling:
        draw_dice(output1, output2)
        rolling = True

pygame.quit()
sys.exit()
