import tkinter as tk
from tkinter import messagebox


class KantoGamesApp:

  def __init__(self, root):
    self.root = root
    self.root.title("KantoGames Launcher")
    self.root.geometry("500x600")
    self.root.configure(bg="#1E1E28")
    self.root.resizable(False, False)

    self.selected_game = "Tumbang Preso"
    self.selected_powerup = "Speed Burst"

    self.create_widgets()

  def create_widgets(self):
    # Title Label
    title_label = tk.Label(
        self.root,
        text="KANTO GAMES 🎮",
        font=("Arial", 22, "bold"),
        bg="#FFAA00",
        fg="white",
        padx=20,
        pady=8,
    )
    title_label.pack(pady=20)

    # Game Mode Selection Frame
    mode_frame = tk.LabelFrame(
        self.root,
        text=" SELECT GAME MODE ",
        font=("Arial", 11, "bold"),
        bg="#1E1E28",
        fg="#C8C8C8",
        bd=2,
        relief="groove",
    )
    mode_frame.pack(pady=5, padx=30, fill="both", expand=True)

    game_modes = [
        "Tumbang Preso",
        "SekyuBase",
        "Patintero",
        "Tagutaguan",
        "Sipa",
        "Luksong Baka",
    ]

    self.game_buttons = {}
    for i, game in enumerate(game_modes):
      btn = tk.Button(
          mode_frame,
          text=game,
          font=("Arial", 10, "bold"),
          bg="#323241",
          fg="white",
          activebackground="#00AAFF",
          activeforeground="white",
          relief="flat",
          command=lambda g=game: self.select_game(g),
      )
      row = i // 2
      col = i % 2
      btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
      mode_frame.rowconfigure(row, weight=1)
      mode_frame.columnconfigure(col, weight=1)
      self.game_buttons[game] = btn

    # Highlight default selected game
    self.game_buttons[self.selected_game].config(bg="#00AAFF")

    # Power-Up HUD Frame
    power_frame = tk.LabelFrame(
        self.root,
        text=" EQUIPPED POWER-UP (Click to Cycle) ",
        font=("Arial", 10, "bold"),
        bg="#1E1E28",
        fg="#969696",
        bd=2,
        relief="groove",
    )
    power_frame.pack(pady=10, padx=30, fill="x")

    self.power_btn = tk.Button(
        power_frame,
        text=f"⚡ {self.selected_powerup}",
        font=("Arial", 11, "bold"),
        bg="#8A2BE2",
        fg="white",
        activebackground="#9B30FF",
        activeforeground="white",
        relief="flat",
        command=self.cycle_powerup,
    )
    self.power_btn.pack(pady=10, padx=20, fill="x", ipady=5)

    # Play Button
    play_btn = tk.Button(
        self.root,
        text="PLAY MATCH",
        font=("Arial", 14, "bold"),
        bg="#2ECC71",
        fg="white",
        activebackground="#27AE60",
        activeforeground="white",
        relief="flat",
        command=self.start_match,
    )
    play_btn.pack(pady=20, padx=50, fill="x", ipady=8)

  def select_game(self, game_name):
    self.selected_game = game_name
    for name, btn in self.game_buttons.items():
      if name == game_name:
        btn.config(bg="#00AAFF")
      else:
        btn.config(bg="#323241")

  def cycle_powerup(self):
    powerups = [
        "Speed Burst",
        "Stealth Camouflage",
        "Forcefield Barrier",
        "Dash Dodge",
        "Low-Gravity Kick",
    ]
    current_idx = powerups.index(self.selected_powerup)
    next_idx = (current_idx + 1) % len(powerups)
    self.selected_powerup = powerups[next_idx]
    self.power_btn.config(text=f"⚡ {self.selected_powerup}")

  def start_match(self):
    messagebox.showinfo(
        "Match Queued",
        f"Entering match...\nMode: {self.selected_game}\nPower-Up:"
        f" {self.selected_powerup}",
    )


if __name__ == "__main__":
  root = tk.Tk()
  app = KantoGamesApp(root)
  root.mainloop()