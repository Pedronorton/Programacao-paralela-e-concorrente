#Desenvolvido por: Pedro Cobianchi Borges Paiva
#22/07/2020
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


iteracao = ['1','2','3','4','5', '6', '7', '8', '9', '10']



tempo0 = [0.371269, 0.356483, 0.370045, 0.368752, 0.367508, 0.372139, 0.370273, 0.370273, 0.370273, 0.360372]
tempo1 = [0.841374, 0.828229, 0.827422, 0.829783, 0.837397, 0.829658, 0.837777, 0.834023, 0.843164, 0.848199]
tempo2 = [0.827350, 0.899982, 0.889186, 0.889280, 0.934241, 0.933266, 0.934281, 0.894035, 0.926447, 0.953478]
tempo3 = [0.822456, 0.808102, 0.833085, 0.815304, 0.817417, 0.827766, 0.843491, 0.850715, 0.829895, 0.739998]

tempo06 = [0.091578 ,0.087901 ,0.095772 ,0.088802,0.096294 ,0.094329,0.088567,0.088930,0.091333 ,0.087220 ]
tempo16 = [0.094091  ,0.084881  ,0.100643 ,0.087406, 0.086217  ,0.096081 , 0.086831 , 0.082015 ,0.089496  ,0.087659  ]
tempo26 = [0.130154 , 0.107219 ,0.152307  , 0.153032 , 0.150571 , 0.123626 , 0.112809 , 0.133078 , 0.110685 , 0.152706]
tempo36 = [0.079955  , 0.080214 , 0.083085 , 0.094208 ,0.072664  ,0.080221  , 0.086695 ,0.089374  ,0.084538 ,0.081537 ]

tempo05 = [0.012999  ,0.012219  , 0.012502 ,0.010243  , 0.012157 ,0.010499  , 0.009958 , 0.011800 ,0.011278  , 0.012474 ]
tempo15 = [ 0.009738 , 0.010627 ,0.010039  , 0.008940 ,0.010964  ,0.010459  ,0.011732  , 0.010147 ,0.009721  ,0.009843  ]
tempo25 = [ 0.044486 ,0.026641  , 0.014471 ,0.027177  ,0.031609  ,0.032901  ,0.024022  ,0.046448  ,0.029072  , 0.021491 ]
tempo35 = [ 0.008969 , 0.009013 ,0.000892  ,0.010737  ,0.009219  ,0.007659  , 0.008644 ,0.010577  ,0.009286  ,0.009698  ]


#-----------------------------------------1^7 trapézios

fig, axs = plt.subplots(2, 2)

fig.suptitle('Método do trapézio com a integral da funcção f(x) = x²+√x avaliado no intervalo de 1 a 30 com 10000000 10^7 trapézios')
axs[0,0].bar(iteracao, tempo0)
axs[0,0].set_ylim(0,1)
axs[0,0].set_yticks(np.arange(0, 1, 0.1))
axs[0, 0].set_title('16 Threads')
axs[0,0].set_ylabel("Tempo de execução (segundos)")

axs[0,1].bar(iteracao, tempo1)
axs[0,1].set_ylim(0,1)
axs[0,1].set_yticks(np.arange(0, 1, 0.1))
axs[0, 1].set_title('8 Threads')
axs[0,1].set_ylabel("Tempo de execução (segundos)")

axs[1,0].bar(iteracao, tempo2)
axs[1,0].set_ylim(0,1)
axs[1,0].set_yticks(np.arange(0, 1, 0.1))
axs[1, 0].set_title('4 Threads')
axs[1,0].set_ylabel("Tempo de execução (segundos)")

axs[1,1].bar(iteracao, tempo3)
axs[1,1].set_ylim(0,1)
axs[1,1].set_yticks(np.arange(0, 1, 0.1))
axs[1, 1].set_title('1 Thread')
axs[1,1].set_ylabel("Tempo de execução (segundos)")

#-----------------------------------------1^6 trapézios

fig2, axs2 = plt.subplots(2, 2)

fig2.suptitle('Método do trapézio com a integral da funcção f(x) = x²+√x avaliado no intervalo de 1 a 30 com 1000000 10^6 trapézios')
axs2[0,0].bar(iteracao, tempo06)
axs2[0,0].set_ylim(0,0.2)
axs2[0,0].set_yticks(np.arange(0, 0.2, 0.02))
axs2[0, 0].set_title('16 Threads')
axs2[0,0].set_ylabel("Tempo de execução (segundos)")

