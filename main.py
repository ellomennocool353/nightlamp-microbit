def on_button_pressed_a():
    global licht
    if licht == 0:
        licht = 1
    else:
        licht = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

licht = 0
if input.light_level() < 70:
    licht = 0

def on_forever():
    if input.light_level() < 70 and licht == 0:
        basic.show_leds("""
            . # # # .
            # # # . .
            # # . . #
            # # # . .
            . # # # .
            """)
    else:
        basic.clear_screen()
basic.forever(on_forever)
