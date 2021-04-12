import TCGA as tcga


######Classe para padronização dos dados de entrada########


#Verifica se vetores de treino e teste não possuem dados
#em comum pela intersecção dos vetores
def verificaInputData(vetTrein, vetValid, vetTeste):
    if (len(set(vetTrein).intersection(vetValid)) == 0):
        return True
    else:
        raise Exception ("A intersecção dos vetores de treinamento e validação deve ser 0. "+
                        "O valor é {}".format(len(set(vetTrein).intersection(vetTeste))))

    if (len(set(vetValid).intersection(vetTeste)) == 0):
        return True
    else:
        raise Exception ("A intersecção dos vetores de validação e teste deve ser 0. "+
                        "O valor é {}".format(len(set(vetTrein).intersection(vetTeste))))

    if (len(set(vetTrein).intersection(vetTeste)) == 0):
        return True
    else:
        raise Exception ("A intersecção dos vetores de Treinamento e teste deve ser 0. "+
                        "O valor é {}".format(len(set(vetTrein).intersection(vetTeste))))




#Cria o rotulo do paciente para entrada na rede neural
#A entrada é o rotulo usado com as informações do TCGA e o vetor com o UUID
#Altera os rotulos de palavras para numéricos
#Retorna o vetor de rotulos com o indice dos exames
#E o vetor de rotulos com o valor do indice referente ao rotulo
def retornaRotulosOld(examesRotuloPac, rotulo):
    examesRotulo = []
    if (rotulo == "Stage"):
        #Cria o rotulo do paciente para entrada na rede neural
        for paciente in examesRotuloPac:
            examesRotulo.append(tcga.retornaPacienteDadoClinico(paciente, "Tratamento"))

    #Altera o valor do rótulo de uma String para um valor
    #de acordo com a posição do vetor examesRotulosUsados
    examesRotulosUsados = sorted(set(examesRotulo))
    examesRotuloTemp = []
    for rotulo in examesRotulo:
        examesRotuloTemp.append(examesRotulosUsados.index(rotulo))
    examesRotulo = examesRotuloTemp
    return (examesRotulo, examesRotulosUsados)


def retornaRotulos(examesRotuloPac, dadoClinico, examesRotulosUsados):
    examesRotulo = []
    
    for paciente in examesRotuloPac:
        examesRotulo.append(tcga.retornaPacienteDadoClinico(paciente, dadoClinico))
    

    examesRotuloTemp = []
    for rotulo in examesRotulo:
        examesRotuloTemp.append(examesRotulosUsados.index(rotulo))
    examesRotulo = examesRotuloTemp
    return examesRotulo

#Verifica se vetor de exames tem o mesmo tamanho do 
#vetor de rótulos
def verificaTamanhoExamesRotulos(exames, rotulosExames):
    if (len(exames) == len(rotulosExames)):
        return True
    else:
        raise Exception ("O tamanho do vetor de exames é: {}\n".format(len(exames))+
                        "O tamanho do vetor de rotulos de exames é {}".format(len(rotulosExames)))