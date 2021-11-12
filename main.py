import PySimpleGUI as sg
import const as c
import password


def main() -> None:
    layout = [
        [sg.Text('Length:'), sg.InputText(key=c.KEY_LENGTH, default_text=10, size=(4, 1))],
        [sg.Checkbox(text='Numbers', default=True, key=c.KEY_NUMBERS)],
        [sg.Checkbox(text='Ascii', default=True, key=c.KEY_ASCII)],
        [sg.Checkbox(text='Symbols', default=True, key=c.KEY_SYMBOLS)],
        [sg.InputText(key=c.KEY_RESULT)],
        [sg.Button(c.EVENT_GENERATE)],
        [sg.Text('Input password:', key=c.KEY_VALIDATION_RESULT)],
        [sg.InputText(key=c.KEY_VALIDATION)],
        [sg.Button(c.EVENT_VALIDATE)],
        [sg.Button(c.EVENT_EXIT)]
    ]

    window = sg.Window('Password Tool', layout)

    while True:
        event, values = window.read()

        if event == c.EVENT_VALIDATE:
            window.Element(c.KEY_VALIDATION_RESULT).update(password.validate(values[c.KEY_VALIDATION]))

        elif event == c.EVENT_GENERATE:
            window.Element(c.KEY_RESULT).update(password.gen(values))

        elif event == sg.WIN_CLOSED or event == c.EVENT_EXIT:
            break

    window.close()


if __name__ == '__main__':
    main()
