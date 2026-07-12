from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties

USERNAME = "CarrotzCode"

font = FontProperties(family="DejaVu Sans", weight="bold")

text = TextPath(
    (0, 0),
    USERNAME,
    size=100,
    prop=font
)

vertices = text.vertices
codes = text.codes

commands = []

for (x, y), code in zip(vertices, codes):
    x = x + 20
    y = 130 - y

    if code == 1:
        commands.append(f"M{x:.2f},{y:.2f}")
    elif code == 2:
        commands.append(f"L{x:.2f},{y:.2f}")
    elif code == 3:
        commands.append(f"Q{x:.2f},{y:.2f}")
    elif code == 4:
        commands.append(f"L{x:.2f},{y:.2f}")
    elif code == 79:
        commands.append("Z")

path = " ".join(commands)

svg = f"""
<svg xmlns="http://www.w3.org/2000/svg"
     width="900"
     height="180"
     viewBox="0 0 900 180">

  <rect width="100%" height="100%" fill="#0d1117"/>

  <path
    id="username"
    d="{path}"
    fill="none"
    stroke="#39d353"
    stroke-width="2"
    opacity="0.45"
  />

  <text font-size="30">
    🥕
    <animateMotion
      dur="20s"
      repeatCount="indefinite"
      rotate="auto">
      <mpath href="#username"/>
    </animateMotion>
  </text>

</svg>
"""

with open("output/carrot.svg", "w", encoding="utf-8") as file:
    file.write(svg)

print("🥕 CarrotzCode animation generated!")
