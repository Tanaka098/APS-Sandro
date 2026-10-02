def cabecalho():
     head = open("Curriculo.html", 'w', encoding='utf-8')
     head.write('''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Curriculo</title>
</head>
<style>
     h1{
          text-align: center;
          font-size: 35px;
          font-family: 'Times New Roman', Times, serif;
     }
     h3{
          text-align: left;
          font-size: 25px;
          font-family: 'Times New Roman', Times, serif;         
     }
     .Subtitulo{
          text-align: center;
          font-size: 20px;
          font-family: 'Times New Roman', Times, serif;
          font-weight: normal;
          color: white;
          background-color: rgb(0, 0, 110);
          border-radius: 20px;
     }
     .dados {
          text-align: left;
          font-size: 20px;
          font-family: 'Times New Roman', Times, serif;
          font-weight: normal;
     }

</style>
<body>

<h1>Currículo Vitae</h1>

''')
def dados_pessoais():
     info_pessoal = open("Curriculo.html", 'a', encoding='utf-8')
     nome = input("Nome:")
     idade = input("Idade:")
     endereco = input("Endereço:")
     telefone = input("Telefone:")
     email = input("E-mail:")
     info_pessoal.write (f'''
<h2 class="Subtitulo">Dados Pessoais</h2>
<h3>Nome:{nome}</h3>
<p class="dados">Idade:{idade} anos</p>
<p class="dados">Telefone:{telefone}</p>
<p class="dados">E-mail:{email}</p>
''')
     info_pessoal.close()

def idiomas():
     idiomas = open('Curriculo.html', 'a', encoding='utf-8')
     resposta = 'S'
     idiomas.write(f'''
<h2 class="Subtitulo">Idiomas</h2>
''')
     while resposta.upper() == 'S':
          idioma = input("Idiomas:")
          fluencia = input("Nível de proficiência:")
          idiomas.write (f'''
<p class="dados">{idioma} - {fluencia}</p>
                    ''')
          resposta = input("Deseja adicionar outro idioma (S/N):")
     idiomas.close()

def dados_profissional():
     info_profissional = open("Curriculo.html", 'a', encoding='utf-8')
     info_profissional.write(f'''
<h2 class="Subtitulo">Experiência profissional</h2>''')
     resposta = 'S'
     while resposta.upper() == 'S':
          empresa = input("Empresa:")
          funcao = input("Função:")
          data_inicio = input("Data de ínicio:")
          data_fim = input("Data de saída:")
          info_profissional.write(f'''
<p class="dados">Empresa:{empresa}</p>
<p class="dados">Função:{funcao}</p>
<p class="dados">De {data_inicio} até {data_fim}</p>
''')
          resposta = input("Deseja adicionar outra experiência (S/N): ")
     info_profissional.close()

def escolaridade():
     escolaridade = open("Curriculo.html", 'a', encoding='utf-8')
     escolaridade.write(f'''
<h2 class="Subtitulo">Escolaridade</h2>''')
     resposta = 'S'
     while resposta.upper() == 'S':
          escola = input("Instituição de ensino:")
          curso = input("Curso:")
          duracao = input("Duracao:")
          escolaridade.write(f'''
<p class="dados">{escola}</p>
<p class="dados">{curso}</p>
<p class="dados">{duracao}</p>
''')
          resposta = input("Deseja adicionar outra formação (S/N): ")
     escolaridade.write('''
</body>
</html>
''')
     escolaridade.close()
     
cabecalho()
dados_pessoais()
dados_profissional()
idiomas()
escolaridade()