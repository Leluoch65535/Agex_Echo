import tkinter as tk
from tkinter import ttk


class DisasterDashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disaster Response Dashboard")
        self.root.geometry("1280x760")
        self.root.configure(bg="#0b1220")
        self.root.minsize(1100, 700)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#0b1220")
        self.style.configure("Header.TLabel", background="#0b1220", foreground="#eaf3ff", font=("Segoe UI", 28, "bold"))
        self.style.configure("Sub.TLabel", background="#0b1220", foreground="#9bb5d1", font=("Segoe UI", 11))
        self.style.configure("Card.TFrame", background="#101b2e")
        self.style.configure("Stat.TLabel", background="#101b2e", foreground="#dfeeff", font=("Segoe UI", 16, "bold"))
        self.style.configure("Muted.TLabel", background="#101b2e", foreground="#89a6c6", font=("Segoe UI", 9))
        self.style.configure("Accent.TLabel", background="#101b2e", foreground="#7ce6d4", font=("Segoe UI", 10, "bold"))
        self.style.configure("Panel.TFrame", background="#111d32")
        self.style.configure("Section.TLabel", background="#111d32", foreground="#eff7ff", font=("Segoe UI", 16, "bold"))
        self.style.configure("Body.TLabel", background="#111d32", foreground="#d6e8ff", font=("Segoe UI", 11))

        self.build_ui()

    def build_ui(self):
        topbar = tk.Frame(self.root, bg="#0f1729", height=80)
        topbar.pack(fill="x", padx=24, pady=(18, 14))

        title = tk.Label(topbar, text="Agex Echo", bg="#0f1729", fg="#dcecff", font=("Segoe UI", 22, "bold"))
        title.pack(anchor="w", padx=24, pady=(18, 0))

        live = tk.Label(topbar, text="LIVE OPERATIONS", bg="#0f1729", fg="#7ce6d4", font=("Segoe UI", 10, "bold"))
        live.place(x=1060, y=18)

        status_dot = tk.Label(topbar, text="●", bg="#0f1729", fg="#39d98a", font=("Segoe UI", 12, "bold"))
        status_dot.place(x=1180, y=18)

        status_text = tk.Label(topbar, text="System stable", bg="#0f1729", fg="#d9f8ee", font=("Segoe UI", 10))
        status_text.place(x=1198, y=16)

        content = tk.Frame(self.root, bg="#0b1220")
        content.pack(fill="both", expand=True, padx=24, pady=(0, 18))

        stats_row = tk.Frame(content, bg="#0b1220")
        stats_row.pack(fill="x", pady=(0, 16))

        stats = [
            ("Active Incidents", "14", "+2 since 08:00", "#ffb454"),
            ("Teams Deployed", "42", "18 on route", "#5db8ff"),
            ("Critical Alerts", "07", "3 life-threatening", "#ff6b6b"),
            ("Shelter Capacity", "68%", "1,240 occupied", "#58d68d"),
        ]

        for i, (label, value, detail, accent) in enumerate(stats):
            card = tk.Frame(stats_row, bg="#101b2e", width=260, height=115, highlightthickness=1, highlightbackground="#1d2d44")
            card.grid_rowconfigure(0, weight=1)
            card.grid_columnconfigure(0, weight=1)
            card.grid_propagate(False)
            card.grid(row=0, column=i, padx=(0, 18) if i < 3 else 0, sticky="nsew")
            stats_row.grid_columnconfigure(i, weight=1)

            accent_bar = tk.Frame(card, bg=accent, height=4)
            accent_bar.pack(fill="x")

            label_l = tk.Label(card, text=label, bg="#101b2e", fg="#9db6d1", font=("Segoe UI", 10))
            label_l.pack(anchor="w", padx=16, pady=(14, 0))

            val_l = tk.Label(card, text=value, bg="#101b2e", fg="#edf7ff", font=("Segoe UI", 26, "bold"))
            val_l.pack(anchor="w", padx=16, pady=(8, 0))

            det_l = tk.Label(card, text=detail, bg="#101b2e", fg=accent, font=("Segoe UI", 9, "bold"))
            det_l.pack(anchor="w", padx=16, pady=(4, 0))

        main = tk.Frame(content, bg="#0b1220")
        main.pack(fill="both", expand=True)

        left = tk.Frame(main, bg="#0b1220", width=760)
        left.pack(side="left", fill="y", padx=(0, 16))
        left.pack_propagate(False)

        right = tk.Frame(main, bg="#0b1220", width=420)
        right.pack(side="right", fill="y")
        right.pack_propagate(False)

        map_panel = tk.Frame(left, bg="#111d32", height=430, highlightthickness=1, highlightbackground="#1c2d45")
        map_panel.pack(fill="x")
        map_panel.pack_propagate(False)

        map_head = tk.Label(map_panel, text="Regional Response View", bg="#111d32", fg="#ebf3ff", font=("Segoe UI", 16, "bold"))
        map_head.place(x=18, y=14)

        map_label = tk.Label(map_panel, text="North Sector • South Basin • Coastal District", bg="#111d32", fg="#9bb5d1", font=("Segoe UI", 10))
        map_label.place(x=18, y=42)

        canvas = tk.Canvas(map_panel, width=700, height=330, bg="#101b2e", highlightthickness=0)
        canvas.place(x=18, y=70)

        # Background terrain blocks
        terrain_colors = ["#152742", "#1d2f4d", "#12253d", "#18314c", "#13273d"]
        for i, color in enumerate(terrain_colors):
            x0 = 25 + (i % 3) * 210
            y0 = 20 + (i // 3) * 120
            canvas.create_rectangle(x0, y0, x0 + 150, y0 + 90, fill=color, outline="")

        # Map routes
        canvas.create_line(80, 110, 220, 140, 320, 90, 520, 150, width=4, fill="#4ad3c6", smooth=True)
        canvas.create_line(260, 240, 430, 210, 560, 270, width=4, fill="#59a9ff", smooth=True)
        canvas.create_line(170, 210, 200, 300, 370, 280, 510, 330, width=4, fill="#f6b267", dash=(8, 5))

        # Incident markers
        markers = [
            (90, 105, "Flood Zone", "#ffb454"),
            (250, 135, "Bridge Blocked", "#ff6b6b"),
            (430, 190, "Medical Aid", "#58d68d"),
            (630, 260, "Evac Route", "#5db8ff"),
        ]

        for x, y, label, color in markers:
            canvas.create_oval(x - 12, y - 12, x + 12, y + 12, fill=color, outline="")
            canvas.create_text(x + 18, y - 14, text=label, fill="#dfeeff", font=("Segoe UI", 9, "bold"))

        bottom = tk.Frame(left, bg="#0b1220", height=210)
        bottom.pack(fill="x", pady=(16, 0))

        timeline = tk.Frame(bottom, bg="#111d32", highlightthickness=1, highlightbackground="#1c2d45")
        timeline.pack(fill="both")
        timeline.pack_propagate(False)

        tk.Label(timeline, text="Response Timeline", bg="#111d32", fg="#ebf3ff", font=("Segoe UI", 16, "bold")).place(x=18, y=12)

        events = [
            ("08:20", "Helicopter team dispatched to North Ridge"),
            ("09:15", "Emergency shelter opened in Harbor District"),
            ("10:40", "Power repair crew restoring grid in East Ward"),
            ("11:30", "Medical convoy reached remote village"),
        ]

        for idx, (time, text) in enumerate(events):
            y = 52 + idx * 38
            tk.Label(timeline, text=time, bg="#111d32", fg="#7ce6d4", font=("Segoe UI", 10, "bold")).place(x=18, y=y)
            tk.Label(timeline, text=text, bg="#111d32", fg="#dfeeff", font=("Segoe UI", 10)).place(x=110, y=y)
            if idx < len(events) - 1:
                tk.Label(timeline, text="─", bg="#111d32", fg="#3a4f6d", font=("Segoe UI", 12)).place(x=82, y=y+14)

        priority_panel = tk.Frame(right, bg="#111d32", height=250, highlightthickness=1, highlightbackground="#1c2d45")
        priority_panel.pack(fill="x")
        priority_panel.pack_propagate(False)

        tk.Label(priority_panel, text="Priority Incidents", bg="#111d32", fg="#ebf3ff", font=("Segoe UI", 16, "bold")).place(x=18, y=14)

        incidents = [
            ("Critical", "Flooding at South Crossing", "2 min ago"),
            ("High", "Electrical outage in Harbor", "8 min ago"),
            ("Medium", "Road closure near East Loop", "12 min ago"),
        ]

        for idx, (level, title, age) in enumerate(incidents):
            y = 58 + idx * 52
            color = {"Critical": "#ff6b6b", "High": "#ffb454", "Medium": "#5db8ff"}[level]
            tk.Label(priority_panel, text=level, bg=color, fg="#ffffff", font=("Segoe UI", 8, "bold"), padx=8, pady=4).place(x=18, y=y)
            tk.Label(priority_panel, text=title, bg="#111d32", fg="#e9f4ff", font=("Segoe UI", 11, "bold")).place(x=120, y=y)
            tk.Label(priority_panel, text=age, bg="#111d32", fg="#8ea6c1", font=("Segoe UI", 9)).place(x=120, y=y + 20)

        resource_panel = tk.Frame(right, bg="#111d32", height=280, highlightthickness=1, highlightbackground="#1c2d45")
        resource_panel.pack(fill="x", pady=(16, 0))
        resource_panel.pack_propagate(False)

        tk.Label(resource_panel, text="Resource Status", bg="#111d32", fg="#ebf3ff", font=("Segoe UI", 16, "bold")).place(x=18, y=14)

        resources = [
            ("Medical Teams", "8 available", "#58d68d"),
            ("Fire Units", "5 on standby", "#ffb454"),
            ("Water Supply", "3 trucks active", "#5db8ff"),
            ("Shelters", "12 open", "#7ce6d4"),
        ]

        for idx, (name, status, color) in enumerate(resources):
            y = 58 + idx * 48
            tk.Label(resource_panel, text=name, bg="#111d32", fg="#eaf3ff", font=("Segoe UI", 11)).place(x=18, y=y)
            tk.Label(resource_panel, text=status, bg="#111d32", fg="#a7bed9", font=("Segoe UI", 9)).place(x=200, y=y)
            tk.Label(resource_panel, text="●", bg="#111d32", fg=color, font=("Segoe UI", 18)).place(x=350, y=y-2)

        footer = tk.Frame(content, bg="#0b1220", height=34)
        footer.pack(fill="x", pady=(12, 0))
        footer.pack_propagate(False)

        tk.Label(footer, text="Updated 11:42 AM • 06 reporting zones • 3 ongoing evacuations", bg="#0b1220", fg="#8faac1", font=("Segoe UI", 10)).pack(anchor="w")


def main():
    root = tk.Tk()
    DisasterDashboardApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
