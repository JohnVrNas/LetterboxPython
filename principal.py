import customtkinter

FILE_PATH = 'filmes_series.txt'

def buscar_filme():
    """Busca um filme pelo título e preenche os campos com as informações encontradas."""
    titulo_busca = entryBusca.get().strip().lower()
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            for linha in file:
                campos = linha.strip().split(",")
                if len(campos) < 6:
                    continue  # Ignorar registros incompletos
                if campos[0].strip().lower() == titulo_busca:
                    # Preenche os campos com as informações encontradas
                    entryTitulo.delete(0, "end")
                    entryTitulo.insert(0, campos[0])  # Título
                    entryAno.delete(0, "end")
                    entryAno.insert(0, campos[1])  # Ano
                    entryGenero.set(campos[2])  # Gênero
                    status_var.set(campos[3])  # Status
                    slider_nota.set(float(campos[4]))  # Nota
                    entryComentario.delete("1.0", "end")
                    entryComentario.insert("1.0", campos[5])  # Comentários
                    label_valor_slider.configure(text=f"Nota: {float(campos[4]):.1f}")
                    retornoBusca.configure(text=f"Filme '{campos[0]}' encontrado!", text_color="green")
                    return
        retornoBusca.configure(text="Filme não encontrado.", text_color="red")
    except FileNotFoundError:
        retornoBusca.configure(text="Arquivo não encontrado.", text_color="red")

def atualizar_valor_slider(valor):
    """Arredonda o valor do Slider para o incremento de 0.5 e atualiza a Label."""
    valor_arredondado = round(float(valor) * 2) / 2
    label_valor_slider.configure(text=f"Nota: {valor_arredondado:.1f}")

def cadastrar():
    """Salva ou atualiza um filme no arquivo e limpa os campos após o cadastro."""
    titulo = entryTitulo.get().strip().lower()  # Normaliza para lowercase
    ano = entryAno.get().strip()
    genero = entryGenero.get().strip()
    status = status_var.get()
    nota = slider_nota.get()
    comentario = entryComentario.get("1.0", "end").strip()
    
    try:
        linhas = []
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            linhas = file.readlines()
        
        atualizado = False
        registros_normalizados = set()  # Para evitar duplicação
        
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            for linha in linhas:
                campos = linha.strip().split(",")
                if len(campos) >= 6:
                    campos_normalizados = [
                        campo.strip().lower() if i == 0 else campo.strip()  # Normaliza título
                        for i, campo in enumerate(campos)
                    ]
                    registros_normalizados.add(tuple(campos_normalizados))
                
                # Atualiza o filme correspondente
                if len(campos) >= 6 and campos[0].strip().lower() == titulo:
                    file.write(f"{titulo},{ano},{genero},{status},{nota:.1f},{comentario}\n")
                    atualizado = True
                else:
                    file.write(linha)
            
            # Se não foi atualizado, adiciona como novo
            if not atualizado:
                novo_registro = (titulo, ano, genero, status, f"{nota:.1f}", comentario)
                if novo_registro not in registros_normalizados:
                    file.write(f"{titulo},{ano},{genero},{status},{nota:.1f},{comentario}\n")
        
        retornoBotao.configure(text="Cadastrado/Atualizado com sucesso!", text_color="green")
    except FileNotFoundError:
        # Cria o arquivo se não existir
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            file.write(f"{titulo},{ano},{genero},{status},{nota:.1f},{comentario}\n")
        retornoBotao.configure(text="Arquivo criado e filme cadastrado!", text_color="green")
    
    # Limpar os campos após o cadastro
    entryTitulo.delete(0, "end")
    entryAno.delete(0, "end")
    entryGenero.set("")  # Limpar o menu suspenso
    status_var.set("")  # Limpar os RadioButtons
    slider_nota.set(0)  # Resetar o Slider para 0
    label_valor_slider.configure(text="Nota: 0.0")
    entryComentario.delete("1.0", "end")

    
    # Limpar os campos após o cadastro
    entryTitulo.delete(0, "end")
    entryAno.delete(0, "end")
    entryGenero.set("")  # Limpar o menu suspenso
    status_var.set("")  # Limpar os RadioButtons
    slider_nota.set(0)  # Resetar o Slider para 0
    label_valor_slider.configure(text="Nota: 0.0")
    entryComentario.delete("1.0", "end")

