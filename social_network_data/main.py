import os
import tkinter as tk
from tkinter import Canvas, Scrollbar, messagebox
import json
import datetime
import webbrowser
import fbReader
import insReader

SOCIAL_NETWORKS = ["facebook", "instagram", "snapchat", "tiktok.json", "twitter"]


def empty_function(inner_folders_window, folder_path, social_network):
    def display(file_path):
        if file_path[-31:] == "your_off-facebook_activity.json":
            with open(file_path, 'r') as file:
                data = json.load(file)
            app_list = []
            for i in data["off_facebook_activity_v2"]:
                app_list.append(i["name"])

            new_window = tk.Toplevel()
            new_window.title("Off-Facebook activity")
            label = tk.Label(new_window, text="Your activity off of Facebook that is still tracked\nThis is a list of apps that Facebook tracks even when you are not on it. If you want yo see the type of action they tracked and the date click on the app which you want to see this for.")
            label.pack()

            for app in app_list:
                button = tk.Button(new_window, text=app, command=lambda name=app: chosen_app(name))
                button.pack()

            def chosen_app(name):
                text = "Your activity off of Facebook that is still tracked\n\n"
                for i in data["off_facebook_activity_v2"]:
                    if i["name"] == name:
                        for x in i["events"]:
                            text += "\nType of event: " + x["type"]
                            dt = datetime.datetime.fromtimestamp(x["timestamp"])
                            text += "\nTime of log: " + str(dt)
                        popup = tk.Toplevel()
                        popup.title("Off-Facebook activity")

                        # Add a text widget to display the JSON data
                        text_widget = tk.Text(popup, wrap=tk.WORD, padx=10, pady=10)
                        text_widget.insert(tk.END, text)
                        text_widget.config(state=tk.DISABLED)
                        text_widget.pack(expand=True, fill=tk.BOTH)

                        # Add a close button to close the pop-up window
                        close_button = tk.Button(popup, text="Close", command=popup.destroy)
                        close_button.pack(pady=10)

                        # Run the pop-up window's main loop
                        popup.mainloop()


        else:
            if social_network == "facebook":
                text = fbReader.get_text(file_path)
            elif social_network == "instagram":
                text = insReader.get_text(file_path)


            # Create a pop-up window to display the contents
            popup = tk.Toplevel()
            popup.title(text[0])

            # Add a text widget to display the JSON data
            text_widget = tk.Text(popup, wrap=tk.WORD, padx=10, pady=10)
            text_widget.insert(tk.END, str(text[1]))
            text_widget.config(state=tk.DISABLED)
            text_widget.pack(expand=True, fill=tk.BOTH)

            # Add a close button to close the pop-up window
            close_button = tk.Button(popup, text="Close", command=popup.destroy)
            close_button.pack(pady=10)

            # Run the pop-up window's main loop
            popup.mainloop()

    def back_to_inner_folders():
        inner_folders_window.deiconify()
        file_list_window.destroy()
        
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if len(files) == 1:
        path = folder_path + "/" + files[0]
        display(path)
    else:
        inner_folders_window.withdraw()
        file_list_window = tk.Tk()
        file_list_window.configure(bg="#90CAF9")
        file_list_window.title(folder_path)

        screen_width = file_list_window.winfo_screenwidth()
        screen_height = file_list_window.winfo_screenheight()
        file_list_window.geometry(f"{(2 * screen_width)//3}x{screen_height}")

        for index, file in enumerate(files):
            path = folder_path + "/" + file
            button = tk.Button(file_list_window, text=file, command=lambda p=path: display(p))
            button.grid(row=index // 3, column=index % 3, padx=20, pady=20)

        back_button = tk.Button(file_list_window, text="Back", bg="red", command=back_to_inner_folders)
        back_button.grid(row=100, column=0, columnspan=3, padx=20, pady=20)

        file_list_window.protocol("WM_DELETE_WINDOW", back_to_inner_folders)
        file_list_window.mainloop()

def display_inner_folders(main_root, folder_name):
    def callback():
        main_root.deiconify()
        inner_folders_window.destroy()

    main_root.withdraw()
    inner_folders_window = tk.Tk()
    inner_folders_window.configure(bg="#90CAF9")
    inner_folders_window.title(folder_name)

    screen_width = inner_folders_window.winfo_screenwidth()
    screen_height = inner_folders_window.winfo_screenheight()
    inner_folders_window.geometry(f"{(2 * screen_width)//3}x{screen_height}")

    inner_folders = os.listdir(os.path.join("social_networks", folder_name))

    canvas = Canvas(inner_folders_window, bg="#90CAF9")
    canvas.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(inner_folders_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    buttons_frame = tk.Frame(canvas, bg="#90CAF9")
    canvas.create_window((0, 0), window=buttons_frame, anchor=tk.NW)

    num_columns = 3
    column_frames = [tk.Frame(buttons_frame, bg="#90CAF9") for _ in range(num_columns)]
    for i, frame in enumerate(column_frames):
        frame.pack(side=tk.LEFT, padx=10)

    if inner_folders:
        for index, inner_folder in enumerate(inner_folders):
            path = "social_networks/" + folder_name + "/" + inner_folders[index]
            no_data_file_path = os.path.join(path, "no-data.txt")
            if (not os.path.isfile(no_data_file_path)) and (inner_folder != ".DS_Store"):
                button = tk.Button(column_frames[index % num_columns], text=inner_folder, command=lambda p=path: empty_function(inner_folders_window, p, folder_name))
                button.pack(pady=20)

    else:
        tk.Label(buttons_frame, text=f"No folders found in {folder_name}.", bg="#90CAF9").pack(pady=20)

    back_button = tk.Button(inner_folders_window, text="Back", bg="red", command=callback)
    back_button.pack(padx=20, pady=20)

    inner_folders_window.protocol("WM_DELETE_WINDOW", callback)
    inner_folders_window.mainloop()


def snapchat():
    file_path = os.path.abspath("social_networks/snapchat/index.html")
    url = "file://" + file_path
    webbrowser.open(url)

def tiktok(main_root):
    def callback():
        main_root.deiconify()
        inner_folders_window.destroy()
   
    def dataTik(x):
        text = x + "\n"
        for values in data["Activity"][x]:
            if data["Activity"][x][values] is not None:
                for subkey in data["Activity"][x][values]:
                    for subkeykey, subkeyvalues in subkey.items():
                        text += "\n" + subkeykey + ": " + subkeyvalues
                    text += "\n"
        popup = tk.Toplevel()
        popup.title(x)

        # Add a text widget to display the JSON data
        text_widget = tk.Text(popup, wrap=tk.WORD, padx=10, pady=10)
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH)

        # Add a close button to close the pop-up window
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

        # Run the pop-up window's main loop
        popup.mainloop()
    main_root.withdraw()
    inner_folders_window = tk.Tk()
    inner_folders_window.configure(bg="#90CAF9")
    inner_folders_window.title("TikTok")

    screen_width = inner_folders_window.winfo_screenwidth()
    screen_height = inner_folders_window.winfo_screenheight()
    inner_folders_window.geometry(f"{(2 * screen_width)//3}x{screen_height}")

    file_path = os.path.abspath("social_networks/tiktok.json")
    keys = []

    with open(file_path, 'r') as file:
        data = json.load(file)
    for key in data["Activity"]:
        keys.append(key)
    canvas = Canvas(inner_folders_window, bg="#90CAF9")
    canvas.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(inner_folders_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    buttons_frame = tk.Frame(canvas, bg="#90CAF9")
    canvas.create_window((0, 0), window=buttons_frame, anchor=tk.NW)

    num_columns = 3
    column_frames = [tk.Frame(buttons_frame, bg="#90CAF9") for _ in range(num_columns)]
    for i, frame in enumerate(column_frames):
        frame.pack(side=tk.LEFT, padx=10)

    if keys:
        for index, key in enumerate(keys):
            button = tk.Button(column_frames[index % num_columns], text=key, command=lambda k=key: dataTik(k))
            button.pack(pady=20)

    else:
        tk.Label(buttons_frame, text=f"No folders found in {folder_name}.", bg="#90CAF9").pack(pady=20)

    back_button = tk.Button(inner_folders_window, text="Back", bg="red", command=callback)
    back_button.pack(padx=20, pady=20)

    inner_folders_window.protocol("WM_DELETE_WINDOW", callback)
    inner_folders_window.mainloop()


def main():
    root = tk.Tk()
    root.configure(bg="#90CAF9")
    root.title("Social Networks")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{(2 * screen_width)//3}x{screen_height}")

    social_networks_path = "social_networks"
    if not os.path.exists(social_networks_path):
        os.makedirs(social_networks_path)

    found_networks = []
    for network in os.listdir(social_networks_path):
        if network.lower() in SOCIAL_NETWORKS:
            found_networks.append(network)

    if found_networks:
        cols = 3
        for index, network in enumerate(found_networks):
            row, col = divmod(index, cols)
            if network == "snapchat":
                button = tk.Button(root, text=network, command=lambda: snapchat())
                button.grid(row=row, column=col, padx=20, pady=20)
            elif network == "tiktok.json":
                button = tk.Button(root, text=network[:6], command=lambda: tiktok(root))
                button.grid(row=row, column=col, padx=20, pady=20)
            else:
                button = tk.Button(root, text=network, command=lambda n=network: display_inner_folders(root, n))
                button.grid(row=row, column=col, padx=20, pady=20)
    else:
        tk.Label(root, text="No social network folders found.", bg="#90CAF9").pack(pady=20)

    root.mainloop()    

if __name__ == "__main__":
    main()
