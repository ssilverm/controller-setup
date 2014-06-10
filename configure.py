import json
import sys
import os
import pygame
from pygame.locals import *
import subprocess

pygame.init()
pygame.font.init()
pygame.joystick.init()

#  Try to initialize the first joystick
try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
except:
    pass

#  Formatters available 
formatters_available = filter(lambda x: x[-3:]==".py", os.listdir('formatters'))

#  What controller are we configuring?
controllers_available = os.listdir('controllers')

if len(sys.argv) > 1:
    controllers = sys.argv[1:]
else:
    controllers = controllers_available

events_to_capture = [KEYUP, JOYBUTTONUP, JOYHATMOTION, JOYAXISMOTION]

#  Initialize screen
pygame.display.init()
dinfo = pygame.display.Info()
fullscreen = False

flag = 0
if fullscreen:
    flag = pygame.FULLSCREEN

if (pygame.display.mode_ok((dinfo.current_w,dinfo.current_h),pygame.FULLSCREEN)):
    windowSurface = pygame.display.set_mode((dinfo.current_w, dinfo.current_h), flag)
else:
    pygame.quit()
    sys.exit()



#windowSurface = pygame.display.set_mode((0,0), 0, 32)

center_x = windowSurface.get_rect().centerx
center_y = windowSurface.get_rect().centery


#  Setup font
font_size = 24
font = pygame.font.SysFont(None, font_size)

def render():  
    windowSurface.fill((0, 0, 0))
    
    #  Display controller image
    windowSurface.blit(controllerImage, controllerImageRect)

    #  Display the controller label
    text = font.render("Controller: " + controller['name'], True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = center_x
    textRect.centery = controllerImageRect[1] - font_size/2
    windowSurface.blit(text, textRect)
    
    #  Display what button we're currently configuring
    key_text = font.render("Currently configuring button: "+ buttons_to_update[current_button], True, (255, 255, 255), (0, 0, 0))
    currentTextRect = key_text.get_rect()
    currentTextRect.centerx = windowSurface.get_rect().centerx
    currentTextRect.centery = controllerImageRect[1] + controllerImageRect[3] + font_size/2
    windowSurface.blit(key_text, currentTextRect) 
    
    pygame.display.update()

for selected_controller in controllers:
    #  Read in controller data
    input_path = "controllers/" + selected_controller
    try:
        input_text = open(input_path + "/info.json").read()
    except:
        print "Invalid controller: %s. Skipping" % selected_controller
        continue
    controller = json.loads(input_text)

    #  Load controller image
    controllerImage = pygame.image.load(input_path + '/'+controller['image']).convert()

    #  Setup where controller image will be drawn
    controllerImageRect = controllerImage.get_rect()
    controllerImageRect.centerx = center_x
    controllerImageRect.centery = center_y

    #  Which button are we adjusting?
    current_button = 0
    buttons_to_update = controller['controls']
    '''
        KEYUP = scancode, key, mod
        JOYBUTTONUP = joy, button
        JOYHATMOTION = joy, hat, value
    '''

    mapping = {}
    running = True
    render()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type in events_to_capture:
                if event.type == KEYUP:
                    mapping[buttons_to_update[current_button]] = {"type":event.type, "key":event.key, "mod": event.mod}
                
                elif event.type == JOYBUTTONUP:
                    mapping[buttons_to_update[current_button]] = {"type":event.type, "button":event.button, "joy": event.joy}
                
                elif event.type == JOYHATMOTION:
                    #  Skip the event of the joystick reseting to 0, 0
                    if event.value == (0,0):
                        continue
                    mapping[buttons_to_update[current_button]] = {"type": event.type, "value": event.value, "joy": event.joy}
                
                elif event.type == JOYAXISMOTION:
                    #  Skip if the press wasn't 'hard' enough
                    if event.value < 1.0 and event.value > -1.0:
                        continue
                    mapping[buttons_to_update[current_button]] = {"type": event.type, "value": event.value, "axis": event.axis, "joy": event.joy}
                
                #  Advance to next button
                current_button += 1
                if current_button >= len(buttons_to_update):
                    current_button = 0
                    running = False
                else:
                    render()

    #  Output our mapping
    with open(controller['name'] + ".json", "w") as output_file:
        output_file.write(json.dumps(mapping, indent=4, separators=(',', ': ')))

    output_directory = None
    if "output directory" in controller:
        output_directory = controller['output directory']
    else:
        output_directory = "output/"+controller['name']
    #  Call Formatters
    if "formatters" in controller:
        for formatter in controller['formatters']:
            try:
                subprocess.call([sys.executable, "formatters/"+formatter, controller['name'] + ".json ", output_directory+"/"+formatter[:-3]])
            except:
                print formatter + " has failed."
