## What is a variable?
1. **What is a variable?**
   - A box to store information that you find important to use later.
   
2. **Why is it needed?**
   - To remember and use information (people names, numbers, files, website names).
   
3. **What is it used for?**
   - Holding and changing information.
   
4. **What is not possible to do without it?**
   - Remember information in a program.

**Examples related to music:**
   - Storing the name of a song: `song_name = "Happy Birthday"`
   - Remembering an artist's name: `artist = "Beatles"`
   - Keeping track of song duration: `duration = 3.5` (minutes)
   - Saving an album title: `album = "Abbey Road"`

---

## What is a List?
1. **What is a List?**
   - A collection of items, like a music playlist, stored in a specific order.
   
2. **Why is it needed?**
   - To keep multiple items together and access them using their position.
   
3. **What is it used for?**
   - Storing and organizing multiple items.
   
4. **What is not possible to do without it?**
   - Easily manage and access a sequence of items.

**Examples related to music:**
   - Creating a playlist: `songs = ["Imagine", "Yesterday", "Billie Jean"]`
   - Accessing the first song: `first_song = songs[0]`
   - Adding a new song to the playlist: `songs.append("Bohemian Rhapsody")`
   - Removing a song: `songs.remove("Billie Jean")`

---

## What is a Dictionary?
1. **What is a Dictionary?**
   - A collection where each item has a unique name (key) and a value, like a song and its artist.
   
2. **Why is it needed?**
   - To pair and store information that belongs together.
   
3. **What is it used for?**
   - Storing items with a unique identifier.
   
4. **What is not possible to do without it?**
   - Easily pair and lookup values based on a unique key.

**Examples related to music:**
   - Creating a music library: `library = {"Imagine": "John Lennon", "Yesterday": "The Beatles", "Billie Jean": "Michael Jackson"}`
   - Finding the artist of "Imagine": `artist = library["Imagine"]`
   - Adding a new song: `library["Bohemian Rhapsody"] = "Queen"`
   - Removing a song: `del library["Yesterday"]`

---

## What is a function?
1. **What is a function?**
   - A set of instructions bundled together to perform a specific task, like how a music button performs an action when pressed.
   
2. **Why is it needed?**
   - To avoid repeating the same code and to organize tasks.
   
3. **What is it used for?**
   - Executing specific tasks when called upon.
   
4. **What is not possible to do without it?**
   - Easily reuse and organize code in a program.

**Examples related to music:**
   - A function to play a song: 
     ```python
     def play_song(song_name):
         print(f"Playing {song_name}...")
     ```
   - Calling the function: `play_song("Imagine")`
   - A function to stop all music: 
     ```python
     def stop_music():
         print("Music stopped.")
     ```
   - Calling the function: `stop_music()`

---

## What is a function argument?
1. **What is a function argument?**
   - Information or data you give to a function, like telling which song to play.
   
2. **Why is it needed?**
   - To provide specific details or customization for a function's task.
   
3. **What is it used for?**
   - Directing a function on how to perform its task based on given information.
   
4. **What is not possible to do without it?**
   - Make functions flexible and adaptable to various situations.

**Examples related to music:**
   - A function that changes the volume: 
     ```python
     def set_volume(level):
         print(f"Volume set to {level}%")
     ```
   - Setting the volume to 70%: `set_volume(70)`
   - A function to skip to a specific time in a song: 
     ```python
     def skip_to_time(minutes, seconds):
         print(f"Skipped to {minutes}m {seconds}s.")
     ```
   - Skipping to 1 minute 30 seconds: `skip_to_time(1, 30)`

---

## What is a function return value?
1. **What is a function return value?**
   - The result or answer a function gives back after completing its task, like a music player showing the song duration.
   
2. **Why is it needed?**
   - To obtain outcomes from functions for further use or decisions.
   
3. **What is it used for?**
   - Providing results after processing or calculation.
   
4. **What is not possible to do without it?**
   - Get direct outcomes from functions to use elsewhere in the program.

