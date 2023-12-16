from tkinter import Tk, StringVar, OptionMenu

# Initialize the window
root = Tk()
root.title("Purple Drop-down List")

# Define options for the drop-down list
options = ["Option 1", "Option 2", "Option 3"]

# Create a StringVar to hold the selected option
selected_option = StringVar()
selected_option.set(options[0])  # Set the default option

# Create the drop-down list
menu = OptionMenu(root, selected_option, *options)
menu.config(bg="#E5BEEC", fg="white", font="Bold", relief="flat", bd=0,highlightthickness=0)  # Set purple background and white text
# menu.place(x=724.0, y=370.0)

# # Create a label to display the selected option (optional)
# label = Label(root, text="Selected option:", fg="white", bg="purple")

# Place the widgets on the window
menu.pack(pady=10)
# label.pack(pady=10)

# Run the main event loop
root.mainloop()



# # Define options for the drop-down list
# options = ["GScribe_0012", "GScribe_0012", "Add Devices"]

# # Create a StringVar to hold the selected option
# selected_option = StringVar()
# selected_option.set(options[0])  # Set the default option

# # Create the drop-down list
# menu = OptionMenu(window, selected_option, *options)
# menu.config(bg="#2A2F4F", fg="white", font="Bold", relief="flat", bd=0, highlightthickness=0)  # Set purple background and white text
# menu.place(x=221, y=301.0)
