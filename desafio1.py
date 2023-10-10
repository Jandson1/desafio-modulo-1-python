#Função que recebe a votação do personagem
def votacao():
    votos = []

    for i in range(5):
        voto = int(input("Digite o voto para o seu personagem favorito(1 - Bart | 2 - Homer): "))
        if voto == 1 or voto == 2:
            votos.append(voto)
        else:
            votos.append(0)
    return votos

#Função que conta os votos e atribui os resultados
def resultados(votos):
    votosBart = votos.count(1)
    votosHomer = votos.count(2)
    votosNulos = votos.count(0)

    if votosBart > votosHomer:
        favorito = "Bart"
        votosMais = votosBart
        menosVotado = "Homer"
        votosMenos = votosHomer
    elif votosHomer > votosBart:
        favorito = "Homer"
        votosMais = votosHomer
        menosVotado = "Bart"
        votosMenos = votosBart
    else:
        favorito = menosVotado = "Empate"
        votosMais = votosMenos = votosHomer
    
    return favorito, votosMais, menosVotado, votosMenos, votosNulos

#Função para mostrar os resultados
def mostra_resultado(favorito, votosMais, menosVotado, votosMenos, votosNulos):
    print(f"O personagem favorito foi {favorito} com {votosMais} votos.")
    print(f"O personagem menos votado foi {menosVotado} com {votosMenos} votos.")
    print(f"Votos nulos: {votosNulos}")

#Função principal
def main():
    votos = votacao()
    favorito, votosMais, menosVotado, votosMenos, votosNulos = resultados(votos)
    mostra_resultado(favorito, votosMais, menosVotado, votosMenos, votosNulos)

main()