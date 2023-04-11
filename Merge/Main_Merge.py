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