def apagar_filme():
    """Apaga o filme pesquisado pelo título do arquivo de dados."""
    titulo_busca = entryBusca.get().strip().lower()
    
    if not titulo_busca:
        retornoBusca.configure(text="Digite um título para apagar.", text_color="red")
        return
    
    try:
        linhas = []
        filme_encontrado = False

        # Lê todas as linhas do arquivo
        with open(FILE_PATH, 'r', encoding='latin-1') as file:
            linhas = file.readlines()
        
        # Reescreve o arquivo removendo o filme correspondente
        with open(FILE_PATH, 'w', encoding='latin-1') as file:
            for linha in linhas:
                campos = linha.strip().split(",")
                if len(campos) >= 6 and campos[0].strip().lower() == titulo_busca:
                    filme_encontrado = True  # Filme encontrado e não será reescrito
                else:
                    file.write(linha)
        
        if filme_encontrado:
            retornoBusca.configure(text=f"Filme '{titulo_busca}' apagado com sucesso!", text_color="green")
            # Limpar os campos após exclusão
            entryTitulo.delete(0, "end")
            entryAno.delete(0, "end")
            entryGenero.set("")  # Limpar o menu suspenso
            status_var.set("")  # Limpar os RadioButtons
            slider_nota.set(0)  # Resetar o Slider para 0
            label_valor_slider.configure(text="Nota: 0.0")
            entryComentario.delete("1.0", "end")
        else:
            retornoBusca.configure(text="Filme não encontrado para apagar.", text_color="red")
    except FileNotFoundError:
        retornoBusca.configure(text="Arquivo não encontrado. Não há filmes para apagar.", text_color="red")

# Criação da tela Main
janelaMain = customtkinter.CTk()
janelaMain.title("Biblioteca de Filmes")
janelaMain.geometry("400x840")

# Título
titulo = customtkinter.CTkLabel(janelaMain, text="Letterboxd", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Campo de busca
labelBusca = customtkinter.CTkLabel(janelaMain, text="Buscar por título")
labelBusca.pack()
entryBusca = customtkinter.CTkEntry(janelaMain)
entryBusca.pack()
botaoBuscar = customtkinter.CTkButton(janelaMain, text="Buscar", command=buscar_filme)
botaoBuscar.pack(pady=10)
retornoBusca = customtkinter.CTkLabel(janelaMain, text="")
retornoBusca.pack()

# Input: Título
labelTitulo = customtkinter.CTkLabel(janelaMain, text="Título")
labelTitulo.pack()
entryTitulo = customtkinter.CTkEntry(janelaMain)
entryTitulo.pack()

# Input: Ano
labelAno = customtkinter.CTkLabel(janelaMain, text="Ano de Lançamento")
labelAno.pack()
entryAno = customtkinter.CTkEntry(janelaMain)
entryAno.pack()

# Input: Gênero
labelGenero = customtkinter.CTkLabel(janelaMain, text="Gênero")
labelGenero.pack()
entryGenero = customtkinter.CTkOptionMenu(janelaMain, values=["Romance", "Ficção Científica", "Ação", "Suspense", "Terror", "Drama", "Comédia"])
entryGenero.pack()

# Input: Status
labelStatus = customtkinter.CTkLabel(janelaMain, text="Status")
labelStatus.pack(pady=10)
quadroStatus = customtkinter.CTkFrame(janelaMain)
quadroStatus.pack()
status_var = customtkinter.StringVar(value="")
radio_assistido = customtkinter.CTkRadioButton(quadroStatus, text="Assistido", variable=status_var, value="Assistido")
radio_assistido.pack(side="left", padx=10)
radio_nao_assistido = customtkinter.CTkRadioButton(quadroStatus, text="Não Assistido", variable=status_var, value="Não Assistido")
radio_nao_assistido.pack(side="left", padx=10)

# Input: Nota
labelNota = customtkinter.CTkLabel(janelaMain, text="Nota")
labelNota.pack()
slider_nota = customtkinter.CTkSlider(janelaMain, from_=0, to=5, command=atualizar_valor_slider)
slider_nota.pack()
label_valor_slider = customtkinter.CTkLabel(janelaMain, text="Nota: 0.0")
label_valor_slider.pack()

# Input: Comentários
labelComentario = customtkinter.CTkLabel(janelaMain, text="Comentários")
labelComentario.pack()
entryComentario = customtkinter.CTkTextbox(janelaMain, height=100)
entryComentario.pack()

# Botão para cadastrar
botaoCadastrar = customtkinter.CTkButton(janelaMain, text="Cadastrar/Atualizar", command=cadastrar)
botaoCadastrar.pack(pady=25)

# Botão para apagar filme
botaoApagar = customtkinter.CTkButton(janelaMain, text="Apagar Filme", command=apagar_filme)
botaoApagar.pack(pady=10)

# Mensagem de retorno
retornoBotao = customtkinter.CTkLabel(janelaMain, text="")
retornoBotao.pack()

# Mostrar a tela em loop
janelaMain.mainloop()
