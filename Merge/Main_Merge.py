#머지 용
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
