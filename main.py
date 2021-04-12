import TCGA as tcga
import TCIA as tcia
import DadosEntrada as entrada
import RNA as rna
import pickle
import random

#import cv2
from matplotlib import pyplot as plt
from matplotlib import rcParams
from pydicom import dcmread
from os import walk
from os import path
from os import listdir
import numpy as np


import keras
from keras.utils import np_utils
 

#Remover paciente TCGA-EW-A1J2
#138 pacientes


#Parâmetros
#pastaRaiz = "/media/marcos/Dropbox/Dropbox/MultiLinguagens/Projeto_PUC_IA/Data_TCGA_BRCA/MiniData/"
#pastaRaiz = "/media/marcos/Games2/TCGA-BRCA_image_mini/"
pastaRaiz = "/media/marcos/Games2/TCGA-BRCA_image/"
tamanhoImagem = 256

#Para rodar completo:
#Distant metastasis
#Tratamento
#Primary tumor
#Regional lymph nodes

#Stage | Distant metastasis | Regional lymph nodes | Primary tumor | Tratamento | tipoTratamento
dadoClinico = "Regional lymph nodes"

#Salva os arquivos da Rede Neural
pastaRedeNeural = "ArquivosRedesNeurais/"
arquivoPesosRedeNeural = pastaRedeNeural + dadoClinico + "_pesos_rede_neural.hdf5"
arquivoListaTreinamento = pastaRedeNeural + dadoClinico + "_Lista_Treinamento"
arquivoListaValidacao = pastaRedeNeural + dadoClinico + "_Lista_Validacao"
arquivoListaTeste = pastaRedeNeural + dadoClinico + "_Lista_Teste"
arquivoSaidaTreinamento = pastaRedeNeural + dadoClinico + "_saida_Treinamento.csv"




###########Rótulos para cada dado usado:#########################
examesRotulosUsados = []


if (dadoClinico == "Stage"):
    examesRotulosUsados = ["Stage 0", "Stage I", "Stage II", "Stage III", "Stage IV",]
elif (dadoClinico == "Distant metastasis"):
    examesRotulosUsados = ["M0", "M1", "MX"]
elif (dadoClinico == "Regional lymph nodes"):
    examesRotulosUsados = ["N0", "N1", "N2", "N3", "NX"]
elif (dadoClinico == "Primary tumor"):
    examesRotulosUsados = ["T0", "T1", "T2", "T3", "T4", "TX"]

#Binários
elif (dadoClinico == "Tratamento"):
    examesRotulosUsados = ["no", "yes"]
elif (dadoClinico == "tipoTratamento"):
    examesRotulosUsados = ["Pharmaceutical Therapy, NOS", "Radiation Therapy, NOS"]


#tcia.retornaDadosImagens("/media/marcos/Games2/TCGA-BRCA_image/TCGA-AO-A0JM/2.000000-T2 left breast-17307/1-24.dcm")

#tcia.retornaExamesPaciente("TCGA-AO-A0JM")

#print(listdir(path="/media/marcos/Games2/TCGA-BRCA_image/TCGA-AO-A0JM/."))

#tcga.retornaPaciente("TCGA-AO-A0JI")

#for paciente in listdir(pastaRaiz):
#    tcia.retornaArquivosExames(pastaRaiz, paciente)





