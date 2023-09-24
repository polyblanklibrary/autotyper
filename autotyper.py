import time
import random
import pyautogui

time.sleep(5)

def autotyper(text: str):
  # Split the text into sentences
  sentences = text.split(".")
  for sentence in sentences:
    # Type out the sentence character by character
    for char in sentence:
      # Type the character and wait a random amount of time
      pyautogui.typewrite(char)
      time.sleep(random.uniform(0, 0.1))
    # Add a period after the sentence and wait a random amount of time
    pyautogui.typewrite(".")
    time.sleep(random.uniform(4, 13))

# Example usage
autotyper("icture this: it’s a sunny afternoon in my rural, small-town neighborhood in 2011. I was only four years old. I was a curious four-year-old, as many of us are, and on this particular day, my family decided to take a day trip down to one of my family friend’s house who had with a rather nasty dachshund named Max.")
#autotyper("")



