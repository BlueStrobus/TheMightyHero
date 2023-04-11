#머지 용
import tkinter as tk
import random

root = tk.Tk()
root.title("간단한 RPG 게임")

def create_character():
    jobs = ["전사", "마법사", "궁수", "도적"]
    character = {}
    character["name"] = name_entry.get()
    character["job"] = random.choice(jobs)
    character["level"] = random.randint(1, 10) 
    character["hp"] = random.randint(50, 100) * character["level"]
    character["mp"] = random.randint(30, 50) * character["level"]
    return character
