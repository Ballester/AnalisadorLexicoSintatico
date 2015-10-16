from sintatico import Sintatico
from lexico import Lexico

lex = Lexico("inputs.in")

#Insere estados
lex.insereEstado("q0")

lex.insereEstado("chavesA", final=True)
lex.insereEstado("chavesB", final=True)
lex.insereEstado("parenA", final=True)
lex.insereEstado("parenB", final=True)

lex.insereEstado("num", final=True)
lex.insereEstado("id", final=True)
lex.insereEstado("op", final=True)
lex.insereEstado("opMenos", final=True)
lex.insereEstado("pot", final=True)
lex.insereEstado("logUn", final=True)
lex.insereEstado("logBin", final=True)

lex.insereEstado("sep_func", final=True)
lex.insereEstado("virg", final=True)
lex.insereEstado("att", final=True)
lex.insereEstado('aspas', final=True)

lex.insereEstado("comp", final=True)
lex.insereEstado("comp_final", final=True)

#Palavras reservadas
lex.insereReservada("if")
lex.insereReservada("else")
lex.insereReservada("local")
lex.insereReservada("true")
lex.insereReservada("false")
lex.insereReservada("nil")

#Identificadores
lex.insereTrans("q0", "id", "a-z")
lex.insereTrans("id", "id", "a-z")
lex.insereTrans("id", "id", "0-9")
lex.insereTrans("id", "id", "_")

#Separadores
lex.insereTrans("q0", "virg", ",")
lex.insereTrans("q0", "att", "=")
lex.insereTrans("q0", "chavesA", "{")
lex.insereTrans("q0", "chavesB", "}")
lex.insereTrans("q0", "sep_func", ".")
lex.insereTrans("q0", "aspas", '"')
lex.insereTrans("q0", "parenA", "(")
lex.insereTrans("q0", "parenB", ")")

#Comparadores
lex.insereTrans("q0", "comp", ">")
lex.insereTrans("q0", "comp", "<")
lex.insereTrans("att", "comp_final", "=")
lex.insereTrans("comp", "comp_final", "=")

#Operacoes
lex.insereTrans("q0", "op", "+")
lex.insereTrans("q0", "opMenos", "-")
lex.insereTrans("q0", "op", "*")
lex.insereTrans("op", "pot", "*")
lex.insereTrans("q0", "op", "/")
lex.insereTrans("q0", "logUn", "!")
lex.insereTrans("q0", "logBin", "&")
lex.insereTrans("q0", "logBin", "|")

#Numeros
lex.insereTrans("q0", "num", "0-9")
lex.insereTrans("num", "num", "0-9")

#Seta estado inicial
lex.setInicial("q0")

#Insere delimitadores
lex.insereDelimitador(" ")
lex.insereDelimitador("\n")


#Le do arquivo
var = lex.scanner()
print var
erro = False
while (var != 'EOF' and not erro):
	if len(var) > 1:
		if var[0][0:4] == 'ERRO':
			print var
			erro = True
		else:
			var = lex.scanner()
			print var

	
		
'''
lex..printEstados()
lex..printFinais()
lex..printTrans()
'''