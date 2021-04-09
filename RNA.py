from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.callbacks import ModelCheckpoint


def setParametrosRNA():
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
    model.add(Dropout(0.3))
    
    model.add(Flatten())
    #model.add(Dense(500, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(8, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(5, activation='softmax'))
    model.summary()

    # compile the model
    #model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy', 'Precision', 'Recall'])

    return model


def treinoModelo(model, examesTrein, examesRotTrein, examesValid, examesRotValid):
    # train the model
    checkpointer = ModelCheckpoint(filepath='pesos_rede_neural.hdf5', verbose=1, save_best_only=True)
    #print(examesTrein)
    hist = model.fit(examesTrein, examesRotTrein, batch_size=32, epochs=10,
            validation_data=(examesValid, examesRotValid), callbacks=[checkpointer], 
            verbose=2, shuffle=True)
    return model

def carregarModelo(model):
    model.load_weights('pesos_rede_neural.hdf5')
    return model

def avaliacaoModelo(model, examesTeste, examesRotTeste):
    score = model.evaluate(examesTeste, examesRotTeste, verbose=0)
    return score