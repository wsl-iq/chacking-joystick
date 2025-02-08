import pygame
import time
import os; os.system('cls' if os.name == 'nt' else 'clear')

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Not = "\033[91;1m" + 'Not' + "\033[97;1m"

print(rf'''{G}

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{R}⣿⣷⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{R}⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀{B}⣀⣤⠀{R}⣿⣿⣿⣿⡇⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀{G}⢀⣠⣤⣶⣾⣿⣿⡿⠀{R}⣿⣿⣿⣿⡇⠀{G}⢰⣶⣿⣿⣿⠿⠿⢿⣶⣦⣤⡀
{Y}⢰⣿⣿⣿⡿⠛⠉⢀⣀⠀{R}⣿⣿⣿⣿⡇{Y}⠀⠘⠋⠉⠀⣀⣠⣴⣾⣿⣿⣿⠇
⠈⠻⠿⣿⣿⣿⣿⣿⠿⠀{R}⣿⣿⣿⣿⡇⠀{Y}⢠⣶⣾⣿⣿⡿⠿⠟⠋⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{R}⠙⠛⠿⢿⡇⠀{Y}⠸⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀
{W}''')

def slowprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)

slowprint(f"{sign} {B}Developed by: {R}Mohammed Al-Baqer {B}for checking joystick {Y}[{G}Play Station{Y}] {B}Controller{W}\n")

pygame.init()

pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print(f"{please} No joystick connected!{W}")
else:
    print((sign) + " Number of joysticks connected: " + "\033[92;1m" + f"{joystick_count}" + "\033[97;1m")

joystick = pygame.joystick.Joystick(0)
joystick.init()
 
print(f"{sign} Joystick name: {G}{joystick.get_name()}" + (W))

print(f'''{W}+---------------------------------------------------+      
| {B}View chacking joysticks Controller {Y}[{G}Play Station{Y}]{W} |
+---------------------------------------------------+''')
button_names = {
    0: "\033[90;1m" + 'Button ' + "\033[94;1m" + "✖" + "\033[97;1m",
    1: "\033[90;1m" + 'Button ' + "\033[91;1m" + "〇" + "\033[97;1m",
    2: "\033[90;1m" + 'Button ' + "\033[95;1m" + "☐" + "\033[97;1m",
    3: "\033[90;1m" + 'Button ' + "\033[92;1m" + "🛆" + "\033[97;1m",
    4: "Button Left (L1)",
    5: "Button Right (R1)",
    6: "SELECT",
    7: "Start",
    8: "\033[90;1m" + "Right Click " + "\033[97;1m" + "(L3)",
    9: "\033[90;1m" + "Left Click " + "\033[97;1m" + "(R3)",
    10: "Xbox",
    11: Not,
    12: Not
}

axis_names = {
    0: "Left X",
    1: "Left Y",
    2: "Right X",
    3: "Right Y",
    4: "Button Left (L2)",
    5: "Button Right (R2)"
}

hat_names = {
    (1, 0): "\033[90;1m" + "Button D-Pad " + "\033[97;1m" + "Right",
    (-1, 0): "\033[90;1m" + "Button D-Pad " + "\033[97;1m" + "Left",
    (0, 1): "\033[90;1m" + "Button D-Pad " + "\033[97;1m" + "Up",
    (0, -1): "\033[90;1m" + "Button D-Pad " + "\033[97;1m" + "Down",
    (0, 0): "\033[90;1m" + "Button D-Pad " + "\033[97;1m" + "\033[91;1m" + "Centered" + "\033[97;1m"
}

previous_button_states = [0] * joystick.get_numbuttons()
previous_axis_states = [0.0] * joystick.get_numaxes()
previous_hat_states = [(0, 0)] * joystick.get_numhats()

def display_inputs():
    global previous_button_states, previous_axis_states, previous_hat_states
    pygame.event.pump()

    for i in range(joystick.get_numbuttons()):
        button = joystick.get_button(i)
        if button != previous_button_states[i]:
            button_name = button_names.get(i, f"Button {i}")
            if button:
                print(f"{button_name}")
            previous_button_states[i] = button

    for i in range(joystick.get_numaxes()):
        axis = joystick.get_axis(i)
        if abs(axis - previous_axis_states[i]) > 0.1:
            axis_name = axis_names.get(i, f"Axis {i}")
            print(f"{axis_name}: {axis:.2f}")
            previous_axis_states[i] = axis

    for i in range(joystick.get_numhats()):
        hat = joystick.get_hat(i)
        if hat != previous_hat_states[i]:
            hat_name = hat_names.get(hat, f"Hat {i}")
            print(f"{hat_name}: {hat}")
            previous_hat_states[i] = hat

try:
    while True:
        display_inputs()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\033[93;1m" + "Stopped checking." + "\033[0m")

pygame.quit()