axs2[0,1].bar(iteracao, tempo16)
axs2[0,1].set_ylim(0,0.2)
axs2[0,1].set_yticks(np.arange(0, 0.2, 0.02))
axs2[0, 1].set_title('8 Threads')
axs2[0,1].set_ylabel("Tempo de execução (segundos)")

axs2[1,0].bar(iteracao, tempo26)
axs2[1,0].set_ylim(0,0.2)
axs2[1,0].set_yticks(np.arange(0, 0.2, 0.02))
axs2[1, 0].set_title('4 Threads')
axs2[1,0].set_ylabel("Tempo de execução (segundos)")

axs2[1,1].bar(iteracao, tempo36)
axs2[1,1].set_ylim(0,0.2)
axs2[1,1].set_yticks(np.arange(0, 0.2, 0.02))
axs2[1, 1].set_title('1 Thread')
axs2[1,1].set_ylabel("Tempo de execução (segundos)")



#-----------------------------------------1^5 trapézios
fig3, axs3 = plt.subplots(2, 2)

fig3.suptitle('Método do trapézio com a integral da funcção f(x) = x²+√x avaliado no intervalo de 1 a 30 com 100000 10^5 trapézios')
axs3[0,0].bar(iteracao, tempo05)
axs3[0,0].set_ylim(0,0.05)
axs3[0,0].set_yticks(np.arange(0, 0.05, 0.01))
axs3[0, 0].set_title('16 Threads')
axs3[0,0].set_ylabel("Tempo de execução (segundos)")

axs3[0,1].bar(iteracao, tempo15)
axs3[0,1].set_ylim(0,0.05)
axs3[0,1].set_yticks(np.arange(0, 0.05, 0.01))
axs3[0, 1].set_title('8 Threads')
axs3[0,1].set_ylabel("Tempo de execução (segundos)")

axs3[1,0].bar(iteracao, tempo25)
axs3[1,0].set_ylim(0,0.05)
axs3[1,0].set_yticks(np.arange(0, 0.05, 0.01))
axs3[1, 0].set_title('4 Threads')
axs3[1,0].set_ylabel("Tempo de execução (segundos)")

axs3[1,1].bar(iteracao, tempo35)
axs3[1,1].set_ylim(0,0.05)
axs3[1,1].set_yticks(np.arange(0, 0.05, 0.01))
axs3[1, 1].set_title('1 Thread')
axs3[1,1].set_ylabel("Tempo de execução (segundos)")

#------------------------------------------ MÉDIAS

fig4, axs4 = plt.subplots(2, 2)

media0 = 0
media1 = 0
media2 = 0
media3 = 0

media06 = 0
media16 = 0
media26 = 0
media36 = 0

media05 = 0
media15 = 0
media25 = 0
media35 = 0

mediaTotal7=[]
mediaTota16=[]
mediaTota15=[]
for i in range(10):
    media0 += tempo0[i]/10
    media1 += tempo1[i] / 10
    media2 += tempo2[i] / 10
    media3 += tempo3[i] / 10

    media06 += tempo06[i] / 10
    media16 += tempo16[i] / 10
    media26 += tempo26[i] / 10
    media36 += tempo36[i] / 10

    media05 += tempo05[i] / 10
    media15 += tempo15[i] / 10
    media25 += tempo25[i] / 10
    media35 += tempo35[i] / 10

mediaTotal7.append(media0)
mediaTotal7.append(media1)
mediaTotal7.append(media2)
mediaTotal7.append(media3)

mediaTota16.append(media06)
mediaTota16.append(media16)
mediaTota16.append(media26)
mediaTota16.append(media36)

mediaTota15.append(media05)
mediaTota15.append(media15)
mediaTota15.append(media25)
mediaTota15.append(media35)

medias = ["16 Threads", "8 Threads", "4 Threads", "1 Thread"]
fig4.suptitle('Método do trapézio com a integral da funcção f(x) = x²+√x avaliado no intervalo de 1 a 30')
axs4[0,0].set_ylim(0,1)
axs4[0,0].bar(medias, mediaTotal7)
# axs4[0,0].set_xticks((0,1))
axs4[0, 0].set_title('Media dos tempos para n = 10000000 10^7')
axs4[0,0].set_ylabel("Média do tempo de execução (segundos)")

