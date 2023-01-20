import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")
root.title("Grade Calculator")
root.iconbitmap("gradeclacICO.ico")

arr = {"Deutsch": 0,
       "SytI": 0,
       "SytE": 0,
       "SEW": 0,
       "NAWI": 0,
       "Sport": 0,
       "Werkstäte": 0,
       "ITSI": 0,
       "Englisch": 0,
       "Mathe": 0,
       "Medientechnik": 0,
       "Geografie": 0,
       "NWTK": 0,
       "Religion": 0,
       }
amount = 0
total = float(0)


def userin():
    global label, amount, total
    grade = float(entry.get())
    subject = label.cget("text")
    if grade == "0" or grade == 0 or grade == '':
        pass
    else:
        while grade > 5 or grade < 0:
            label1.configure(text="Not valid")
            grade = entry.get()

        arr[subject] = grade
        amount += 1
        total += grade
        del arr[subject]
        if arr:
            label.configure(text=next(iter(arr)))
        else:
            label.configure(text="Finished")
            button.configure(state="disabled")
            entry.configure(state="disabled")
        label1.configure(text=f">>> {round((total / amount) * 100) / 100} <<<")
        entry.delete(0, 'end')


frame = ctk.CTkFrame(master=root, width=500, height=350)
frame.pack(pady=12, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text=next(iter(arr)), font=("Arial", 25))
label.pack(pady=15, padx=10)

entry = ctk.CTkEntry(master=frame, placeholder_text="Grade")
entry.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Enter", command=userin)
button.pack(pady=12, padx=10)

label1 = ctk.CTkLabel(master=frame, text="0.00", font=("Arial", 25))
label1.pack(pady=60, padx=10)

root.mainloop()
