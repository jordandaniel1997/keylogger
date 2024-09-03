import keyboard

word = []
void_str = ''
#TODO: configurar correctamente ambos contadores: arrow left y arrow right
start_index = 1
counter_push_arrow_left = start_index
counter_push_arrow_right = start_index

def print_info()->None:
    print(counter_push_arrow_left)
    print(word)
    print(void_str.join(word))

def space_key()->None:
    space = ' '
    
    #TODO: configurar correctamente ambos contadores: arrow left y arrow right
    if counter_push_arrow_left == start_index:
        word.append(space)
    else:
        word.insert(-counter_push_arrow_left + 1, space)


def back_del_key()->None: 
    #TODO: configurar correctamente ambos contadores: arrow left y arrow right
    if counter_push_arrow_left == start_index:
        word.pop()
    else:
        word.pop(-counter_push_arrow_left)


def arrow_left()->None:
    global counter_push_arrow_left
    global counter_push_arrow_right
    #TODO: configurar correctamente ambos contadores: arrow left y arrow right
    counter_push_arrow_left += 1
    print(counter_push_arrow_left)
    

#TODO: Terminar funcion al presionar la flecha derecha
def arrow_right()->None:
    global counter_push_arrow_right
    global counter_push_arrow_left
    
    if counter_push_arrow_left == start_index:
        counter_push_arrow_right = start_index
        
        
def key_handless(key):
    '''
    Esta función gestiona las teclas presionadas por el usuario
    en base a eso, ejecuta cierta función dependiendo de la tecla
    que se presionó.
    '''
    if not len(key) == 1:
        # Se presionaron teclas que no son letras como ctrl, shift, tab, etc.
        match key:
            case 'space':
                space_key()
            case 'backspace':
                back_del_key()
            case 'flecha izquierda':
                arrow_left()
            case 'flecha derecha':
                arrow_right()
                
        print_info()
    else:
        # El flujo de programa entra aquí si se presiona una letra
        #TODO: configurar correctamente ambos contadores: arrow left y arrow right
        if counter_push_arrow_left == start_index:
            word.append(key)
        else:
            word.insert(-counter_push_arrow_left + 1, key)
            
def main():
    # keyboard.on_press(lambda key: print(key), suppress=False)
    keyboard.on_press(lambda k: key_handless(k.name), suppress=False)
    while True:
        if keyboard.is_pressed('esc'): break
    
    print(void_str.join(word))
    

if __name__ == "__main__":
    main()