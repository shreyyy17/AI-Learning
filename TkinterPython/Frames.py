import tkinter as tk
from tkinter import ttk

# def greeting():
#     print(f'Hello, {user_name.get()}!')



root = tk.Tk()

main = ttk.Frame(root)
main.pack(side='left',fill='both',expand=True)

tk.Label(main,text='Label Top',bg='red').pack(side='top',expand=True,fill='both')
tk.Label(main,text='Label Top',bg='red').pack(side='top',expand=True,fill='both')
tk.Label(root,text='Label Left',bg='green').pack(side='left',expand=True,fill='both')
root.title('Helowww')

# user_name = tk.StringVar()
#
# name_label= ttk.Label(root,text='Name :')
# name_label.pack(side='left',padx=(0,10))
# name_entry =ttk.Entry(root,width=15,textvariable=user_name)
# name_entry.pack(side='left')
# name_entry.focus()
#
# greet_button = ttk.Button(root, text='Greet', command=greeting)
# greet_button.pack(side='left',fill='x',expand=True)
#
# quit_button = ttk.Button(root, text='Quit', command=root.destroy)
# quit_button.pack(side='right',fill='x',expand=True)
root.mainloop()
