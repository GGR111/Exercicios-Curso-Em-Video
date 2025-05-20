n = input('Digite qualquer coisa: ')
print( 'tipo: ',type(n),
      '\né numerico:',n.isnumeric(),
      '\né alfanumerico:', n.isalnum(),
      '\né alfabetico:', n.isalpha(),
      '\né um digito:', n.isdigit(),
      '\né decimal?:', n.isdecimal(),
      '\né uma identificação:', n.isidentifier(),
      '\né em letra minuscula:', n.islower(),
      '\né imprimivel:', n.isprintable(),
      '\né um espaço:', n.isspace(),
      '\né um titulo:', n.istitle(),
      '\né em letra maiuscula:', n.isupper())