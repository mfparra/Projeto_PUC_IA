from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam
from keras.callbacks import CSVLogger


def setParametrosRNA(numeroRotulos):
    #onde está model.add(Dense(2, activation='softmax'))
    #O valor 2 é o número de classes
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=1, padding='same', activation='relu', input_shape=(256, 256, 1)))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=64, kernel_size=5, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=64, kernel_size=5, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=128, kernel_size=7, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    #model.add(Conv2D(filters=64, kernel_size=5, padding='same', activation='relu'))
    #model.add(MaxPooling2D())
    #model.add(Dropout(0.3))
    
    model.add(Flatten())
    #model.add(Dense(500, activation='relu'))
    #model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(numeroRotulos, activation='softmax'))
    model.summary()

    # compile the model
    #model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model


#Rede para um classificador Binário
#Usados para alguns dados 
def setParametrosRNAClassBinaria():
    #onde está model.add(Dense(2, activation='softmax'))
    #O valor 2 é o número de classes
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=1, padding='same', activation='relu', input_shape=(256, 256, 1)))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=64, kernel_size=5, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=64, kernel_size=5, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    #model.add(Dropout(0.3))
    
    model.add(Flatten())
    #model.add(Dense(500, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(8, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(2, activation='sigmoid'))
    model.summary()

    # compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', 'Precision'])
    return model


def treinoModelo(model, examesTrein, examesRotTrein, examesValid, examesRotValid, arquivoPesos, arquivoLog):
    # train the model
    checkpointer = ModelCheckpoint(filepath=arquivoPesos, verbose=1, save_best_only=True)
    #print(examesTrein)
    csvLog = CSVLogger(arquivoLog, append=True)
    hist = model.fit(examesTrein, examesRotTrein, batch_size=32, epochs=10,
            validation_data=(examesValid, examesRotValid), callbacks=[checkpointer], 
            verbose=2, shuffle=True)
    return model

def carregarModelo(model, arquivoPesos):
    model.load_weights(arquivoPesos)
    return model


def restauraDadosValidacao(model, examesValid, examesRotValid, arquivoPesos):
    model.load_weights(arquivoPesos)
    acuracia = model.evaluate(examesValid, examesRotValid, verbose=2)
    print("Acuracia do modelo: {}".format(acuracia[1]))


def avaliacaoModelo(model, examesTeste, examesRotTeste, arquivoPesos):
    model.load_weights(arquivoPesos)
    score = model.evaluate(examesTeste, examesRotTeste, verbose=2)
    return score

def printaImagensAcuracia(model, examesTeste, examesRotTeste, arquivoPesos):
    model.load_weights(arquivoPesos)
    predicao = model.predict(examesTeste)
    return predicao