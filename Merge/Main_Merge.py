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

def show_character_info():
    character = create_character()
    info_label.config(text=f"{character['name']} (Lv.{character['level']})\n직업: {character['job']}\n체력: {character['hp']}\n마나: {character['mp']}")

def explore():
    monster_list = ["고블린", "오크", "트롤", "드래곤"]
    monster = random.choice(monster_list)
    character = create_character()
    if character["hp"] > 0:
        battle_text = f"{character['name']}은(는) {monster}를 만났다!\n"
        battle_text += f"{character['name']}의 체력: {character['hp']}\n"
        battle_text += f"{monster}의 체력: {random.randint(50, 100)}\n"
        info_label.config(text=battle_text)
    else:
        info_label.config(text="당신은 죽었습니다...")



#머지 용
name_label = tk.Label(root, text="캐릭터 이름:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

info_label = tk.Label(root, text="캐릭터 정보가 여기에 표시됩니다.")
info_label.grid(row=1, column=0, columnspan=2)

character_button = tk.Button(root, text="캐릭터 정보", command=show_character_info)
character_button.grid(row=2, column=0)

explore_button = tk.Button(root, text="탐험", command=explore)
explore_button.grid(row=2, column=1)

root.mainloop()
# 마지막문단입니다.