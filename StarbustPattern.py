import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("dark_background")

# Zaman parametresi
t = np.linspace(0, 2*np.pi, 1500)

# Taban çiçek
base_x = np.cos(t) * (1 + 0.6 * np.cos(20 * t))
base_y = np.sin(t) * (1 + 0.6 * np.cos(20 * t))

fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# İlk görüntü
scatter = ax.scatter(base_x, base_y, c=t, cmap="spring", s=2)

def update(frame):
    # --- 1) Açılıp Kapanma (bloom) ---
    bloom = 1 + 0.25 * np.sin(frame * 0.05)
    x = base_x * bloom
    y = base_y * bloom

    # --- 2) Dönme ---
    angle = frame * 0.03
    rot_x = x * np.cos(angle) - y * np.sin(angle)
    rot_y = x * np.sin(angle) + y * np.cos(angle)

    # --- 3) Neon renk akışı ---
    c = (t + frame * 0.07) % (2*np.pi)  # hızlı renk kayması

    # --- 4) NEON PARLAMA EFEKTİ ---
    # Nokta boyutu sinüs dalgasıyla parlıyor
    glow = 2 + 1.5 * (1 + np.sin(frame * 0.15))

    scatter.set_offsets(np.column_stack([rot_x, rot_y]))
    scatter.set_array(c)
    scatter.set_sizes(np.full_like(t, glow))  # neon dalgalanma

    return scatter,

ani = FuncAnimation(fig, update, frames=4000, interval=10, blit=True)
plt.show()
