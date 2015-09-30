from automato import Automato

aut = Automato()

#Insere estados
aut.insereEstado("q0")
aut.insereEstado("q1", final=True)
aut.insereEstado("q2")
aut.insereEstado("q3")

#Insere transicoes
aut.insereTrans("q0", "q2", "->")
aut.insereTrans("q2", "q3", "->")
aut.insereTrans("q3", "q1", "----")

#Seta estado inicial
aut.setInicial("q0")

aut.printAtual()

#Faz transicoes
aut.doTrans("->")

aut.printAtual()

aut.doTrans("->")

aut.printAtual()
print aut.isFinal()

aut.doTrans("----")

aut.printAtual()
print aut.isFinal()

'''
aut.printEstados()
aut.printFinais()
aut.printTrans()
'''