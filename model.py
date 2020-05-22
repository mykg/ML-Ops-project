from keras.applications import VGG16
model = VGG16(weights='imagenet', include_top=False, input_shape=(64, 64, 3))

model.layers[0].input


for layer in model.layers:
layer.trainable = False

model.output

top_model = model.output

from keras.models import Sequential

from keras.layers import Dense, Flatten, Activation

top_model = Flatten()(top_model)
n1=300
n2=200
top_model = Dense(n1, activation='relu')(top_model)
#addlayerhere
top_model = Dense(n2, activation='relu')(top_model)
top_model = Dense(6, activation='softmax')(top_model)

from keras.models import Model

model.input

top_model

newmodel = Model(inputs=model.input, outputs=top_model)

from keras.preprocessing.image import ImageDataGenerator

train_data_dir = '/root/model/seg_train/seg_train/'
validation_data_dir = '/root/model/seg_test/seg_test/'

train_datagen = ImageDataGenerator(
rescale=1./255,
rotation_range=20,
width_shift_range=0.2,
height_shift_range=0.2,
horizontal_flip=True,
fill_mode='nearest')

validation_datagen = ImageDataGenerator(rescale=1./255)

# Change the batchsize according to your system RAM
train_batchsize=16
val_batchsize=10

train_generator = train_datagen.flow_from_directory(
train_data_dir,
target_size=(64, 64),
batch_size=train_batchsize,
class_mode='categorical')

validation_generator = validation_datagen.flow_from_directory(
validation_data_dir,
target_size=(64, 64),
batch_size=val_batchsize,
class_mode='categorical',
shuffle=False)

from keras.optimizers import RMSprop

newmodel.compile(loss = 'categorical_crossentropy',
optimizer = RMSprop(lr = 0.001),
metrics = ['accuracy'])

nb_train_samples=1500
nb_validation_samples=200
epochs_x=3
batch_size_x=40

import sys
orig_stdout=sys.stdout
f=open("/root/model/output.txt",'w')
sys.stdout=f

history = newmodel.fit_generator(
train_generator,
steps_per_epoch = nb_train_samples // batch_size_x,
epochs = epochs_x,
validation_data = validation_generator,
validation_steps = nb_validation_samples // batch_size_x)

"""history = newmodel.fit_generator(
train_generator,
epochs = epochs,
validation_data = validation_generator)"""

sys.stdout=orig_stdout
f.close()

newmodel.save('seg_vgg.h5')
