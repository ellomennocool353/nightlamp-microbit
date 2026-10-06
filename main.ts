input.onButtonPressed(Button.A, function () {
    if (licht == 0) {
        licht = 1
    } else {
        licht = 0
    }
})
let licht = 0
if (input.lightLevel() < 70) {
    licht = 0
}
basic.forever(function () {
    if (input.lightLevel() < 70 && licht == 0) {
        basic.showLeds(`
            . # # # .
            # # # . .
            # # . . #
            # # # . .
            . # # # .
            `)
    } else {
        basic.clearScreen()
    }
})
