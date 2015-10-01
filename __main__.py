from lexico import Lexico

lex = Lexico("inputs.in")

#Insere estados
lex.insereEstado("q0", final=True)
lex.insereEstado("q1")
lex.insereEstado("q2")
lex.insereEstado("q3")

#Insere transicoes
lex.insereTrans("q0", "q0", "o")
lex.insereTrans("q0", "q0", "i")
lex.insereTrans("q2", "q3", "->")
lex.insereTrans("q3", "q1", "----")

#Seta estado inicial
lex.setInicial("q0")
lex.insereDelimitador(" ")

#Le do arquivo
var = lex.scanner()
print var
while (var != 'EOF' and var[0] != 'ERRO'):
	var = lex.scanner()
	print var

'''
lex.printEstados()
lex.printFinais()
lex.printTrans()
'''