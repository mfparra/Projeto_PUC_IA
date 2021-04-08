import matplotlib.pyplot as plt
from pydicom import dcmread
from os import walk
from os import path

from skimage.transform import resize





#Retorna todas as imagens pelo código do paciente
def retornaArquivosExames(pastaRaiz, UUID):
    vetorImagens = []
    for raiz, diretorios, arquivos in walk(pastaRaiz + UUID):
        for arq in arquivos:
            if(arq.endswith(".dcm")):
                vetorImagens.append(path.join(raiz, arq))
    return vetorImagens


#Recebe de entrada o vetor com os pacientes de treinamento
#Retorna dois vetores:
#Primeiro com os valores dos pixels dos exames
#Segundo com o paciente de cada exame
#Os dois vetores são relacionados no index
def retornaPixelsPaciente(pastaRaiz, vetorPacientes, tamanhoImagem):
    arquivosExames = []
    vetorPacienteExame = []
    exames = []
    examesRotuloPaciente = []
    
    for paciente in vetorPacientes:
        arquivosExames.append(retornaArquivosExames(pastaRaiz, paciente))
        vetorPacienteExame.append(paciente)

    for i, examePaciente in enumerate(arquivosExames):
        paciente = vetorPacienteExame[i]
        for exame in examePaciente:
            exameTemp = dcmread(exame)
            examePixel = exameTemp.pixel_array
            
            #Padroniza o tamanho da imagem
            exameRedimen = resize(examePixel,(tamanhoImagem, tamanhoImagem), anti_aliasing=True)
            
            #print(exameRedimen)
            exames.append(exameRedimen)
            examesRotuloPaciente.append(paciente)

    return (exames, examesRotuloPaciente)













#Retornar Imagens pelo código do TCGA
def retornaExamesPaciente(UUID):
    #Ler arquivo dcm
    imagem =dcmread(UUID)


    print(f"SOP Class........: {imagem.SOPClassUID} ({imagem.SOPClassUID.name})")

    nomePaciente = imagem.PatientName
    nomePacienteFormat = nomePaciente.family_name + ", " + nomePaciente.given_name
    print(f"Nome Paciente...: {nomePacienteFormat}")
    print(f"Paciente ID.......: {imagem.PatientID}")
    print(f"Modalidade.........: {imagem.Modality}")
    print(f"Data Estudo.......: {imagem.StudyDate}")
    print(f"Tamanho Imagem.......: {imagem.Rows} x {imagem.Columns}")
    print(f"Espaço Pixel....: {imagem.PixelSpacing}")

    # use .get() if not sure the item exists, and want a default value if missing
    print(f"Slice location...: {imagem.get('SliceLocation', '(missing)')}")

    # use .get() if not sure the item exists, and want a default value if missing
    print(f"Slice location...: {imagem.get('SliceLocation', '(missing)')}")

    #print(imagem)

    # plot the image using matplotlib
    #plt.imshow(imagem.pixel_array, cmap=plt.cm.gray)
    #plt.show()


def retornaDadosImagens(caminho):
    #Ler arquivo dcm
    imagem =dcmread(caminho)


    print(f"SOP Class........: {imagem.SOPClassUID} ({imagem.SOPClassUID.name})")

    nomePaciente = imagem.PatientName
    nomePacienteFormat = nomePaciente.family_name + ", " + nomePaciente.given_name
    print(f"Nome Paciente...: {nomePacienteFormat}")
    print(f"Paciente ID.......: {imagem.PatientID}")
    print(f"Modalidade.........: {imagem.Modality}")
    print(f"Data Estudo.......: {imagem.StudyDate}")
    print(f"Tamanho Imagem.......: {imagem.Rows} x {imagem.Columns}")
    print(f"Espaço Pixel....: {imagem.PixelSpacing}")

    # use .get() if not sure the item exists, and want a default value if missing
    print(f"Slice location...: {imagem.get('SliceLocation', '(missing)')}")

    # use .get() if not sure the item exists, and want a default value if missing
    print(f"Slice location...: {imagem.get('SliceLocation', '(missing)')}")

    print(imagem)

    # plot the image using matplotlib
    plt.imshow(imagem.pixel_array, cmap=plt.cm.gray)
    plt.show()