def executaTreinamento(dadoClinico, examesRotulosUsados, arquivoPesosRedeNeural, arquivoSaidaTreinamento):
    #Usado 3 pacientes para treinamento e 1 para teste
    vetorPaciente=listdir(pastaRaiz)
    random.shuffle(vetorPaciente)
    trein = int(len(vetorPaciente)*0.6)
    valid = int(len(vetorPaciente)*0.2 + trein)
    teste = int(len(vetorPaciente)*0.2 + trein + valid)

    vetorPacienteTrein = []
    vetorPacienteValid = []
    vetorPacienteTeste = []

    for i, paciente in enumerate(vetorPaciente):
        if (i + 1 <= trein):
            vetorPacienteTrein.append(paciente)
        elif (i + 1 <= valid):
            vetorPacienteValid.append(paciente)
        else:
            vetorPacienteTeste.append(paciente)


    print("Treinamento: ", vetorPacienteTrein)
    print("Validação: ", vetorPacienteValid)
    print("Teste: ", vetorPacienteTeste)
    print("Rótulos usados : {}".format(examesRotulosUsados))

    ###Salva os aquivos dos vetores da rede neural
    with open(arquivoListaTreinamento, "wb") as arquivo:
        pickle.dump(vetorPacienteTrein, arquivo)

    with open(arquivoListaValidacao, "wb") as arquivo:
        pickle.dump(vetorPacienteValid, arquivo)

    with open(arquivoListaTeste, "wb") as arquivo:
        pickle.dump(vetorPacienteTeste, arquivo)
    
    
    #Verifica se o vetor não possui algum paciente igual
    try:
        entrada.verificaInputData(vetorPacienteTrein, vetorPacienteValid, vetorPacienteTeste)
    except ValueError as e:
        print(e)



    #Dados Treinamento
    (examesTrein, examesRotuloPacTrein) = tcia.retornaPixelsPaciente(pastaRaiz, vetorPacienteTrein, tamanhoImagem)
    examesRotTrein = entrada.retornaRotulos(examesRotuloPacTrein, dadoClinico, examesRotulosUsados)
    

    (examesValid, examesRotuloPacValid) = tcia.retornaPixelsPaciente(pastaRaiz, vetorPacienteValid, tamanhoImagem)
    examesRotValid = entrada.retornaRotulos(examesRotuloPacValid, dadoClinico, examesRotulosUsados)




    #print(examesRotTrein)
    #print(examesRotValid)
    #print(examesRotTeste)

    #Verifica o tamanho dos vetores de exames e rotulos
    try:
        entrada.verificaTamanhoExamesRotulos(examesTrein, examesRotTrein)
    except ValueError as e:
        print(e)

    try:
        entrada.verificaTamanhoExamesRotulos(examesValid, examesRotValid)
    except ValueError as e:
        print(e)


    #for exames in examesTrein:
    #    print(len(exames))



    examesTrein = np.array(examesTrein)
    examesRotTrein = np.array(examesRotTrein)
    examesValid = np.asarray(examesValid)
    examesRotValid = np.array(examesRotValid)



    examesTrein = np.float32(examesTrein)
    examesValid = np.float32(examesValid)



    examesRotTrein = keras.utils.to_categorical(examesRotTrein, len(examesRotulosUsados))
    examesRotValid = keras.utils.to_categorical(examesRotValid, len(examesRotulosUsados))



    examesTrein = examesTrein.astype("float32")/255
    examesValid = examesValid.astype("float32")/255




    print(examesTrein.shape)
    print(examesValid.shape)


    #plt.imshow(examesTrein[550], cmap=plt.cm.gray)
    #plt.show()


    if (len(examesRotulosUsados) == 2):
        modelo = rna.setParametrosRNAClassBinaria()
    elif (len(examesRotulosUsados) > 2):
        modelo = rna.setParametrosRNA(len(examesRotulosUsados))

    modelo = rna.treinoModelo(modelo, examesTrein, examesRotTrein, examesValid, examesRotValid, arquivoPesosRedeNeural, arquivoSaidaTreinamento)




def executaValidacao(arquivoListaValidacao, examesRotulosUsados, arquivoPesosRedeNeural):
    with open(arquivoListaValidacao, "rb") as arquivo:
        vetorPacienteValid = pickle.load(arquivo)

    (examesValid, examesRotuloPacValid) = tcia.retornaPixelsPaciente(pastaRaiz, vetorPacienteValid, tamanhoImagem)
    examesRotValid = entrada.retornaRotulos(examesRotuloPacValid, dadoClinico, examesRotulosUsados)

    examesValid = np.asarray(examesValid)
    examesRotValid = np.array(examesRotValid)
    examesValid = np.float32(examesValid)
    examesRotValid = keras.utils.to_categorical(examesRotValid, len(examesRotulosUsados))
    examesValid = examesValid.astype("float32")/255

    if (len(examesRotulosUsados) == 2):
        modelo = rna.setParametrosRNAClassBinaria()
    elif (len(examesRotulosUsados) > 2):
        modelo = rna.setParametrosRNA(len(examesRotulosUsados))

    modelo = rna.carregarModelo(modelo, arquivoPesosRedeNeural)

    rna.restauraDadosValidacao(modelo, examesValid, examesRotValid, arquivoPesosRedeNeural)


