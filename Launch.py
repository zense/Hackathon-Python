import pygame
import trial
import os

# initializing the constructor
pygame.init()

# screen resolution
res = (620, 400)
pygame.display.set_caption("Random Password Generator ")

screen1 = pygame.display.set_mode(res)
image1 = pygame.image.load(os.path.join('img', "1.jpeg"))
image2 = pygame.image.load(os.path.join('img', "icon.jpg"))
image3 = pygame.image.load(os.path.join('img', 'instructions.JPG'))

width = screen1.get_width()

height = screen1.get_height()

pygame.display.set_icon(image2)
# defining a font
smallfont = pygame.font.SysFont('italic', 35)

text1 = smallfont.render('START ', True, (0, 0, 0))

text2 = smallfont.render('INSTRUCTIONS ', True, (0, 0, 0))

text3 = smallfont.render('QUIT ', True, (0, 0, 0))

text4 = smallfont.render('Home', True, (0, 0, 0))

text5 = smallfont.render('WELCOME', True, (0, 0, 0))


def instructions():

    global screen1, image3, width, height, text4

    while True:

        screen1.blit(image3, (0, 0))  # Image embedding

        pygame.draw.rect(screen1, (196, 164, 132), pygame.Rect(width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40))  # Dark Rectangle on Home
        pygame.draw.rect(screen1, (255, 0, 0), pygame.Rect(width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40), 4)  # Boundary around button

        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:      # If window closed
                pygame.quit()
                exit()

            if event1.type == pygame.MOUSEBUTTONDOWN:

                mouse = pygame.mouse.get_pos()      # mouse position
                if width / 2 + width / 4 - 5 <= mouse[0] <= width / 2 + width / 4 - 5+90 and height / 2 + 140 - 3 <= mouse[1] <= height / 2 + 140 - 3 + 38:     # Home button clicked
                    start()         # Go to start page

            mouse = pygame.mouse.get_pos()
            # If mouse is on home button, make the rectangle light in color
            if width / 2 + width / 4 - 5 <= mouse[0] <= width / 2 + width / 4 - 5 + 90 and height / 2 + 140 - 3 <= mouse[1] <= height / 2 + 140 - 3 + 40:
                pygame.draw.rect(screen1, (255, 164, 132), pygame.Rect(width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40))
                pygame.draw.rect(screen1, (90, 0, 0), pygame.Rect(width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40), 3)

            screen1.blit(text4, (width / 2 + width / 4 + 2, height / 2 + 142))      # Writing Home
            pygame.display.update()


def start():

    while True:

        global screen1
        global res

        screen1.blit(image2, (0, 0))        # Starting image gets embedded

        pygame.draw.rect(screen1, (196, 164, 132), pygame.Rect(width / 2 - width / 4 - 80, height / 2 + 20, 120, 50))   # Start button display
        pygame.draw.rect(screen1, (196, 164, 132), pygame.Rect(width / 2 - 100 - 10, height / 2 + 80, 250, 50))         # Instructions button display
        pygame.draw.rect(screen1, (196, 164, 132), pygame.Rect(width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40))# Quit button display
        pygame.draw.rect(screen1, (255, 0, 0), pygame.Rect(width / 2 - width / 4 - 80, height / 2 + 20, 120, 50), 4)    # Start button Boundary
        pygame.draw.rect(screen1, (255, 0, 0), pygame.Rect(width / 2 - 100 - 10, height / 2 + 80, 250, 50), 4)          # Instructions button Boundary
        pygame.draw.rect(screen1, (255, 0, 0), pygame.Rect(width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40), 4) # Quit button Boundary

        for event1 in pygame.event.get():

            if event1.type == pygame.QUIT:      # If window closed
                pygame.quit()
                exit()

            # checks if a mouse is clicked
            if event1.type == pygame.MOUSEBUTTONDOWN:

                mouse = pygame.mouse.get_pos()
                # Quit button clicked
                if width / 2 + width / 4 - 5 <= mouse[0] <= width / 2 + width / 4 - 5+90 and height / 2 + 140 - 3 <= mouse[1] <= height / 2 + 140 - 3 + 38:
                    pygame.quit()
                    exit()

                # instructions button clicked
                elif width / 2 - 100 - 10 <= mouse[0] <= width / 2 - 100 - 10+250 and height / 2 + 80 <= mouse[1] <= height / 2 + 80 + 50:
                    instructions()

                # Start button clicked
                elif width / 2 - width/4-80 <= mouse[0] <= width / 2 - width/4-80+120 and height / 2+20 <= mouse[1] <= height / 2 + 70:
                    start.begin()

                    screen1 = pygame.display.set_mode(res)
                    pygame.display.set_caption("RANDOM PASSWORD GENERATOR")
                    screen1.blit(image2, (0, 0))
                    pygame.display.set_icon(image2)
                    pygame.display.update()

                else:
                    pygame.display.update()

        mouse = pygame.mouse.get_pos()

        # if mouse  on a button
        # to change to lighter shade

        # If mouse on start button
        if width / 2 - width/4-80 <= mouse[0] <= width / 2 - width/4-80+120 and height / 2+20 <= mouse[1] <= height / 2 + 70:
            pygame.draw.rect(screen1, (255, 164, 132), pygame.Rect(width / 2 - width / 4 - 80, height / 2 + 20, 120, 50))
            pygame.draw.rect(screen1, (255, 0, 0), pygame.Rect(width / 2 - width / 4 - 80, height / 2 + 20, 120, 50), 3)

        # If mouse on instructions button
        if width / 2 - 100 - 10 <= mouse[0] <= width / 2 - 100 - 10+250 and height / 2 + 80 <= mouse[1] <= height / 2 + 80 + 50:
            pygame.draw.rect(screen1, (255, 164, 132), pygame.Rect(width / 2 - 100 - 10, height / 2 + 80, 250, 50))
            pygame.draw.rect(screen1, (255, 0, 0), pygame.Rect(width / 2 - 100 - 10, height / 2 + 80, 250, 50), 3)

        # If mouse on Quit button
        if width / 2 + width / 4 - 5 <= mouse[0] <= width / 2 + width / 4 - 5 + 90 and height / 2 + 140 - 3 <= mouse[1] <= height / 2 + 140 - 3 + 40:
            pygame.draw.rect(screen1, (255, 164, 132), pygame.Rect(width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40))
            pygame.draw.rect(screen1, (255, 0, 0), pygame.Rect(width / 2 + width / 4 - 5, height / 2 + 140 - 3, 90, 40), 3)

        # the text onto our button
        screen1.blit(text1, (width / 2 - width/4-65, height / 2+33))
        screen1.blit(text2, (width / 2-100 + 10, height / 2+93))
        screen1.blit(text3, (width / 2 + width/4 + 5, height / 2+145))
        screen1.blit(text5, (width / 2 -150 , height / 2 -40))

        # updates the frames of the game
        pygame.display.update()

start()
