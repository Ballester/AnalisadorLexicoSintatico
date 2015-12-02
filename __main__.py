from sintatico import Sintatico

sin = Sintatico("inputs.in")

#Insere estados
sin.insereEstado("q0")

sin.insereEstado("chavesA", final=True)
sin.insereEstado("chavesB", final=True)
sin.insereEstado("parenA", final=True)
sin.insereEstado("parenB", final=True)

sin.insereEstado("num", final=True)
sin.insereEstado("id", final=True)
sin.insereEstado("op", final=True)
sin.insereEstado("opMenos", final=True)
sin.insereEstado("pot", final=True)
sin.insereEstado("logUn", final=True)
sin.insereEstado("logBin", final=True)

sin.insereEstado("sep_func", final=True)
sin.insereEstado("virg", final=True)
sin.insereEstado("att", final=True)
sin.insereEstado('aspas', final=True)

sin.insereEstado("comp", final=True)
sin.insereEstado("comp_final", final=True)

#Palavras reservadas
sin.insereReservada("if")
sin.insereReservada("else")
sin.insereReservada("local")
sin.insereReservada("true")
sin.insereReservada("false")
sin.insereReservada("nil")

#Identificadores
sin.insereTrans("q0", "id", "a-z")
sin.insereTrans("id", "id", "a-z")
sin.insereTrans("id", "id", "0-9")
sin.insereTrans("id", "id", "_")

#Separadores
sin.insereTrans("q0", "virg", ",")
sin.insereTrans("q0", "att", "=")
sin.insereTrans("q0", "chavesA", "{")
sin.insereTrans("q0", "chavesB", "}")
sin.insereTrans("q0", "sep_func", ".")
sin.insereTrans("q0", "aspas", '"')
sin.insereTrans("q0", "parenA", "(")
sin.insereTrans("q0", "parenB", ")")

#Comparadores
sin.insereTrans("q0", "comp", ">")
sin.insereTrans("q0", "comp", "<")
sin.insereTrans("att", "comp_final", "=")
sin.insereTrans("comp", "comp_final", "=")

#Operacoes
sin.insereTrans("q0", "op", "+")
sin.insereTrans("q0", "opMenos", "-")
sin.insereTrans("q0", "op", "*")
sin.insereTrans("op", "pot", "*")
sin.insereTrans("q0", "op", "/")
sin.insereTrans("q0", "logUn", "!")
sin.insereTrans("q0", "logBin", "&")
sin.insereTrans("q0", "logBin", "|")

#Numeros
sin.insereTrans("q0", "num", "0-9")
sin.insereTrans("num", "num", "0-9")

#Seta estado inicial
sin.setInicial("q0")

#Insere delimitadores
sin.insereDelimitador(" ")
# sin.insereDelimitador("\n")

#nome da regra e lista
sin.insereRegra('A', [('N', 'B')])
sin.insereRegra('B', [('T', 'id'), ('T', 'oi')])


#Le do arquivo
sin.le_token()
print sin.executaRegra('A')
	
		
'''
sin..printEstados()
sin..printFinais()
sin..printTrans()
'''