**Examples related to music:**
   - A function that returns song duration: 
     ```python
     def song_duration(song_name):
         durations = {"Imagine": 3.03, "Yesterday": 2.05}
         return durations.get(song_name, "Unknown")
     ```
   - Getting the duration of "Imagine": `duration = song_duration("Imagine")`
   - A function to calculate total playlist time: 
     ```python
     def total_time(song_list):
         total = 0
         for song in song_list:
             total += song_duration(song)
         return total
     ```
   - Calculating total time for a playlist: `total = total_time(["Imagine", "Yesterday"])`

---

## What is branching?
1. **What is branching?**
   - Making decisions in the program based on conditions, like choosing which song to play based on mood.
   
2. **Why is it needed?**
   - To allow the program to take different actions depending on circumstances.
   
3. **What is it used for?**
   - Directing the program flow based on conditions or decisions.
   
4. **What is not possible to do without it?**
   - Make decisions and execute varied logic in the program.

**Examples related to music:**
   - Playing a song based on mood: 
     ```python
     if mood == "happy":
         play("Happy Song")
     else:
         play("Calm Song")
     ```
   - Adjusting volume for night time: 
     ```python
     if time == "night":
         set_volume(20)
     ```

---

## What is a loop?
1. **What is a loop?**
   - Repeating a set of instructions multiple times, like playing a song on repeat.
   
2. **Why is it needed?**
   - To perform repetitive tasks without rewriting the same code.
   
3. **What is it used for?**
   - Executing the same code multiple times based on conditions.
   
4. **What is not possible to do without it?**
   - Easily perform repetitive operations and tasks.

**Examples related to music:**
   - Playing a playlist of songs:
     ```python
     for song in playlist:
         play(song)
     ```
   - Repeating a song 5 times:
     ```python
     for i in range(5):
         play("Imagine")
     ```

---

## What is an object?
1. **What is an object?**
   - A collection of properties (like attributes) and behaviors (like methods) representing a concept, like a digital representation of a musical instrument.
   
2. **Why is it needed?**
   - To model and represent complex entities and their behaviors in the program.
   
3. **What is it used for?**
   - Encapsulating data and actions in a single entity.
   
4. **What is not possible to do without it?**
   - Create organized and structured representations of real-world entities in the program.

**Examples related to music:**
   - An object representing a musical instrument:
     ```python
     class Guitar:
         def __init__(self, brand, string_count):
             self.brand = brand
             self.string_count = string_count

         def play(self):
             print(f"Playing the {self.brand} guitar with {self.string_count} strings!")
     ```
   - Creating a guitar object and playing it:
     ```python
     my_guitar = Guitar("Fender", 6)
     my_guitar.play()
     ```

## What is a statement?
1. **What is a statement?**
   - An instruction that Python can execute, like reading a music note on a sheet.
   
2. **Why is it needed?**
   - To tell the program what action to take.
   
3. **What is it used for?**
   - Carrying out actions and making decisions in the program.
   
4. **What is not possible to do without it?**
   - Direct the flow and operations of a program.

**Examples related to music:**
   - A statement to assign a song title: `song_title = "Imagine"`
   - A statement to call a play function: `play(song_title)`
   - A statement to stop the music: `stop()`

---

## What is an expression?
1. **What is an expression?**
   - A combination of values, variables, and operators that results in a value, like calculating the total length of two songs.
   
2. **Why is it needed?**
   - To compute and derive new information.
   
3. **What is it used for?**
   - Evaluating to a value and making computations.
   
4. **What is not possible to do without it?**
   - Compute and derive values within a program.

**Examples related to music:**
   - An expression to calculate total song time: `song1_length + song2_length`
   - Checking if a song is longer than 4 minutes: `song_length > 4`
   - Calculating the average song length: `(song1_length + song2_length) / 2`

---

# music_tool

```shell
pip install pygame
cd music_tool
python music_tool.py
```