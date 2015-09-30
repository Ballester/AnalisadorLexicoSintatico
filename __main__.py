from automato import Automato

aut = Automato()

#Insere estados
aut.insereEstado("q0")
aut.insereEstado("q1", final=True)

#Insere transicoes
aut.insereTrans("q0", "q1", "->")

aut.printEstados()
aut.printFinais()
aut.printTrans()