axs4[0,1].bar(medias, mediaTota16)
axs4[0,1].set_ylim(0,0.4)
axs4[0,1].set_yticks(np.arange(0, 0.4, 0.1))
axs4[0, 1].set_title('Media dos tempos para n = 1000000 10^6')
axs4[0,1].set_ylabel("Média do tempo (segundos)")

axs4[1,0].bar(medias, mediaTota15)
axs4[1,0].set_ylim(0,0.04)
axs4[1,0].set_yticks(np.arange(0, 0.04, 0.01))
axs4[1, 0].set_title('Media dos tempos para n = 100000 10^5')

axs4[1,0].set_ylabel("Média do tempo (segundos)")


values = [['T(p)', 'S(p)''</b>'], #1st col
  [media3,1],
  [media2, media3/media2],
  [media1, media3 / media1],
  [media0, media3/media0]]


table = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela de speed-up para n = 10000000 10^7")
    )
)

values1 = [['T(p)', 'S(p)''</b>'], #1st col
  [media36,1],
  [media26, media36/media26],
  [media16, media36 / media16],
  [media06, media36/media06]]

table1 = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values1,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela de speed-up para n = 1000000 10^6")
    )
)

values2 = [['T(p)', 'S(p)''</b>'], #1st col
  [media35,1],
  [media25, media35/media25],
  [media15, media35 / media15],
  [media05, media35/media05]]

table2 = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values2,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela de speed-up para n = 100000 10^5")
    )
)

#16
speedup07 = media3/media0
#8
speedup17 = media3/media1
#4
speedup27 = media3/media2


values3 = [ ['e''</b>'], #1st col
  ['-'],
  [((1/speedup07) - (1/16))/ (1 - (1/16))],
  [((1/speedup17) - (1/8))/ (1 - (1/8))],
  [((1/speedup27) - (1/4))/ (1 - (1/4))]]

table3 = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values3,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela utilizando a métrica Karp-Flatt para n = 100000 10^7")
    )
)

speedup06 = media36/media06
speedup16 = media36/media16
speedup26 = media36/media26

values4 = [ ['e''</b>'], #1st col
  ['-'],
  [((1/speedup06) - (1/16))/ (1 - (1/16))],
  [((1/speedup16) - (1/8))/ (1 - (1/8))],
  [((1/speedup26) - (1/4))/ (1 - (1/4))]]


table4 = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values4,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela utilizando a métrica Karp-Flatt para n = 100000 10^6")
    )
)

speedup05 = media35/media05
speedup15 = media35/media15
speedup25 = media35/media25

values5 = [ ['e''</b>'], #1st col
  ['-'],
  [((1/speedup05) - (1/16))/ (1 - (1/16))],
  [((1/speedup15) - (1/8))/ (1 - (1/8))],
  [((1/speedup25) - (1/4))/ (1 - (1/4))]]


table5 = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values5,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela utilizando a métrica Karp-Flatt para n = 100000 10^5")
    )
)

#---------------------------------------------------------- eficiencia

values6 = [ ['S(p)', 'E(p)','</b>'], #1st col
  ['1',['1']],
  [speedup27, speedup27/4],
  [speedup17, speedup17/8],
  [speedup07, speedup07/16]]

print(speedup07)

#eficiencia para n = 10000000
table6 = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values6,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela para cálculo de eficiência para n = 10000000 10^7")
    )
)


values7 = [ ['S(p)', 'E(p)','</b>'], #1st col
  ['1',['1']],
  [speedup26, speedup26/4],
  [speedup16, speedup16/8],
  [speedup06, speedup06/16]]

#eficiencia para n = 1000000
table7 = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values7,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela para cálculo de eficiência para n = 1000000 10^6")
    )
)

values8 = [ ['S(p)', 'E(p)','</b>'], #1st col
  ['1',['1']],
  [speedup25, speedup25/4],
  [speedup15, speedup15/8],
  [speedup05, speedup05/16]]


#eficiencia para n = 100000

table8 = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],

  header = dict(
    values = [ [],
                  ['<b>1 Thread</b>'],
                  ['<b>4 Threads</b>'],
                  ['<b>8 Threads</b>'],
                  ['<b>16 Threads</b>'],
               ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values8,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
],
    layout=go.Layout(
    title=go.layout.Title(text="Tabela para cálculo de eficiência para n = 100000 10^5")
    )
)


table.show()
table1.show()
table2.show()
table3.show()
table4.show()
table5.show()
table6.show()
table7.show()
table8.show()

plt.show()
