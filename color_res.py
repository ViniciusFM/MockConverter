def toPCT(r,g,b,a): return (r/255.0, g/255.0, b/255.0, a)

def get_syntax_err_string_color_hex():
    return "fab9b6"
    
def get_main_canvas():
    return toPCT(29, 30, 31, 1)

def get_text_input_border_color():
    return toPCT(207, 207, 207, 1)

def get_text_input_bg_color():
    return toPCT(94, 94, 94, 1)
    
def get_text_color():
    return toPCT(255, 255, 255, 1)
