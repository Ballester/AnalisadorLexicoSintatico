from lexico import Lexico

class Sintatico(object):
	
	def __init__(self):
		self.regras = []

	'''
	#Inicializa analisador lexico
	def initLexico(self, arq):
		self.lex = Lexico("inputs.in")

		#Insere estados
		self.lexinsereEstado("q0")
		self.lexinsereEstado("chaves", final=True)
		self.lexinsereEstado("id", final=True)
		self.lexinsereEstado("op", final=True)
		self.lexinsereEstado("num", final=True)

		#Palavras reservadas
		self.lexinsereReservada("for")
		self.lexinsereReservada("while")
		self.lexinsereReservada("if")

		#Identificadores
		self.lexinsereTrans("q0", "id", "a-z")
		self.lexinsereTrans("id", "id", "a-z")
		self.lexinsereTrans("id", "id", "0-9")

		#Operacoes
		self.lexinsereTrans("q0", "op", "+")
		self.lexinsereTrans("q0", "op", "-")
		self.lexinsereTrans("q0", "op", "*")

		#Chaves
		self.lexinsereTrans("q0", "chaves", "{")
		self.lexinsereTrans("q0", "chaves", "}")

		#Numeros
		self.lexinsereTrans("q0", "num", "0-9")
		self.lexinsereTrans("num", "num", "0-9")

		#Seta estado inicial
		self.lexsetInicial("q0")

		#Insere delimitadores
		self.lexinsereDelimitador(" ")
		self.lexinsereDelimitador("\n")
	'''

	#Insere regra de transicao: B eh n-upla de transicoes da gramatica
	def insereRegra(self, A, B):
		self.regras.append((A, B))

	#Executa a regra: N o proximo eh nao terminal, T o proximo eh trminal
	def executaRegra(self, A, token):
		result_total = False
		for regra in self.regras:
			if regra[0][0] == A:

				#Itera sobre regras
				for j in range(0, len(regra[0][1])):
					last_token = token
					result = True

					#Itera sobre as operacoes da regra
					for i in range(0, len(regra[0][1])-1, 2):
						if regra[0][1][i] == 'N':
							result = result and self.executaRegra(regra[0][0][i+1], last_token)
						elif regra[0][1][i] == 'T':
							if last_token == regra[0][1][i+1]:
								last_token =  self.lex.scanner()

							else:
								return False

					result_total = result_total or result
			
				return result_total		






