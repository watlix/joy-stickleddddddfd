def on_forever():
    servos.P0.set_angle(pins.map(pins.analog_read_pin(AnalogPin.P1), 0, 1023, 10, 170))
basic.forever(on_forever)
