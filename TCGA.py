import csv


    #for linha in csv.reader(tsv, dialect="excel-tab"):
    #    print(linha[1])


#dadosClinicos = open("Data_TCGA_BRCA/CasosClinicos/clinical.tsv", "r")
#print(dadosClinicos[2])

#Retorna os dados clínicos do Paciente pelo ID
def retornaPaciente(UUID):
    with open("clinical.tsv") as tsv:
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

                    #Primary Diagnosis
                    #Infiltrating duct carcinoma, NOS
                    #Lobular carcinoma, NOS
                    #Infiltrating duct and lobular carcinoma
                    #Infiltrating duct mixed with other types of carcinoma
                    primaryDiagnosis = linha[107]


                    priorMalignancy = linha[109]
                    priorTreatment = linha[110]

                    tumorStage = linha[127]

                    #Binário: sim / não
                    tratamento = linha[151]
                    
                    #Pharmaceutical / Radiation
                    tipoTratamento = linha[153]

                    #Correção dos dados de raça
                    if(raca == "black or african american"):
                        raca = "black"
                    elif(raca == "not reported"):
                        raca = "black"
                    print(pacienteID, "|", idade, "|", etnia, "|", genero, "|", raca, "|", ajccPatT, "|",ajccPatM, "|",ajccPatN, "|",ajccPatStage, "|",primaryDiagnosis
                            , "|", tumorStage, "|", tratamento, "|", tipoTratamento)
                    

                    #Correção dos dados de Stage
                    if(ajccPatStage == "Stage IA"):
                        ajccPatStage = "Stage I"
                    elif(ajccPatStage == "Stage IB"):
                        ajccPatStage = "Stage I"
                    elif(ajccPatStage == "Stage IC"):
                        ajccPatStage = "Stage I"
                    elif(ajccPatStage == "Stage IIA"):
                        ajccPatStage = "Stage II"
                    elif(ajccPatStage == "Stage IIB"):
                        ajccPatStage = "Stage II"
                    elif(ajccPatStage == "Stage IIC"):
                        ajccPatStage = "Stage II"
                    elif(ajccPatStage == "Stage IIIA"):
                        ajccPatStage = "Stage III"
                    elif(ajccPatStage == "Stage IIIB"):
                        ajccPatStage = "Stage III"
                    elif(ajccPatStage == "Stage IIIC"):
                        ajccPatStage = "Stage III"


                    #Correção dados Primary tumor (T)
                    if(ajccPatT == "T1a"):
                        ajccPatT = "T1"
                    elif(ajccPatT == "T1b"):
                        ajccPatT = "T1"
                    elif(ajccPatT == "T1c"):
                        ajccPatT = "T1"

                    #Correção Distant metastasis (M)
                    if(ajccPatM == "cM0 (i+)"):
                        ajccPatM = "M0"

                    #Correção Regional lymph nodes (N)
                    if(ajccPatN == "N0 (i-)"):
                        ajccPatN = "N0"
                    elif(ajccPatN == "N0 (i+)"):
                        ajccPatN = "N0"
                    elif(ajccPatN == "N1a"):
                        ajccPatN = "N1"
                    elif(ajccPatN == "N1b"):
                        ajccPatN = "N1"
                    elif(ajccPatN == "N1mi"):
                        ajccPatN = "N1"
                    elif(ajccPatN == "N2a"):
                        ajccPatN = "N2"
                    elif(ajccPatN == "N3a"):
                        ajccPatN = "N3"
                    


                    #print(linha)

def retornaPacienteDadoClinico(UUID, dadoClinico):
    with open("clinical.tsv") as tsv:
        linhasArquivo = csv.reader(tsv, dialect="excel-tab")
        for i, linha in enumerate(csv.reader(tsv, dialect="excel-tab")):
            if (i % 2 != 0):
                if (linha[1]==UUID):
                    if (dadoClinico == "Distant metastasis"):
                        #Distant metastasis (M)
                        #MX: Metastasis cannot be measured.
                        #M0: Cancer has not spread to other parts of the body.
                        #M1: Cancer has spread to other parts of the body.
                        dadoPaciente = linha[24]

                        #Correção Distant metastasis (M)
                        if(dadoPaciente == "cM0 (i+)"):
                            dadoPaciente = "M0"
                    
                    elif (dadoClinico == "Regional lymph nodes"):
                        #Regional lymph nodes (N)
                        #NX: Cancer in nearby lymph nodes cannot be measured.
                        #N0: There is no cancer in nearby lymph nodes.
                        #N1, N2, N3: Refers to the number and location of lymph nodes 
                        #that contain cancer. The higher the number after the N, the 
                        #more lymph nodes that contain cancer.
                        dadoPaciente = linha[25]

                        #Correção Regional lymph nodes (N)
                        if(dadoPaciente == "N0 (i-)"):
                            dadoPaciente = "N0"
                        elif(dadoPaciente == "N0 (i+)"):
                            dadoPaciente = "N0"
                        elif(dadoPaciente == "N1a"):
                            dadoPaciente = "N1"
                        elif(dadoPaciente == "N1b"):
                            dadoPaciente = "N1"
                        elif(dadoPaciente == "N1mi"):
                            dadoPaciente = "N1"
                        elif(dadoPaciente == "N2a"):
                            dadoPaciente = "N2"
                        elif(dadoPaciente == "N3a"):
                            dadoPaciente = "N3"

                    elif (dadoClinico == "Primary tumor"):
                        #Primary tumor (T)
                        #TX: Main tumor cannot be measured.
                        #T0: Main tumor cannot be found.
                        #T1, T2, T3, T4: Refers to the size and/or extent of the main
                        #tumor. The higher the number after the T, the larger the tumor
                        #or the more it has grown into nearby tissues. T's may be
                        #further divided to provide more detail, such as T3a and T3b.
                        dadoPaciente = linha[27]

                        #Correção dados Primary tumor (T)
                        if(dadoPaciente == "T1a"):
                            dadoPaciente = "T1"
                        elif(dadoPaciente == "T1b"):
                            dadoPaciente = "T1"
                        elif(dadoPaciente == "T1c"):
                            dadoPaciente = "T1"

                    
                    elif (dadoClinico == "Stage"):
                        dadoPaciente = linha[26]

                        #Correção dos dados de Stage
                        if(dadoPaciente == "Stage IA"):
                            dadoPaciente = "Stage I"
                        elif(dadoPaciente == "Stage IB"):
                            dadoPaciente = "Stage I"
                        elif(dadoPaciente == "Stage IC"):
                            dadoPaciente = "Stage I"
                        elif(dadoPaciente == "Stage IIA"):
                            dadoPaciente = "Stage II"
                        elif(dadoPaciente == "Stage IIB"):
                            dadoPaciente = "Stage II"
                        elif(dadoPaciente == "Stage IIC"):
                            dadoPaciente = "Stage II"
                        elif(dadoPaciente == "Stage IIIA"):
                            dadoPaciente = "Stage III"
                        elif(dadoPaciente == "Stage IIIB"):
                            dadoPaciente = "Stage III"
                        elif(dadoPaciente == "Stage IIIC"):
                            dadoPaciente = "Stage III"
                    
                    elif (dadoClinico == "Tratamento"):
                        #Binário: sim / não
                        dadoPaciente = linha[151]

                    elif (dadoClinico == "tipoTratamento"):
                        #Pharmaceutical / Radiation
                        dadoPaciente = linha[153]
    return(dadoPaciente)




                