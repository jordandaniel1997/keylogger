import keyboard

def space_key(word_lst, index_dict)->None:
    space = ' '
    
    if index_dict["index_negative"]["index_right"] == index_dict["index_negative"]["start_index"]:
        word_lst.append(space)
    else:
        word_lst.insert(index_dict["index_negative"]["index_right"] + 1, space)

def back_delete_key(word_lst:list, index_dict:dict)->None: 
    if index_dict["index_negative"]["index_right"] == index_dict["index_negative"]["start_index"]:
        word_lst.pop()
    else:
        word_lst.pop(index_dict["index_negative"]["index_right"])
        
    print(word_lst)
    
#FIXME: Reparar funcion de flecha izquierda cuando el foco se encuentra al inicio
def arrow_left(word_lst, index_dict)->None:
    length_word = len(word_lst)
    
    index_dict["index_negative"]["index_right"] += -1
    index_dict["index_default"]["index_left"] += 1
    
#FIXME: Reparar funcion de flecha derecha cuando el foco se encunentra al final
def arrow_right(index_dict)->None:
    index_dict["index_default"]["index_left"] += 1
    index_dict["index_negative"]["index_right"] -= -1
        
def key_handless(key:str, word_lst:list, index_dict:dict)->None:
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
                arrow_left(word_lst, index_dict)
                print(index_dict)
                print(word_lst[index_dict["index_negative"]["index_right"]])
                print(word_lst[index_dict["index_default"]["index_left"]])
                
            case 'flecha derecha':
                arrow_right(index_dict)
                print(index_dict["index_negative"]["index_right"])
                print(index_dict["index_default"]["index_left"])                  
    else:
        """_summary_
        El flujo de programa entra aquí si se presiona una letra: a - z
        """
        if index_dict["index_negative"]["index_right"] == index_dict["index_negative"]["start_index"]:
            word_lst.append(key)
            print(word_lst)
        else:
            word_lst.insert(index_dict["index_negative"]["index_right"] + 1, key)
            print(word_lst)

def main():
    word_list = []
    void_str = ''
    indexes = {
        "index_negative": {
            "start_index": -1,
            "index_right": None
        },
        "index_default": {
            "start_index": 0,
            "index_left": None
        }
    }
    indexes['index_negative']["index_right"] = indexes['index_negative']["start_index"]
    indexes['index_default']["index_left"] = indexes['index_default']["start_index"]
    
    key_press = lambda k: key_handless(k.name, word_list, indexes)
    keyboard.on_press(key_press, suppress=False)
    
    # Mantiene la ejecución del script
    while True:
        if keyboard.is_pressed('esc'): break
    
    print(void_str.join(word_list))
    

if __name__ == "__main__":
    main()