import pygame

pygame.init()

screen_width = 1000  # les dimensions de la fenêtre de jeu (largeur et hauteur)
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2048")


def ask_int(message: str, min: int, max: int):
    run2 = True
    while run2:
        try:
            check: int = int(input(message))
            if min <= check <= max:
                break
            else:
                print(f'veuillez rentrer un nombre entre {min} et {max}')
        except ValueError:
            print("veuillez rentrer un nombre valide")
    return check


def draw_text(text, font, text_col, x, y):  # fonction qui définit la position du texte sur l'écran
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# grid_lenght = ask_int("Choisissez la taille de la grille entre 4 et 10", 4, 10)


font = pygame.font.SysFont('Bauhaus 93', 70)
tile_size = screen_width / 4
game_over = 0
score = 0
end_menu = False
start_menu = True

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

start_button_img = pygame.image.load("assets/start_button.png")


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        action = False
        # on obtient la position de la souris avec la fonction pygame.mouse.get_pos()
        pos = pygame.mouse.get_pos()

        # on vérifie si la souris passe au dessus du bouton et le clique de la souris sur le bouton avec la fonction get_pressed de pygame
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # on dessine les boutons
        screen.blit(self.image, self.rect)

        return action


start_button = Button(screen_width // 2 - 450, screen_height // 50 + 300, start_button_img)

run = True
while run:

    pygame.display.flip()

    if start_menu:
        draw_text('Bienvenue sur le 2048 !', font, white, 200, 100)
        if start_button.draw():
            start_menu = False
    else:
        pass
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Fermeture ....")
            run = False

    pygame.display.update()

pygame.quit()
