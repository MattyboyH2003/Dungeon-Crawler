import copy
import pygame
from colours import colours

########################################################################################################
#                                              - Setup -                                               #
########################################################################################################

if __name__ == "__main__":
    pygame.init()
    resolution = (1280, 720)
    pygame.display.set_caption("Dungeon Crawler")
    window = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
else:
    exit()

########################################################################################################
#                                              - Classes -                                             #
########################################################################################################

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, sprite, hoverSprite=None, func=None, params={}, tags=[]):
        self.pos = pos
        self.defaultSprite = sprite

        if not hoverSprite:
            self.hoverEnabled = False
        else:
            self.hoverEnabled = True
            self.hoverSprite = hoverSprite

        self.func = func
        self.params = params

        self.tags = tags
        
        #Spritey Things
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite).convert()
        self.image.set_colorkey(colours["colourKey"])
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def SetParams(self, newParams):
        self.params = newParams

    def GetTags(self):
        return self.tags
    
    def ResetSprite(self):
        self.image = pygame.image.load(self.defaultSprite).convert()
    
    def OnHover(self):
        if self.hoverEnabled:
            self.image = pygame.image.load(self.hoverSprite).convert()
    
    def OnClick(self):
        self.func(**self.params)

########################################################################################################
#                                            - Functions -                                             #
########################################################################################################

def MainMenu():
    mainMenu = True
    allSpritesList = pygame.sprite.Group()
    buttonList = pygame.sprite.Group()
    
    playButton = Button((int(resolution[0] / 2), int(resolution[1] / 2)), "Sprites/MainMenuSprites/PlayDefault.png", "Sprites/MainMenuSprites/PlayHover.png", aha, tags=["Button", "MainMenu"])
    allSpritesList.add(playButton)
    buttonList.add(playButton)
    
    while mainMenu:
        window.fill((255, 255, 255))
        mouse = pygame.mouse.get_pos()

        #Check events 'n' shit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [s for s in buttonList if s.rect.collidepoint(mouse)]
                for button in clicked:
                    button.OnClick()
        
        #Set Button Visuals
        hoveredButtons = [s for s in buttonList if s.rect.collidepoint(mouse)]
        notHoveredButtons = [s for s in buttonList if not s.rect.collidepoint(mouse)]

        for button in notHoveredButtons:
            button.ResetSprite()
        for button in hoveredButtons:
            button.OnHover()

        allSpritesList.draw(window)
        pygame.display.update()
        clock.tick(30)

def aha():
    print("cheese")

MainMenu()
