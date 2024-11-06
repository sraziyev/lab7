import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("music")

playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song_index = 0

pygame.mixer.music.load(playlist[current_song_index])

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song_index])
    pygame.mixer.music.play()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song_index])
    pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # P for play
                play_music()
            elif event.key == pygame.K_s:  # S for stop
                stop_music()
            elif event.key == pygame.K_n:  # N for next
                next_song()
            elif event.key == pygame.K_b:  # B for before
                previous_song()

    screen.fill((255, 255, 255))
    
    pygame.display.flip()
