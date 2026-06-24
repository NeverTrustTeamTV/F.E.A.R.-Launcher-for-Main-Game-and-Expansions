import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# DEFINE STRATEGIC GAME PATHS
GAME_LAUNCHERS = {
    "F.E.A.R. (Base Game)": r"C:\Program Files (x86)\Steam\steamapps\common\FEAR Ultimate Shooter Edition\FEAR.exe",
    "Extraction Point": r"C:\Program Files (x86)\Steam\steamapps\common\FEAR Ultimate Shooter Edition\FEARXP\FEARXP.exe",
    "Perseus Mandate": r"C:\Program Files (x86)\Steam\steamapps\common\FEAR Ultimate Shooter Edition\FEARXP2\FEARXP2.exe"
}

GAME_CONFIGS = {
    "Base Config": r"C:\Program Files (x86)\Steam\steamapps\common\FEAR Ultimate Shooter Edition\Config.exe",
    "XP1 Config": r"C:\Program Files (x86)\Steam\steamapps\common\FEAR Ultimate Shooter Edition\FEARXP\Config.exe",
    "XP2 Config": r"C:\Program Files (x86)\Steam\steamapps\common\FEAR Ultimate Shooter Edition\FEARXP2\Config.exe"
}

def run_executable(path, title):
    if os.path.exists(path):
        working_dir = os.path.dirname(path)
        try:
            subprocess.Popen([path], cwd=working_dir)
            # Only close the launcher if we are playing a game, keep open for configs
            if "Config" not in title:
                root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open:\n{e}")
    else:
        messagebox.showerror("Not Found", f"Missing file at:\n{path}")

# WINDOW SETUP
root = tk.Tk()
root.title("F.E.A.R. Master Command Launcher")
root.geometry("600x380")
root.configure(bg="#121212")

# HEADER
tk.Label(root, text="F.E.A.R. UNIFIED LAUNCHER & CONFIGS", font=("Arial", 14, "bold"), fg="#ff3333", bg="#121212").pack(pady=15)

# SECTION: LAUNCH GAMES
tk.Label(root, text="PLAY CAMPAIGNS", font=("Arial", 10, "bold"), fg="#888888", bg="#121212").pack(pady=5)
game_frame = tk.Frame(root, bg="#121212")
game_frame.pack()

for name, path in GAME_LAUNCHERS.items():
    btn = tk.Button(game_frame, text=name, font=("Arial", 10, "bold"), fg="white", bg="#222222", 
                    activebackground="#ff3333", activeforeground="white", width=18, height=2,
                    command=lambda p=path, t=name: run_executable(p, t))
    btn.pack(side=tk.LEFT, padx=10, pady=5)

# Separator Line
tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN, bg="#333333").pack(fill=tk.X, padx=30, pady=20)

# SECTION: CONFIGURATIONS
tk.Label(root, text="GAME SETTINGS & HARDWARE CONFIGS", font=("Arial", 10, "bold"), fg="#888888", bg="#121212").pack(pady=5)
config_frame = tk.Frame(root, bg="#121212")
config_frame.pack()

for name, path in GAME_CONFIGS.items():
    btn = tk.Button(config_frame, text=name, font=("Arial", 9, "bold"), fg="#cccccc", bg="#2c2c2c", 
                    activebackground="#444444", activeforeground="white", width=18, height=1,
                    command=lambda p=path, t=name: run_executable(p, t))
    btn.pack(side=tk.LEFT, padx=10, pady=5)

root.mainloop()
