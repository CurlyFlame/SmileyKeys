import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, KCString
from kmk.modules.encoder import EncoderHandler

# Create the keyboard
keyboard = KMKKeyboard()

# --- Add Macro Module ---
macros = Macros()
keyboard.modules.append(macros)

# --- Add Encoder Module ---
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# --- Define Button Pins ---
PINS = [board.D3, board.D4, board.D2, board.D1, board.D0]  # Adjust pins to your wiring

# No key matrix; just 5 direct keys
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

# --- Define Emoji Macros ---
keyboard.keymap = [
    [
        KC.MACRO(KCString("😀")),  # Button 1
        KC.MACRO(KCString("😂")),  # Button 2
        KC.MACRO(KCString("👍")),  # Button 3
        KC.MACRO(KCString("🔥")),  # Button 4
        KC.MACRO(KCString("💯")),  # Button 5
    ]
]

# --- Configure Encoder ---
# Replace board.D5, board.D6 with your actual encoder A/B pins
encoder.pins = ((board.D5, board.D6, None),)  # (pin_a, pin_b, pin_button) — button optional

# Volume control on encoder
encoder.map = [
    ((KC.VOLD, KC.VOLU),),  # Rotate left: volume down, right: volume up
]

# --- Start KMK ---
if __name__ == '__main__':
    keyboard.go()
