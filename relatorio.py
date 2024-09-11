from fpdf import FPDF

class PDF(FPDF):
    
    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')
        
    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
        
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
        
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()
        
    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()
        
    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)
        
pdf = PDF()

pdf.add_page()

pdf.titulo('Análise de dados')
pdf.sub_titulo('ANÁLISE DA DESIGUALDADE NA EDUCAÇÃO BRASILEIRA')
pdf.image('image.png', 40, 90, 130)
pdf.ln(160)
pdf.linha_centralizada('Autor: Roger F. Souza')

# pág 1
pdf.add_page()

pdf.titulo_base('Introdução')
pdf.paragrafo('A educação superior desempenha um papel crucial no desenvolvimento social e econômico de um país, oferecendo a preparação necessária para que o indivíduo adquira aptidão para que o mesmo conquiste seu espaço no mercado de trabalho.')
pdf.paragrafo('Este relatório foi feito com base nos dados disponibilizados pelo Ministério da Educação(MEC), os quais oferecem uma ampla visão quantitativa dos cursos de graduação brasileiros durante o ano de 2022.')

# pág 2
pdf.add_page()

pdf.titulo_base('Análise dos dados')

pdf.paragrafo('A partir da análise inicial, nota-se uma disparidade significativa na distribuição de vagas disponíveis entre as diferentes regiões do país, com uma concentração maior nas áreas de maior desenvolvimento econômico. Isso resulta em um investimento mais robusto na educação, tanto por instituições privadas quanto públicas.')
pdf.imagem('Gráfico_Vagas_Regiao.png', 10, 105, 200)

# pág 3
pdf.add_page()

pdf.paragrafo('A educação à distância tem mostrado uma clara predominância no número de vagas, especialmente após a pandemia. Essa modalidade se tornou a escolha preferida da população devido à sua maior flexibilidade de horários e, em geral, por ser mais acessível para pessoas de baixa renda, já que elimina custos adicionais, como transporte.')
pdf.imagem('Gráfico_Modalidades.png', 10, 105, 200)

# pág 4
pdf.add_page()

pdf.paragrafo('Podemos observar que a maioria da população opta por ingressar em instituições privadas, com ou sem fins lucrativos. Isso ocorre principalmente devido à alta concorrência por vagas em instituições públicas, o que diminui consideravelmente as chances de ingresso. Muitas pessoas, especialmente aquelas que precisam trabalhar para se sustentar ou apoiar suas famílias, não conseguem dedicar tempo suficiente aos estudos para competir por vagas tão disputadas.')
pdf.imagem('Gráfico_Cat_Admin.png', 5, 105, 200)

# pág 5
pdf.add_page()
 
pdf.paragrafo('Por fim, um aspecto interessante destacado neste estudo é a preferência pelos cursos de grau Tecnólogo. Essa escolha parece estar relacionada à necessidade de a maior parte da população ingressar rapidamente no mercado de trabalho, uma vez que esses cursos, com duração média de 2 a 3 anos, oferecem essa possibilidade.')
pdf.imagem('Gráfico_Graus_Ensino.png', 0, 105, 210)

# pág 6
pdf.add_page()
pdf.titulo_base('Conclusão')

pdf.paragrafo('Com base nos fatos apresentados podemos notar padrões muito interessantes em relação a educação brasileira, o que podemos tomar como base para responder o motivo da mesma ser desigual nesta proporção.')
pdf.paragrafo('Primeiramente no âmbito regional, onde vemos uma alta discrepância na distribuição de vagas, onde em sua grande maioria estão concentradas no sudeste, região que por sua vez possui um alto índice de desenvolvimento econômico, também é perceptível a grande preferência por vagas de ensino à distância devido à diversos fatores como a situação econômica.')
pdf.paragrafo('Além disso pudemos comparar a diferença de escolha entre instituições, a qual se deve principalmente por conta da alta concorrência enfrentada nas instituições públicas, dos quais muita gente não possui tempo o suficiente para se dedicar a estudar por conta de precisarem garantir seu sustento.')
pdf.paragrafo('E finalmente conseguimos notar a preferência de cerca de metade da população por cursos de grau tecnólogo, o que pode ser interligado a fatores como a necessidade de ingressar com urgência no mercado de trabalho a fim de garantir o sustento próprio e de seus familiares.')


pdf.output('relatorio.pdf')