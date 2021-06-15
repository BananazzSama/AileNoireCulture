import pygame
import time
import sys
import os
import random
import csv
from pygame import event
from pygame.display import update

from csv import reader

pygame.init()

username = "Random"

play = True

clock = pygame.time.Clock()

#ECRAN
display_width = 1600
display_height = 900
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Aile Noire Culture")

#CONSTANTES
##POLICES
defaultFont = pygame.font.Font("fonts/Nunito-SemiBold.ttf", 30)
nunito_extrabold = pygame.font.Font("fonts/Nunito-ExtraBold.ttf", 30)

##COULEURS
black = (0, 0, 0)
white = (255, 255, 255)
grey = (204, 204, 204)
darkgrey = (39, 39, 39)
green = (101, 255, 43)
orange = (255, 147, 17)
red = (244, 12, 12)
purple = (106, 5, 86)

#BDD QUESTIONS
##AJOUTER LES QUESTIONS LEAGUE OF LEGENDS
def addLolQuestions():
    with open('playlists/LeagueOfLegends.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                print(row[0])
                questionImage.append("questions/" + row[0] + ".png")
                questionLabel.append(row[1])
                questionDifficulty.append(row[2])
                questionCorrection.append(row[3])

##PLAYLIST NORMAL
normalQuestionImage = ["questions/makima3.png", "questions/keisuke_baji.png", "questions/d4c.png", "questions/ayame_kamijou.jpg", "questions/robin.jpg" , "questions/Chaos.png", "questions/Charles_Leclerc.png", "questions/Dajbog_uzumaki.png", "questions/Diarmuid_Ua_Duibhne.png", "questions/DJ_Octavio.png", "questions/Erdrick.png", "questions/Falco.png", "questions/Gaster.png", "questions/Giygas.png", "questions/Hitosh_Shinso.png", "questions/Kefka.png", "questions/Ledros.png", "questions/N.png", "questions/No_face.png", "questions/Roronoa_Zoro.png", "questions/Shawn_Froste.png", "questions/Tabuu.png", "questions/Tyler1.png", "questions/Woody_Woodpecker.png", "questions/Zero.png", "questions/Zoroark.png", "questions/Zorori.jpg", "questions/Zorro.png"]
normalQuestionLabel = ["Qui est ce personnage ?", "Qui est ce personnage ?", "Quel est le nom exact de ce stand (JJBA) ?", "Qui est ce personnage ?", "Quel est le nom du 3ème Robin ?" , "Comment s'appelle ce personnage ?" , "Comment s'appelle cette personnalité ?", "à quel clan appartient ce jeune apprenti ?" , "Comment s'appelle cette personnalité représentée dans Fate (existant aussi dans la vraie vie) ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ? (point bonus avec le nom de famille)", "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?", "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de cette personnalité plutôt connue",  "Quel est le nom de ce personnage ?", "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?" , "Quel est le nom de ce personnage ?"   ]
normalQuestionDifficulty = ["Facile", "Facile", "Difficile", "Hardcore", "Moyen", "Hardcore" , "Moyen" , "Facile" , "Hardcore" , "Hardcore" , "Moyen" , "Facile" , "Difficile" , "Hardcore" , "Moyen" , "Difficile", "Hardcore" , "Moyen" , "Moyen", "Facile", "Facile" , "Hardcore" , "Facile", "Facile" , "Moyen", "Difficile" , "Hardcore" , "Facile"]
normalQuestionCorrection = ["Makima (Chainsaw Man)", "Keisuke Baji (Tokyo Revengers)", "Dirty Deeds Done Dirt Cheap", "Ayame Kamijou (Real Account)", "Tim Drake" , "Chaos (Sonic)" , "Charles Leclerc", "jsp", "Diarmuid Ua Duibhne", "DJ Octavio (Splatoon)", "Elric (Dragon Quest)", "Falco Lombardi", "W. D. Gaster", "Giygas", "Hitoshi Shinso", "Kefka (FF)", "Commandant Ledros(Runeterra)", "N (Pokemon)", "No Face / Sans Visage (Voyage de chihiro)", "Roronoa Zoro", "Shawn Froste", "Tabuu (Smash Bros)", "Tyler1", "Woody Woodpecker", "Zero (Megaman)", "Zoroark", "Zorori (le magnifique)", "Zorro"]

##AJOUTER LES QUESTIONS NORMAL
def addNormalQuestions():
    questionImage.extend(normalQuestionImage)
    questionLabel.extend(normalQuestionLabel)
    questionDifficulty.extend(normalQuestionDifficulty)
    questionCorrection.extend(normalQuestionCorrection)

##AJOUTER LES QUESTIONS CHEVEUX VERTS
def addCheveuxVertsQuestions():
    with open('playlists/CheveuxVerts.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                print(row[0])
                questionImage.append("questions/" + row[0] + ".png")
                questionLabel.append(row[1])
                questionDifficulty.append(row[2])
                questionCorrection.append(row[3])

questionImage = []
questionLabel = []
questionDifficulty = []
questionCorrection = []

correctionQuestionImage = []
correctionQuestionLabel = []
correctionQuestionDifficulty = []
correctionQuestionCorrection = []

listeAvatar = ["froompa" , "placeholder2" , "placeholder1", "placeholder3", "placeholder4"]
listeAvatar2 = []


answers = []
j = 0

userScore = 0


questionNumber = 0
howManyQuestions = 2   #int(input())

lolPlaylistActive = False
normalPlaylistActive = False
cheveuxVertsPlaylistActive = False



print(len(questionCorrection))

def main_menu():
    logo = pygame.image.load("ui/logo.png")
    logoRect = logo.get_rect(center=(display_width/2, 300))

    playButton = defaultFont.render("JOUER", True, white)
    playButtonRect = playButton.get_rect(center=(display_width/2, 600))

    while play:
        screen.fill(darkgrey)
        screen.blit(logo, logoRect)
        screen.blit(playButton, playButtonRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if playButtonRect.collidepoint(x, y):
                        #player_customization()
                        pre_game_lobby()

        pygame.display.update()

def player_customization():
    global howManyQuestions
    global username

    typingActive = True

    name = defaultFont.render("Nom d'utilisateur", True, white)
    nameRect = name.get_rect(center=(display_width/2, 50))

    userTextBackgroundBorder = pygame.Rect(0, 80, 708, 68)
    userTextBackgroundBorder.centerx = display_width/2

    userTextBackground = pygame.Rect(0, 0, 700, 60)
    userTextBackground.center = userTextBackgroundBorder.center


    #BUTTONS
    createGameButton = pygame.Rect(0, 0, 400, 60)
    createGameButton.centerx = display_width/2 - 530
    createGameButton.centery = 810

    joinGameButton = pygame.Rect(0, 0, 400, 60)
    joinGameButton.centerx = display_width/2 + 530
    joinGameButton.centery = 810

    newText = username

    while play:
        screen.fill(darkgrey)

        userTextSurface = defaultFont.render(newText, True, black)
        userTextRect = userTextSurface.get_rect(center=(display_width/2, 110))

        if typingActive == True:
            pygame.draw.rect(screen, black, userTextBackgroundBorder)
            pygame.draw.rect(screen, white, userTextBackground)
        else:
            pygame.draw.rect(screen, black, userTextBackgroundBorder)
            pygame.draw.rect(screen, grey, userTextBackground)

        pygame.draw.rect(screen, black, createGameButton)
        pygame.draw.rect(screen, black, joinGameButton)

        screen.blit(name, nameRect)
        screen.blit(userTextSurface, userTextRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if typingActive:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        newText = newText[:-1]
                    else:
                        newText += event.unicode
                        newText = newText[:12]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    username = newText[:-1]
                    question()

            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if userTextBackground.collidepoint(x, y):
                        typingActive = True
                    else:
                        typingActive = False

        pygame.display.update()

def recursif():
    global actu
    global playerAvatar
    actu = "ui/avatars/" + random.choice(listeAvatar) + ".png"
    if actu == playerAvatar:
        recursif()

def pre_game_lobby():
    global howManyQuestions
    global username
    global actu
    global playerAvatar
    typingActive = True

    name = defaultFont.render("Nom d'utilisateur", True, white)
    nameRect = name.get_rect(center=(display_width/2, 50))

    userTextBackgroundBorder = pygame.Rect(0, 80, 708, 68)
    userTextBackgroundBorder.centerx = display_width/2

    userTextBackground = pygame.Rect(0, 0, 700, 60)
    userTextBackground.center = userTextBackgroundBorder.center


    #BUTTONS
    createGameButton = pygame.Rect(0, 0, 400, 60)
    createGameButton.centerx = display_width/2 - 530
    createGameButton.centery = 810

    joinGameButton = pygame.Rect(0, 0, 400, 60)
    joinGameButton.centerx = display_width/2 + 530
    joinGameButton.centery = 810

    newText = "Random"
    playerAvatar = "ui/avatars/froompa.png"
    screen.fill(darkgrey)
    screen.blit(pygame.image.load("ui/avatars/rien.png"), (1434, 10))
    actu = "ui/avatars/froompa.png"



    while play:


        userTextSurface = defaultFont.render(newText, True, black)
        userTextRect = userTextSurface.get_rect(center=(display_width/2, 110))

        if typingActive == True:
            pygame.draw.rect(screen, black, userTextBackgroundBorder)
            pygame.draw.rect(screen, white, userTextBackground)
        else:
            pygame.draw.rect(screen, black, userTextBackgroundBorder)
            pygame.draw.rect(screen, grey, userTextBackground)

        pygame.draw.rect(screen, black, createGameButton)
        pygame.draw.rect(screen, black, joinGameButton)

        screen.blit(name, nameRect)
        screen.blit(userTextSurface, userTextRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if typingActive:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        newText = newText[:-1]
                    else:
                        newText += event.unicode
                        newText = newText[:12]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    username = newText
                    playlist_selection()

            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if userTextBackground.collidepoint(x, y):
                        typingActive = True
                    else:
                        typingActive = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 1434 < mouse[0] < 1600 and 10 < mouse[1] < 176:
                        recursif()
                        playerAvatar = actu
                        screen.blit(pygame.image.load(playerAvatar), (1434, 10))

        pygame.display.update()

def playlist_selection():
    global username

    global lolPlaylistActive
    global normalPlaylistActive
    global cheveuxVertsPlaylistActive

    lolPlaylist = defaultFont.render("League of Legends", True, white)
    lolPlaylistRect = lolPlaylist.get_rect(topleft=(20, 20))
    deactivateLolPlaylistButton = pygame.image.load("ui/deactivate.png")
    activateLolPlaylistButton = pygame.image.load("ui/activate.png")
    deactivateLolPlaylistButtonRect = deactivateLolPlaylistButton.get_rect(topleft=(300, 28))
    activateLolPlaylistButtonRect = deactivateLolPlaylistButton.get_rect(topleft=(350, 28))

    cheveuxVertsPlaylist = defaultFont.render("Cheveux Verts", True, white)
    cheveuxVertsPlaylistRect = cheveuxVertsPlaylist.get_rect(topleft=(20, 60))
    deactivateCheveuxVertsPlaylistButton = pygame.image.load("ui/deactivate.png")
    activateCheveuxVertsPlaylistButton = pygame.image.load("ui/activate.png")
    deactivateCheveuxVertsPlaylistButtonRect = deactivateCheveuxVertsPlaylistButton.get_rect(topleft=(300, 68))
    activateCheveuxVertsPlaylistButtonRect = activateCheveuxVertsPlaylistButton.get_rect(topleft=(350, 68))

    normalPlaylist = defaultFont.render("Normal", True, white)
    normalPlaylistRect = normalPlaylist.get_rect(center=(display_width/2, 60))
    deactivateNormalPlaylistButton = pygame.image.load("ui/deactivate.png")
    activateNormalPlaylistButton = pygame.image.load("ui/activate.png")
    deactivateNormalPlaylistButtonRect = deactivateNormalPlaylistButton.get_rect(topleft=(300, 28))
    activateNormalPlaylistButtonRect = deactivateNormalPlaylistButton.get_rect(topleft=(350, 28))



    while play:
        screen.fill(darkgrey)

        screen.blit(lolPlaylist, lolPlaylistRect)
        screen.blit(deactivateLolPlaylistButton, deactivateLolPlaylistButtonRect)
        screen.blit(activateLolPlaylistButton, activateLolPlaylistButtonRect)

        screen.blit(cheveuxVertsPlaylist, cheveuxVertsPlaylistRect)
        screen.blit(deactivateCheveuxVertsPlaylistButton, deactivateCheveuxVertsPlaylistButtonRect)
        screen.blit(activateCheveuxVertsPlaylistButton, activateCheveuxVertsPlaylistButtonRect)

        #screen.blit(lolPlaylist, lolPlaylistRect)
        #screen.blit(normalPlaylist, normalPlaylistRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if activateLolPlaylistButtonRect.collidepoint(x, y):
                        print("Playlist LoL ACTIVE")
                        lolPlaylistActive = True
                    elif deactivateLolPlaylistButtonRect.collidepoint(x, y):
                        print("Playlist LoL INACTIVE")
                        lolPlaylistActive = False
                    elif activateNormalPlaylistButtonRect.collidepoint(x, y):
                        print("Playlist Normal ACTIVE")
                        normalPlaylistActive = True
                    elif deactivateNormalPlaylistButtonRect.collidepoint(x, y):
                        print("Playlist Normal INACTIVE")
                        normalPlaylistActive = False
                    elif activateCheveuxVertsPlaylistButtonRect.collidepoint(x, y):
                        print("Playlist Cheveux Verts ACTIVE")
                        cheveuxVertsPlaylistActive = True
                    elif deactivateCheveuxVertsPlaylistButtonRect.collidepoint(x, y):
                        print("Playlist Cheveux Verts INACTIVE")
                        cheveuxVertsPlaylistActive = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if lolPlaylistActive:
                        addLolQuestions()
                    if normalPlaylistActive:
                        addNormalQuestions()
                    if cheveuxVertsPlaylistActive:
                        addCheveuxVertsQuestions()
                    question()


        pygame.display.update()
        clock.tick(60)

def question():
    global username

    #AVATAR/COSMETIC
    playerAvatar = pygame.image.load("ui/avatars/froompa.png")
    

    isCorrection = False
    global howManyQuestions
    global questionNumber
    questionNumber += 1
    difficultyColor = white

    typingActive = True

    if len(questionImage) == 1:
        i = 0
    else:
        i = random.randint(0, len(questionImage)-1)

    choosedImage = questionImage[i]
    choosedQuestion = questionLabel[i]
    choosedDifficulty = questionDifficulty[i]
    choosedCorrection = questionCorrection[i]

    correctionQuestionImage.append(questionImage[i])
    correctionQuestionLabel.append(questionLabel[i])
    correctionQuestionDifficulty.append(questionDifficulty[i])
    correctionQuestionCorrection.append(questionCorrection[i])

    loadQuestionImage = pygame.image.load(choosedImage)
    loadQuestionImageRect = loadQuestionImage.get_rect(center=(display_width/2, 320))

    loadQuestionLabel = defaultFont.render(choosedQuestion, True, white)
    loadQuestionLabelRect = loadQuestionLabel.get_rect(center=(display_width/2, 680))

    loadQuestionNumber = nunito_extrabold.render("Question " + str(questionNumber) + "/" + str(howManyQuestions), True, white)
    loadQuestionNumberRect = loadQuestionNumber.get_rect(topleft=(20, 20))

    if questionNumber > howManyQuestions:
        isCorrection = True

    if choosedDifficulty == "Facile":
        difficultyColor = green
    elif choosedDifficulty == "Moyen":
        difficultyColor = orange
    elif choosedDifficulty == "Difficile":
        difficultyColor = red
    elif choosedDifficulty == "Hardcore":
        difficultyColor = purple

    loadQuestionDifficulty = defaultFont.render(str(choosedDifficulty), True, difficultyColor)
    loadQuestionDifficultyRect = loadQuestionDifficulty.get_rect(topleft=(20, 60))

    userTextBackgroundBorder = pygame.Rect(0, 750, 708, 68)
    userTextBackgroundBorder.centerx = display_width/2

    userTextBackground = pygame.Rect(0, 0, 700, 60)
    userTextBackground.center = userTextBackgroundBorder.center

    newText = ""

    while play:
        screen.fill(darkgrey)

        userTextSurface = defaultFont.render(newText, True, black)
        userTextRect = userTextSurface.get_rect(center=(display_width/2, 780))

        if typingActive == True:
            pygame.draw.rect(screen, black, userTextBackgroundBorder)
            pygame.draw.rect(screen, white, userTextBackground)
        else:
            pygame.draw.rect(screen, black, userTextBackgroundBorder)
            pygame.draw.rect(screen, grey, userTextBackground)


        screen.blit(playerAvatar, (1434, 10))
        screen.blit(userTextSurface, userTextRect)
        screen.blit(loadQuestionLabel, loadQuestionLabelRect)
        screen.blit(loadQuestionImage, loadQuestionImageRect)
        screen.blit(loadQuestionNumber, loadQuestionNumberRect)
        screen.blit(loadQuestionDifficulty, loadQuestionDifficultyRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if typingActive:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        newText = newText[:-1]
                    else:
                        newText += event.unicode

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(questionImage) == 1:
                        del questionImage[i]
                        del questionLabel[i]
                        del questionDifficulty[i]
                        del questionCorrection[i]
                        answers.append(newText[:-1])
                        isCorrection = True
                    else: 
                        del questionImage[i]
                        del questionLabel[i]
                        del questionDifficulty[i]
                        del questionCorrection[i]
                        answers.append(newText[:-1])
                        question()

            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if userTextBackground.collidepoint(x, y):
                        typingActive = True
                    else:
                        typingActive = False

        if isCorrection:
            correction()

        pygame.display.update()
        clock.tick(60)

def correction():
    global j
    global userScore
    global username




    choosedImage = correctionQuestionImage[j]
    choosedQuestion = correctionQuestionLabel[j]
    choosedCorrection = correctionQuestionCorrection[j]
    choosedDifficulty = correctionQuestionDifficulty[j]
    answer = answers[j]

    loadQuestionImage = pygame.image.load(choosedImage)
    loadQuestionImageRect = loadQuestionImage.get_rect(center=(display_width/2, 320))

    loadQuestionLabel = defaultFont.render(choosedQuestion, True, white)
    loadQuestionLabelRect = loadQuestionLabel.get_rect(center=(display_width/2, 680))

    loadQuestionCorrection = nunito_extrabold.render(choosedCorrection, True, green)
    loadQuestionCorrectionRect = loadQuestionCorrection.get_rect(center=(display_width/2, 630))

    answerTextSurface = defaultFont.render(str(answer), True, white)
    answerTextRect = answerTextSurface.get_rect(center=(display_width/2, 780))

    correctionLabel = nunito_extrabold.render("Correction", True, white)
    correctionLabelRect = correctionLabel.get_rect(topleft=(20, 20))

    playerLabel = defaultFont.render(username, True, white)
    playerLabelRect = playerLabel.get_rect(topleft=(20, 60))

    falseButton = pygame.image.load("ui/false.png")
    falseButtonRect = falseButton.get_rect(center=(display_width/2 - 400, 800))

    trueButton = pygame.image.load("ui/true.png")
    trueButtonRect = trueButton.get_rect(center=(display_width/2 + 400, 800))

    while play:
        screen.fill(darkgrey)

        screen.blit(answerTextSurface, answerTextRect)
        screen.blit(loadQuestionLabel, loadQuestionLabelRect)
        screen.blit(loadQuestionImage, loadQuestionImageRect)
        screen.blit(loadQuestionCorrection, loadQuestionCorrectionRect)
        screen.blit(correctionLabel, correctionLabelRect)
        screen.blit(playerLabel, playerLabelRect)
        screen.blit(falseButton, falseButtonRect)
        screen.blit(trueButton, trueButtonRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if falseButtonRect.collidepoint(x, y):
                        j += 1
                        print(userScore)
                        correction()
                    elif trueButtonRect.collidepoint(x, y):
                        if choosedDifficulty == "Facile":
                            userScore += 1
                        elif choosedDifficulty == "Moyen":
                            userScore += 2
                        elif choosedDifficulty == "Difficile":
                            userScore += 3
                        elif choosedDifficulty == "Hardcore":
                            userScore += 4
                        j += 1
                        print(userScore)
                        correction()

        pygame.display.update()
        clock.tick(60)
            

            

while play:

    main_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)