def executaTeste(arquivoVetorTeste, dadoClinico, examesRotulosUsados, arquivoPesosRedeNeural):
    with open(arquivoVetorTeste, "rb") as arquivo:
        vetorPacienteTeste = pickle.load(arquivo)
    
    (examesTeste, examesRotuloPacTeste) = tcia.retornaPixelsPaciente(pastaRaiz, vetorPacienteTeste, tamanhoImagem)
    examesRotTeste = entrada.retornaRotulos(examesRotuloPacTeste, dadoClinico, examesRotulosUsados)

    try:
        entrada.verificaTamanhoExamesRotulos(examesTeste, examesRotTeste)
    except ValueError as e:
        print(e)


    examesTeste = np.array(examesTeste)
    examesRotTeste = np.array(examesRotTeste)
    examesTeste = np.float32(examesTeste)

    examesRotTeste = keras.utils.to_categorical(examesRotTeste, len(examesRotulosUsados))

    examesTeste = examesTeste.astype("float32")/255
    print(examesTeste.shape)

    if (len(examesRotulosUsados) == 2):
        modelo = rna.setParametrosRNAClassBinaria()
    elif (len(examesRotulosUsados) > 2):
        modelo = rna.setParametrosRNA(len(examesRotulosUsados))
    
    
    #modelo = rna.carregarModelo(modelo, arquivoPesosRedeNeural)

    score = rna.avaliacaoModelo(modelo, examesTeste, examesRotTeste, arquivoPesosRedeNeural)
    print("Acurácia: ", score[1])
    print(score)
    

def exibeImagensTeste(arquivoVetorTeste, dadoClinico, examesRotulosUsados, arquivoPesosRedeNeural):
    with open(arquivoVetorTeste, "rb") as arquivo:
        vetorPacienteTeste = pickle.load(arquivo)
    
    (examesTeste, examesRotuloPacTeste) = tcia.retornaPixelsPaciente(pastaRaiz, vetorPacienteTeste, tamanhoImagem)
    examesRotTeste = entrada.retornaRotulos(examesRotuloPacTeste, dadoClinico, examesRotulosUsados)

    try:
        entrada.verificaTamanhoExamesRotulos(examesTeste, examesRotTeste)
    except ValueError as e:
        print(e)


    examesTeste = np.array(examesTeste)
    examesRotTeste = np.array(examesRotTeste)
    examesTeste = np.float32(examesTeste)

    examesRotTeste = keras.utils.to_categorical(examesRotTeste, len(examesRotulosUsados))

    examesTeste = examesTeste.astype("float32")/255
    print(examesTeste.shape)

    if (len(examesRotulosUsados) == 2):
        modelo = rna.setParametrosRNAClassBinaria()
    elif (len(examesRotulosUsados) > 2):
        modelo = rna.setParametrosRNA(len(examesRotulosUsados))
    
    

    predicao = rna.printaImagensAcuracia(modelo, examesTeste, examesRotulosUsados, arquivoPesosRedeNeural)
    fig = plt.figure(figsize=(20, 8))
    for i, idx in enumerate(np.random.choice(examesTeste.shape[0], size=32, replace=False)):
        ax = fig.add_subplot(4, 8, i + 1, xticks=[], yticks=[])
        ax.imshow(np.squeeze(examesTeste[idx]), cmap=plt.cm.gray)
        pred_idx = np.argmax(predicao[idx])
        true_idx = np.argmax(examesRotTeste[idx])
        ax.set_title("{} ({})".format(examesRotulosUsados[pred_idx], examesRotulosUsados[true_idx]),
                    color=("green" if pred_idx == true_idx else "red"))
    plt.show()
    #modelo = rna.carregarModelo(modelo, arquivoPesosRedeNeural)

    #score = rna.avaliacaoModelo(modelo, examesTeste, examesRotTeste, arquivoPesosRedeNeural)
    #print("Acurácia: ", score[1])
    #print(score)



#executaTreinamento(dadoClinico, examesRotulosUsados, arquivoPesosRedeNeural, arquivoSaidaTreinamento)

#Recuperar dados de validação do treinamento
#executaValidacao(arquivoListaValidacao, examesRotulosUsados, arquivoPesosRedeNeural)

#executaTeste(arquivoListaTeste, dadoClinico, examesRotulosUsados, arquivoPesosRedeNeural)

exibeImagensTeste(arquivoListaTeste, dadoClinico, examesRotulosUsados, arquivoPesosRedeNeural)









