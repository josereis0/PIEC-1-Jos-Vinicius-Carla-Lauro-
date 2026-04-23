import xlsxwriter as Criacaodeplanilha
import os

"""

#Depois que adicionar as rotas, sujeito à alteraçpões importantes

"""
# alterar o caminho do arquivo para o local onde deseja salvar a planilha
camilhoArquivo = "C:\\Users\\carla\\OneDrive\\Área de Trabalho\\Curso de Python\\Projeto Piec\\Controle de Estoque.xlsx"

# Cria o arquivo Excel
workbook = Criacaodeplanilha.Workbook(camilhoArquivo)

# Cria uma sheet chamada Controle de Estoque
sheetpadrao = workbook.add_worksheet("Controle de Estoque")

# Formatação para o título (cabeçalho da tabela)
CorTitulo =workbook.add_format({
        "font_name": "Arial",
        "font_size": 10,
        "bold": True,
        "font_color": "white",
        "bg_color": "navy",
        "border": 1,
        "align": "center",
        "valign": "vcenter"
})

# Formatação para os dados que serão inseridos
CorDados =workbook.add_format({
        "font_name": "Arial",
        "font_size": 12,
        "bold": True,
        "font_color": "white",
        "bg_color": "navy",
        "border": 1,
        "align": "center",
        "valign": "vcenter"
})

# Ajusta altura da primeira linha (cabeçalho)
sheetpadrao.set_row(0, 30)

# Ajusta largura das colunas de A até F
sheetpadrao.set_column('A:F', 25)


# Escreve os títulos do cabeçalho com a formatação definida
sheetpadrao.write("A1", "Produto", CorTitulo)
sheetpadrao.write("B1", "Código", CorTitulo)
sheetpadrao.write("C1", "Quantidade", CorTitulo)
sheetpadrao.write("D1", "Estoque Mínimo", CorTitulo)
sheetpadrao.write("E1", "Data", CorTitulo)
sheetpadrao.write("F1", "Horário", CorTitulo)

#Adicionar um loop for para alterar a largura e altura das celulas depois que juntar com o openpy e conseguir ler a planilha.

# Fecha o arquivo Excel (salva as alterações)
workbook.close()

# Abre o arquivo Excel automaticamente
os.startfile(camilhoArquivo)
