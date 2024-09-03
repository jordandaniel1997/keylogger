import keyboard

large_word = []
word = []
void_str = ''
#TODO: configurar correctamente ambos contadores: arrow left y arrow right
start_index = 1
counter_push_arrow_left = start_index
counter_push_arrow_right = start_index

def print_info():
    print(counter_push_arrow_left)
    print(word)
    print(void_str.join(word))

def space_key():
    space = ' '
    
    #TODO: configurar correctamente ambos contadores: arrow left y arrow right
    if counter_push_arrow_left == start_index:
        word.append(space)
    else:
        word.insert(-counter_push_arrow_left + 1, space)


def back_del_key(): 
    #TODO: configurar correctamente ambos contadores: arrow left y arrow right
    if counter_push_arrow_left == start_index:
        word.pop()
    else:
        word.pop(-counter_push_arrow_left)


def arrow_left():
    global counter_push_arrow_left
    global counter_push_arrow_right
    #TODO: configurar correctamente ambos contadores: arrow left y arrow right
    counter_push_arrow_left += 1
    print(counter_push_arrow_left)
    

#TODO: Terminar funcion al presionar la flecha derecha
def arrow_right():
    global counter_push_arrow_right
    global counter_push_arrow_left
    
    if counter_push_arrow_left == start_index:
        counter_push_arrow_right = start_index
        
        


def main(key):
    # Se presionaron teclas que no son letras como ctrl, shift, tab, etc
    if not len(key) == 1:
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
    # Se presiono una letra pero la flecha izquierda no
    else:
        #TODO: configurar correctamente ambos contadores: arrow left y arrow right
        if counter_push_arrow_left == start_index:
            word.append(key)
            print_info()
        else:
            word.insert(-counter_push_arrow_left + 1, key)
            print_info()
            
            
            

def get_key(key):
   main(key.name)
        
# keyboard.on_press(lambda key: print(key), suppress=False)
keyboard.on_press(get_key, suppress=False)
keyboard.wait('esc')
print(void_str.join(word))