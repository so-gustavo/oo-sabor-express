class restaurante:
    nome = ''
    categoria = ''
    status_do_restaurante = False

restaurante_serto = restaurante()
restaurante_serto.nome = 'Sertó'
restaurante_serto.categoria = 'Comida Mineira'
restaurante_caracol = restaurante()

restaurantes = [restaurante_serto, restaurante_caracol]

print(vars(restaurante_serto))
