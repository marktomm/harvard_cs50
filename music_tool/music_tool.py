import pygame.mixer

# Initialize the mixer module
pygame.mixer.init()

# Map keys to notes
NOTE_MAPPING = {
    'a': 'notes/c4.wav',
    's': 'notes/d4.wav',
    'd': 'notes/e4.wav',
    'f': 'notes/f4.wav',
    'g': 'notes/g4.wav',
    'h': 'notes/a4.wav',
    'j': 'notes/b4.wav',
    'w': 'notes/s1.wav',
    'e': 'notes/s2.wav'
}

def play_note(key):
    """Play the note associated with the given key."""
    note_file = NOTE_MAPPING.get(key)
    if note_file:
        sound = pygame.mixer.Sound(note_file)
        sound.play()

print("Mini Piano! Press keys (a, s, d, f, g, h, j, w, e) to play notes. Press 'q' to quit.")
while True:
    key = input("Press a key: ")
    if key == 'q':
        break
    play_note(key)
