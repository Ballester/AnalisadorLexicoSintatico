from sintatico import Sintatico

lex = Lexico("inputs.in")

#Le do arquivo
var = lex.scanner()
print var
erro = False
while (var != 'EOF' and not erro):
	if len(var) > 1:
		if var[0] == 'ERRO':
			print var
			erro = True
		else:
			var = lex.scanner()
			print var

	
		
'''
lex.printEstados()
lex.printFinais()
lex.printTrans()
'''