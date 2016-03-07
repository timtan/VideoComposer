# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import pygame

width = 320
height = 240

pygame.init()

sections = [
        {
            'type' : "image",
            'file': 'lin.jpg',
            'caption': u"下一任台灣女總統!?",
            'second' : 3, 
            },
        {
            'type' : "video",
            'file' : 's.mpg',
            'caption': u"wow",
            },
        ]

font = pygame.font.Font('MSJH.TTF', 30) 

FPS = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

for section in sections:

    section_type = section['type']

    if section_type == 'video':

        file_name = section['file']
        pygame.mixer.quit()
        movie = pygame.movie.Movie(file_name)
        movie_screen = pygame.Surface((width, height)).convert()
        movie.set_display(movie_screen)
        movie.play()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  

            if not movie.get_busy():
                break

            screen.blit(movie_screen,(0,0))
            pygame.display.flip()

            clock.tick(FPS)

    elif section_type == 'image':

        file_name = section['file']

        image = pygame.image.load(file_name)
        image_rect = image.get_rect()

        caption = section['caption']
        second = section['second']

        text = font.render(caption, 1, (10, 10, 10))

        for tick in range(second*FPS):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  

            screen.blit(image, (-1* tick,-1*tick))
            screen.blit(text, (10, 150))

            pygame.display.flip()

            clock.tick(FPS)



pygame.quit()  
