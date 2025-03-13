import customtkinter

# Caminho do arquivo
FILE_PATH = 'filmes_series.txt'

def carregar_filmes(filtro=None, inicializacao=False):
    try:

        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            linhas = file.readlines()

        lista_filmes.delete("1.0", "end")

        filmes_unicos = set()

        for linha in linhas:
            linha_limpa = linha.strip()  
            filmes_unicos.add(linha_limpa)  
        
        encontrou_filmes = False
        for linha in filmes_unicos:
            campos = linha.split(",")
            if len(campos) != 6: 
                continue  

            # Garantir que os campos sejam limpos
            titulo, ano, genero, status, nota, comentario = [campo.strip() for campo in campos]

            texto_formatado = (
                f"Título: {titulo}\n"
                f"Ano de Lançamento: {ano}\n"
                f"Gênero: {genero}\n"
                f"Status: {status}\n"
                f"Nota: {nota}\n"
                f"Comentários: {comentario}\n"
                "-" * 40 + "\n"
            )

            # Aplicar filtro
            if filtro:
                filtro = filtro.lower()
                if (filtro in titulo.lower() or filtro in ano.lower() or 
                    filtro in genero.lower() or filtro in status.lower() or 
                    filtro in nota.lower() or filtro in comentario.lower()):
                    lista_filmes.insert("end", texto_formatado)
                    encontrou_filmes = True
            else:
                lista_filmes.insert("end", texto_formatado)
                encontrou_filmes = True

        # Se nenhum filme foi encontrado
        if not encontrou_filmes:
            lista_filmes.insert("1.0", "Nenhum filme encontrado com o filtro aplicado.")
    except FileNotFoundError:
        lista_filmes.insert("1.0", "Nenhum arquivo encontrado. Adicione filmes primeiro!")


def aplicar_filtro():
    
    filtro = entryFiltro.get().strip()
    carregar_filmes(filtro=filtro)

# Janela de Exibição
janelaLista = customtkinter.CTk()
janelaLista.title("Lista de Filmes")
janelaLista.geometry("600x800")

# Título da Tela
titulo = customtkinter.CTkLabel(janelaLista, text="Lista de Filmes", font=("Arial", 18, "bold"))
titulo.pack(pady=20)

# Campo de Filtro
labelFiltro = customtkinter.CTkLabel(janelaLista, text="Filtrar Filmes (Título, Ano, Gênero, Nota e Sistuação):")
labelFiltro.pack()
entryFiltro = customtkinter.CTkEntry(janelaLista, width=400)
entryFiltro.pack(pady=10)
botaoFiltro = customtkinter.CTkButton(janelaLista, text="Aplicar Filtro", command=aplicar_filtro)
botaoFiltro.pack()

# Área de Exibição dos Filmes
lista_filmes = customtkinter.CTkTextbox(janelaLista, height=600, width=500, wrap="word")
lista_filmes.pack(pady=20)

# Botão para carregar todos os filmes
botaoMostrarTodos = customtkinter.CTkButton(janelaLista, text="Mostrar Todos os Filmes", command=lambda: carregar_filmes())
botaoMostrarTodos.pack()

# Executar a janela
janelaLista.mainloop()
