import pygame


class ImageButton:
    def __init__(
            self,
            image,
            hover_image=None,
            text="",
            sound=None,
            size=None,
            font_size=32,
            text_color=(255, 255, 255),
            position=(0, 0)
    ):

        self.image = pygame.image.load(image).convert_alpha()


        if hover_image:
            self.hover_image = pygame.image.load(hover_image).convert_alpha()
        else:
            self.hover_image = self.image


        if size:
            self.image = pygame.transform.scale(self.image, size)
            self.hover_image = pygame.transform.scale(
                self.hover_image,
                size
            )


        self.rect = self.image.get_rect(topleft=position)


        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color


        if sound:
            self.sound = pygame.mixer.Sound(sound)
        else:
            self.sound = None

        # Состояние
        self.hovered = False

    def draw(self, screen):


        mouse_pos = pygame.mouse.get_pos()

        self.hovered = self.rect.collidepoint(mouse_pos)

        if self.hovered:
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

        # Текст
        if self.text:
            text_surface = self.font.render(
                self.text,
                True,
                self.text_color
            )

            text_rect = text_surface.get_rect(
                center=self.rect.center
            )

            screen.blit(text_surface, text_rect)

    def blit(self, screen, position=None):


        if position:
            self.rect.topleft = position

        self.draw(screen)

    def click(self, event):


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if self.rect.collidepoint(event.pos):

                    if self.sound:
                        pygame.mixer.Channel(0).play(self.sound)

                    return True

        return False