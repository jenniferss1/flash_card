from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 45, "bold"))
canvas.grid(row=0, column=0, columnspan=2) 

# Buttons setup
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

window.mainloop()