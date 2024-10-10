#Variables globales
target_char = ""
def run(source_char: str, offset: int) -> str:
    # TODO
    global target_char
    #Variables locales
    # Obtener el valor Unicode del carácter dado
    valor_unicode = ord(source_char)
    
    # Calcular el nuevo valor Unicode aplicando el desplazamiento
    nuevo_valor_unicode = valor_unicode + offset
    
    # Convertir de nuevo a carácter
    target_char = chr(nuevo_valor_unicode)
   
    #Otra opción sería esta
    # target_char = chr(ord(source_char) + offset)
    return target_char


#Código principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(target_char)