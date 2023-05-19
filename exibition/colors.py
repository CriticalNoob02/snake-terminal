#
def ColorsTerminal(Style,Color,Background):
    """Muda a cor do terminal
        --
        Função responsável por mudar cores e estilos do texto no terminal.

        EX:
            `newStyle, base = ColorsTerminal(0,0,7)
            print(f'{newStyle} Não esquece da estrelinha no repositório {base}')`

        retorna: `newStyle, base`
    """
    match Style:
        case 0:
            style = "0" ## Padrão
        case 1:
            style = "1" ## Negrito
        case 2:
            style = "4" ## Sublinhado 
        case 3:
            style = "7" ## Negativo
    match Color:
        case 0:
            color = "37" ## Padrão
        case 1:
            color = "30" ## Cinza
        case 2:
            color = "31" ## Vermelho
        case 3:
            color = "32" ## Verde
        case 4:
            color = "33" ## Amarelo
        case 5:
            color = "34" ## Azul
        case 6:
            color = "35" ## Rosa
        case 7:
            color = "36" ## Verde Claro
    match Background:
        case 0:
            background = "40" ## Padrão
        case 1:
            background = "47" ## Branco
        case 2:
            background = "41" ## Vermelho
        case 3:
            background = "42" ## Verde
        case 4:
            background = "43" ## Amarelo
        case 5:
            background = "44" ## Azul 
        case 6:
            background = "45" ## Rosa
        case 7:
            background = "46" ## Verde Claro

    base = "\033[0;37;40m"
    newStyle = (f"\033[{style};{color};{background}m")

    return newStyle,base
#