import csv


    #for linha in csv.reader(tsv, dialect="excel-tab"):
    #    print(linha[1])


#dadosClinicos = open("Data_TCGA_BRCA/CasosClinicos/clinical.tsv", "r")
#print(dadosClinicos[2])

#Retorna os dados clínicos do Paciente pelo ID
def retornaPaciente(UUID):
    with open("Data_TCGA_BRCA/CasosClinicos/clinical.tsv") as tsv:
        linhasArquivo = csv.reader(tsv, dialect="excel-tab")
        for i, linha in enumerate(csv.reader(tsv, dialect="excel-tab")):
            if (i % 2 != 0):
                if (linha[1]==UUID):
                    pacienteID = linha[1]
                    idade = linha[3]
                    etnia = linha[10]
                    genero = linha[11]
                    raca = linha[14]
                    vital = linha[15]

                    ###Abaixo estão as descrições dos dados#######

                    #In the TNM system:
                    #The T refers to the size and extent of the main
                    #tumor. The main tumor is usually called the primary tumor.
                    #The N refers to the the number of nearby lymph nodes that
                    #have cancer.
                    #The M refers to whether the cancer has metastasized. This
                    #means that the cancer has spread from the primary tumor to
                    #other parts of the body.
                    #Fonte:https://www.cancer.gov/about-cancer/diagnosis-staging/staging


                    #Distant metastasis (M)
                    #MX: Metastasis cannot be measured.
                    #M0: Cancer has not spread to other parts of the body.
                    #M1: Cancer has spread to other parts of the body.
                    ajccPatM = linha[24]

                    #Regional lymph nodes (N)
                    #NX: Cancer in nearby lymph nodes cannot be measured.
                    #N0: There is no cancer in nearby lymph nodes.
                    #N1, N2, N3: Refers to the number and location of lymph nodes 
                    #that contain cancer. The higher the number after the N, the 
                    #more lymph nodes that contain cancer.
                    ajccPatN = linha[25]

                    #Stage
                    #Stage 0: Abnormal cells are present but have not spread to 
                    #nearby tissue. Also called carcinoma in situ, or CIS. CIS is
                    #not cancer, but it may become cancer.
                    #Stage I, Stage II, and Stage III: Cancer is present. The
                    #higher the number, the larger the cancer tumor and the more
                    #it has spread into nearby tissues.
                    #Stage IV: The cancer has spread to distant parts of the body.
                    ajccPatStage = linha[26]


                    #Primary tumor (T)
                    #TX: Main tumor cannot be measured.
                    #T0: Main tumor cannot be found.
                    #T1, T2, T3, T4: Refers to the size and/or extent of the main
                    #tumor. The higher the number after the T, the larger the tumor
                    #or the more it has grown into nearby tissues. T's may be
                    #further divided to provide more detail, such as T3a and T3b.
                    ajccPatT = linha[27]

                    primaryDiagnosis = linha[107]


                    priorMalignancy = linha[109]
                    priorTreatment = linha[110]

                    tumorStage = linha[127]

                    tratamento = linha[151]
                    tipoTratamento = linha[153]

                    if(raca == "black or african american"):
                        raca = "black"
                    elif(raca == "not reported"):
                        raca = "white"
                    print(pacienteID, "|", idade, "|", etnia, "|", genero, "|", raca, "|", ajccPatT, "|",ajccPatM, "|",ajccPatN, "|",ajccPatStage, "|",primaryDiagnosis
                            , "|", tumorStage, "|", tratamento, "|", tipoTratamento)

                    #print(linha)

def retornaPacienteStage(UUID):
    with open("Data_TCGA_BRCA/CasosClinicos/clinical.tsv") as tsv:
        linhasArquivo = csv.reader(tsv, dialect="excel-tab")
        for i, linha in enumerate(csv.reader(tsv, dialect="excel-tab")):
            if (i % 2 != 0):
                if (linha[1]==UUID):
                    ajccPatStage = linha[26]
    return(ajccPatStage)




                