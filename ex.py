ok = 0
numero = 0

def on_gesture_shake():
    if ok == 1:
        for i in range(5):
            for j in range(5):
                led.toggle(i, j)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global numero, ok
    while input.button_is_pressed(Button.A):
        if input.temperature() > 10 and input.temperature() < 18:
            basic.show_string("Watering the plant")
    while input.button_is_pressed(Button.B):
        numero = randint(0, 100)
        basic.show_number(numero)
        if numero < 60:
            basic.show_string("Watering the plant")
        elif numero > 70:
            basic.show_string("Stopped watering the plant")
    while input.logo_is_pressed():
        if input.light_level() > 120:
            ok = 1
        elif input.light_level() < 120:
            ok = 0
            basic.show_string("Stopped watering the plant")
basic.forever(on_forever)
