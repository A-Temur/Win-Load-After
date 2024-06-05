import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x800")


app.grid_columnconfigure(0, weight=1)

mframe = customtkinter.CTkFrame(app, border_color=("gray10", "#DCE4EE"), border_width=1)
mframe.grid(row=0, column=0)
mframe.grid_columnconfigure(0, weight=1)

scrollable_frame = customtkinter.CTkScrollableFrame(mframe, label_text="Current Load Order")
scrollable_frame.grid(row=0, column=0)
scrollable_frame.grid_columnconfigure(0, weight=1)
entry_2 = customtkinter.CTkLabel(master=scrollable_frame, text="ProcessA")
entry_2.grid(column=0, row=0)
entry_2 = customtkinter.CTkLabel(master=scrollable_frame, text="ProcessA Descr")
entry_2.grid(column=1, row=0)
entry_2 = customtkinter.CTkLabel(master=scrollable_frame, text="ProcessA")
entry_2.grid(column=0, row=1)
entry_2 = customtkinter.CTkLabel(master=scrollable_frame, text="ProcessA Descr")
entry_2.grid(column=1, row=1)

butframe = customtkinter.CTkFrame(mframe)
butframe.grid(row=0, column=1)
butframe.grid_columnconfigure(0, weight=1)
button1 = customtkinter.CTkButton(butframe, text="Move UP", command=button_callback)
button1.grid(row=0, column=0)
button2 = customtkinter.CTkButton(butframe, text="Move Down", command=button_callback)
button2.grid(row=1, column=0)


button3 = customtkinter.CTkButton(app, text="Save", command=button_callback)
button3.grid(row=1, column=0)


# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.grid(row=1, column=0, sticky='w')
# checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
# checkbox_1.grid(row=2, column=0)
# checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
# checkbox_2.grid(row=2, column=1)

app.mainloop()
#
#
# def slider_callback(value):
#     progressbar_1.set(value)
#
#
# frame_1 = customtkinter.CTkFrame(master=app)
# frame_1.pack(expand=True)
#
# label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
# label_1.pack(pady=10, padx=10)
#
# progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
# progressbar_1.pack(pady=10, padx=10)
#
# button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
# button_1.pack(pady=10, padx=10)
#
# slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
# slider_1.pack(pady=10, padx=10)
# slider_1.set(0.5)
#
# entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Search for Process (name)")
# entry_1.pack(pady=10, padx=10)
#
# listprocess = customtkinter.CTkScrollableFrame(app)
# entry_2 = customtkinter.CTkEntry(master=listprocess, placeholder_text="Search for Process (name)")
# entry_3 = customtkinter.CTkEntry(master=listprocess, placeholder_text="Search for Process (name)")
#
# optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# optionmenu_1.pack(pady=10, padx=10)
# optionmenu_1.set("CTkOptionMenu")
#
# combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# combobox_1.pack()
# combobox_1.set("CTkComboBox")
#
# checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
# checkbox_1.pack(pady=10, padx=10)
#
# radiobutton_var = customtkinter.IntVar(value=1)
#
# radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
# radiobutton_1.pack(pady=10, padx=10)
#
# radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
# radiobutton_2.pack()
#
# switch_1 = customtkinter.CTkSwitch(master=frame_1)
# switch_1.pack(pady=10, padx=10)
#
# text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
# text_1.pack()
# text_1.insert("0.0", "CTkTextbox\n\n\n\n")
#
# segmented_button_1 = customtkinter.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
# segmented_button_1.pack(pady=10, padx=10)
#
# tabview_1 = customtkinter.CTkTabview(master=frame_1, width=300)
# tabview_1.pack(pady=10, padx=10)
# tabview_1.add("CTkTabview")
# tabview_1.add("Tab 2")


app.mainloop()