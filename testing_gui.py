import tkinter as tk
window = tk.Tk()
# greeting = tk.Label(text="Hello, Tkinter")
# # greeting.pack()

# # clickable buttons
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )

# for input from user
label = tk.Label(text="Name")
entry = tk.Entry()
# we pack the stuff to make it visible
label.pack()
entry.pack()
# To get the input to program
name = entry.get()
print(name)
window.mainloop()