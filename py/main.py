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

class TextBox: #TextBox class for creating text boxes
    def __init__(self, text, pos, font="comicsansms", fontSize=20, fontColour=colours["black"], tags=[]):
        self.text = text
        self.pos = pos
        self.fontSize = fontSize
        self.fontColour = fontColour
        self.font = font
        self.tags = tags
        
    def Draw(self): #called each frame, draws the object to the screen
        textSurf = pygame.font.SysFont(self.font, self.fontSize).render(self.text, True, self.fontColour)
        textRect = textSurf.get_rect()
        textRect.center = (self.pos) 
        window.blit(textSurf, textRect) 

    def GetTags(self):
        return self.tags

    def SetText(self, newText):
        self.text = newText

    def SetPos(self, newPos):
        self.pos = newPos

    def GetText(self):
        return self.text

########################################################################################################
#                                            - Functions -                                             #
########################################################################################################

def MainMenu():
    #Set Starting Variables
    mainMenu = True
    customObjectsList = []
    allSpritesList = pygame.sprite.Group()
    buttonList = pygame.sprite.Group()
    
    #Add the play button to the menu
    playButton = Button((int(resolution[0] / 2), int(resolution[1] / 2)), "Sprites/MainMenuSprites/PlayDefault.png", "Sprites/MainMenuSprites/PlayHover.png", ChooseSave, tags=["Button", "MainMenu"])
    allSpritesList.add(playButton)
    buttonList.add(playButton)
    
    #Add the title text
    title = TextBox("Dungeon Crawler", (400, 135), fontSize=100, tags=["TextBox", "MainMenu"])
    customObjectsList.append(title)

    #While loop for the running of the menu
    while mainMenu:
        window.fill((255, 255, 255)) #Clear the screen
        mouse = pygame.mouse.get_pos() #Get the position of the mouse this frame

        #Check each event this frame
        for event in pygame.event.get():
            #If the user is exiting the application
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            #Upon mouseclick
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = [s for s in buttonList if s.rect.collidepoint(mouse)]
                for button in clicked:
                    button.OnClick()
        
        #
        # Temporary lines for plotting main menu
        #

        pygame.draw.line(window, colours["black"], (0, 570), (1280, 570), 1)
        pygame.draw.line(window, colours["black"], (0, 470), (1280, 470), 1)
        pygame.draw.line(window, colours["black"], (0, 370), (1280, 370), 1)
        pygame.draw.line(window, colours["black"], (0, 270), (1280, 270), 1)

        #
        #
        #


        #Draw Button Visuals
        hoveredButtons = [s for s in buttonList if s.rect.collidepoint(mouse)]
        notHoveredButtons = [s for s in buttonList if not s.rect.collidepoint(mouse)]

        for button in notHoveredButtons:
            button.ResetSprite()
        for button in hoveredButtons:
            button.OnHover()

        #Draw all custom objects
        for item in customObjectsList:
            item.Draw()
        
        #Final things
        allSpritesList.draw(window)
        pygame.display.update()
        clock.tick(30)

def ChooseSave():
    print("ChooseSave")

def settings():
    print("Settings")

MainMenu()
