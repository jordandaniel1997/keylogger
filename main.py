import keyboard

def pos_cursor_map(dict_props:dict, cursor_to_map:str)->bool:
    start_index_right = -1
    start_index_left = 0
    pos_cursor_right, pos_cursor_left = dict_props.values()

    match cursor_to_map:
        case "right":
            if pos_cursor_right == start_index_right:
                return True
            else:
                return False
        case "left":
            pass


def space_key(word_lst, index_dict)->None:
    space = ' '
    #TODO: Cambiar la repeticion de esta validacion
    if index_dict["index_negative"]["index_right"] == index_dict["index_negative"]["start_index"]:
        word_lst.append(space)
    else:
        word_lst.insert(index_dict["index_negative"]["index_right"] + 1, space)

def back_delete_key(word_lst:list, index_dict:dict)->None: 
    #TODO: Cambiar la repeticion de esta validacion
    if index_dict["index_negative"]["index_right"] == index_dict["index_negative"]["start_index"]:
        word_lst.pop()
    else:
        word_lst.pop(index_dict["index_negative"]["index_right"])
        
    print(word_lst)
    
#FIXME: Reparar funcion de flecha izquierda cuando el foco se encuentra al inicio
def arrow_left(word_lst, cursor)->None:
    #length_word = len(word_lst)

    cursor["pos_right"] += -1

#FIXME: Reparar funcion de flecha derecha cuando el foco se encunentra al final
def arrow_right(index_dict)->None:
    index_dict["index_default"]["index_left"] += 1
    index_dict["index_negative"]["index_right"] -= -1
        
def key_handler(key:str, word_lst:list, cursor:dict)->None:
    '''
    Esta función gestiona las teclas presionadas por el usuario
    en base a eso, ejecuta cierta función dependiendo de la tecla
    que se presionó.
    '''
    if not len(key) == 1:
        # Se presionaron teclas que no son letras como ctrl, shift, tab, etc.
        match key:
            case 'space':
                space_key(word_lst, index_dict)
                print(word_lst)
                
            case 'backspace':
                back_delete_key(word_lst, index_dict)
                
            case 'flecha izquierda':
                #arrow_left(word_lst, cursor)
                print(True)
                print(cursor)
            case 'flecha derecha':
                arrow_right(index_dict)
                print(index_dict["index_negative"]["index_right"])
                print(index_dict["index_default"]["index_left"])
    else:
        """_summary_
        El flujo de programa entra aquí si se presiona una letra: a - z
        """

        #FIXME: Reparar la invocación de la funcione pos_cursor_map
        if pos_cursor_map(cursor, "right"):
            word_lst.append(key)
            print(word_lst)
        else:
            word_lst.insert(cursor["pos_right"] + 1, key)
            print(word_lst)

def main():
    word_list = []
    void_str = ''
    cursor = {
        "pos_right": -1,
        "pos_left": 0
    }
    
    key_press = lambda k: key_handler(k.name, word_list, cursor)
    keyboard.on_press(key_press, suppress=False)
    
    # Mantiene la ejecución del script
    while True:
        if keyboard.is_pressed('esc'): break
    
    print(void_str.join(word_list))

if __name__ == "__main__":
    main()