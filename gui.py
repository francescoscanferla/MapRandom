from tkinter import messagebox

title = "Map Random"


def show_info(message):
    messagebox.showinfo(title, message)


def show_result(data):
    message = f"  Default maps: {data['default']}\n" \
              f"  Custom maps: {data['custom']}\n" \
              f"  Total maps: {data['total']}\n\n" \
              f"Maps config successful generate" \

    messagebox.showinfo(title, message)
