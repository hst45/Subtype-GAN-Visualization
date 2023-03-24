tensorspacejs_converter \
  --input_model_from="keras" \
  --input_model_format="topology_weights_combined" \
  --output_layer_names="dense_7,dense_8,dense_9,dense_10,concatenate_1,dense_11,dense_12,dense_13,z" \
  /Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/models/BRCA.h5 \
  /Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/static/convertedModel/converted_brca

tensorspacejs_converter \
  --input_model_from="keras" \
  --input_model_format="topology_weights_combined" \
  --output_layer_names="Conv2D_1,MaxPooling2D_1,Conv2D_2,MaxPooling2D_2,Dense_1,Dense_2,Softmax" \
  /Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/mnist.h5 \
  /Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/static/convertedModel/converted_keras/

