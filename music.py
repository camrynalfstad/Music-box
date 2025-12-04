import pygame
from gpiozero import Button
from signal import pause

pygame.init()

button_sounds = {Button(4): pygame.mixer.Sound("drum_tom_mid_hard.wav"),
                 Button(17): pygame.mixer.Sound("drum_cymbal_hard.wav"),
                 Button(27): pygame.mixer.Sound("drum_snare_hard.wav"),
                 Button(10): pygame.mixer.Sound("drum_cowbell.wav")}

for button, sound in button_sounds.items():
    button.when_pressed = sound.play

pause()
