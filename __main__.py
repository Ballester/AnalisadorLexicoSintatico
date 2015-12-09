from sintatico import Sintatico
import networkx as nx
import matplotlib.pyplot as plt

sin = Sintatico("inputs.in", debugging=True)
plotter = False

edge_labels = {}

#READ GRAMATICA FROM FILE
fgrammar = open('gramatica.txt')
fauto    = open('automato.txt')

grammar = fgrammar.readlines()
auto    = fauto.readlines()

#Example: prog -> listcmd <EOF>
#Nome da regra -> valores (entre <> sao terminais)
for i in grammar:
    if len(i) <= 1:
        continue
    i = i.split()
    regra = []
    for j in range(2, len(i)):
        if i[j] == 'lambda':
            regra.append(('E', i[j].split('\n')[0]))
        elif i[j][0] == '<':
            regra.append(('T', i[j][1:len(i[j])-1]))
        else:
            regra.append(('N', i[j]))
    sin.insereRegra(i[0], regra)

#<-- Lista de estados -->
#(q0) <q1> <q2> q3
#estado inicial, estado final, estado final, estado normal
#<-- Lista de transicoes -->
#q0 q1 a-z
#q0 q1 b
#q0 q3 .
G = nx.Graph()
read_estados = False
read_trans   = False
for i in auto:
    if len(i) <= 1:
        continue
    #troca se esta lendo estados ou transicoes
    if i == '<-- Lista de estados -->\n':
        read_estados = True
        read_trans = False
        continue
    if i == '<-- Lista de transicoes -->\n':
        read_estados = False
        read_trans = True
        continue

    if read_estados:
        i = i.split()
        for j in i:
            if j[0] == '(':
                j = j[1:len(j)-1]
                sin.insereEstado(j)
                sin.setInicial(j)
            elif j[0] == '<':
                j = j[1:len(j)-1]
                sin.insereEstado(j, final=True)
            else:
                sin.insereEstado(j)

            G.add_node(j)
    
    elif read_trans:
        i = i.split()
        for j in range(2, len(i)):
            if i[j] == 'blank':
                sin.insereTrans(i[0], i[1], ' ')
            else:
                sin.insereTrans(i[0], i[1], i[j])

        G.add_edge(i[0], i[1])
        edge_labels.update({(i[0], i[1]): i[j]})

if plotter:
    node_size=300
    node_color='blue'
    node_alpha=0.3
    node_text_size=10
    edge_color='blue'
    edge_alpha=0.3
    edge_tickness=1
    edge_text_pos=0.3
    text_font='sans-serif'

    graph_pos=nx.spring_layout(G)
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                               alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                               alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                                font_family=text_font)
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
                                label_pos=edge_text_pos)

    plt.show()

#Palavras reservadas
sin.insereReservada("if")
sin.insereReservada("else")
sin.insereReservada("local")
sin.insereReservada("true")
sin.insereReservada("false")
sin.insereReservada("nil")
sin.insereReservada("io.write")
sin.insereReservada("io.read")

#Insere delimitadores
sin.insereDelimitador(" ")

#Le do arquivo
sin.le_token()
if sin.executaRegra('prog'):
    print 'Codigo correto'
else:
    raise Exception('ERRO - Sintatico', sin.tk, sin.linha_atual+1, sin.col_atual+1)
	
		
'''
sin..printEstados()
sin..printFinais()
sin..printTrans()
'''