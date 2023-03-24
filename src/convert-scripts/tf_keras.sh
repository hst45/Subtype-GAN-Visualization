#tensorspacejs_converter \
#  --input_model_from="tensorflow" \
#  --input_model_format="tf_keras" \
#  --output_layer_names="dense_7,dense_8,dense_9,dense_10,concatenate_1,batch_normalization_2,activation_2,dense_11,dense_12,dense_13" \
#  /Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/BRCA.h5 \
#  /Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/static/convertedModel

tensorspacejs_converter \
  --input_model_from="tensorflow" \
  --input_model_format="tf_keras" \
  --output_layer_names="padding_1,conv_1,maxpool_1,conv_2,maxpool_2,dense_1,dense_2,softmax" \
  /Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/tf_keras_model.h5 \
  /Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/static/convertedModel


# --output_layer_names="Conv2D_1,MaxPooling2D_1,Conv2D_2,MaxPooling2D_2,Dense_1,Dense_2,Softmax" \