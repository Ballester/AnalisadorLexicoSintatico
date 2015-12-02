from lexico import Lexico
from automato import Automato
#todo colocar palavra vazia
#funciona se for uma gramatica fatorada a esquerda
class Sintatico(Lexico):
	
	def __init__(self, file):
		# self.lex = Lexico(file)
		self.tk = ''
		self.regras = []
		self.nome_regras = []
		self.reservadas = []
		self.delimitadores = []
		self.aut = Automato()
		self.arq = open(file).readlines()
		self.linha_atual = 0
		self.col_atual = 0

	def le_token(self):
		self.tk = self.scanner()
		return self.tk

	#nome regra is the variable being used
	#regra is a list of tuples, each tuple is a variable followed by wether it is a rule or a terminal
	#T is for terminal N is for a rule
	def insereRegra(self, nome_regra, regra):
		self.nome_regras.append(nome_regra)
		self.regras.append(regra)

	def executaRegra(self, nome_regra):
		
		idx = [i for i, x in enumerate(self.nome_regras) if x == nome_regra]
		if idx == []:
			raise Exception('ERRO - Sintatico, regra invalida')

		last_rule = False	#checks if last rule was used or not
		return_value = False #used to return whether it worked or not
		for idx_now in idx:
			if not last_rule:
				for i in range(0, len(self.regras[idx_now])):
					
					#Check if is a terminal
					if self.regras[idx_now][i][0] == 'T':
						#Check if token is correct
						if self.regras[idx_now][i][1] == self.tk[1]:
							self.le_token()
							last_rule = True

						else:
							break

					elif self.regras[idx_now][i][0] == 'N':
						if executaRegra(regras[idx_now][i][1]):
							last_rule = True

						else:
							break

				else:
					return_value = True

		return return_value