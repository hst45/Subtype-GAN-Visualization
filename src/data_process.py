import numpy as np

raw_data = [
                [0, 0.01, 0.04, 0.08, 0.09, 0.22, 0.27, 0.27, 0.37, 0.63, 1],
                [0.01, 0.04, 0.09, 0.19, 0.22, 0.42, 0.46, 0.48, 0.6, 1, 0.63],
                [0.04, 0.11, 0.22, 0.38, 0.42, 0.7, 0.79, 0.81, 1, 0.6, 0.37],
                [0.08, 0.18, 0.3, 0.48, 0.53, 0.88, 0.97, 1, 0.81, 0.48, 0.27],
                [0.08, 0.19, 0.3, 0.48, 0.55, 0.9, 1, 0.97, 0.79, 0.46, 0.27],
                [0.09, 0.22, 0.37, 0.55, 0.61, 1, 0.9, 0.88, 0.7, 0.42, 0.22],
                [0.22, 0.41, 0.61, 0.9, 1, 0.61, 0.55, 0.53, 0.42, 0.22, 0.09],
                [0.24, 0.45, 0.67, 1, 0.9, 0.55, 0.48, 0.48, 0.38, 0.19, 0.08],
                [0.42, 0.67, 1, 0.67, 0.61, 0.37, 0.3, 0.3, 0.22, 0.09, 0.04],
                [0.62, 1, 0.67, 0.45, 0.41, 0.22, 0.19, 0.18, 0.11, 0.04, 0.01],
                [1, 0.62, 0.42, 0.24, 0.22, 0.09, 0.08, 0.08, 0.04, 0.01, 0],
            ]

new_data = []
for sublist in raw_data:
    print(sublist)
    sublist.reverse()
    new_data.append(sublist)

print(new_data)
name = ['Subtype-GAN', 'NEMO', 'SNF', 'PINS', 'MCCA', 'VAE', 'Spectral', 'K-means', 'LRAcluster', 'iCluster', 'AE']
name.reverse()
print(name)


# import pandas as pd
# omics_data = [0.1861894447806495,
#               0.634567792822462,
#               0.15033345775881726,
#               0.028909304638071922,
#               0.184049649378174,
#               0.626708586105835,
#               0.1416002204894546,
#               0.04764154402653635,
#               0.23250418769531206,
#               0.5961725188585119,
#               0.13192783383657322,
#               0.03939545960960336,
#               0.22186162324409184,
#               0.6273621874264336,
#               0.1507761893294746,
#               0.0,
#               0.41711993034522044,
#               0.4562465152751982,
#               0.09966521158711031,
#               0.026968342792471695,
#               0.5442259508389833,
#               0.3630494345850781,
#               0.0735294003385325,
#               0.019195214237406253,
#               0.529663947446874,
#               0.36099640958049245,
#               0.08657984564816207,
#               0.02275979732447226,
#               0.546049790699804,
#               0.3531390362067014,
#               0.06479585239538471,
#               0.036015320698108665,
#               0.18932533540798024,
#               0.5878032902496055,
#               0.18403367842826723,
#               0.03883769591414693,
#               0.19984674099827468,
#               0.37655834427071244,
#               0.3887469035101353,
#               0.03484801122087759]
#
# Methylation = []
# mRNA = []
# CN = []
# miRNA = []
#
# for i in range(0, 40, 4):
#     Methylation.append(omics_data[i])
#     mRNA.append(omics_data[i+1])
#     CN.append(omics_data[i+2])
#     miRNA.append(omics_data[i+3])
#
# print(Methylation)
# print(mRNA)
# print(CN)
# print(miRNA)

# import os

# from keras.layers import Activation
# from keras.models import Model, load_model
# import tensorflow as tf
# import numpy as np
#
#
# class GeLU (Activation):
#     def __init__(self, activation, **kwargs):
#         super (GeLU, self).__init__ (activation, **kwargs)
#         self.__name__ = 'gelu'
#
# def gelu(x):
#     return 0.5 * x * (1 + tf.tanh (tf.sqrt (2 / np.pi) * (x + 0.044715 * tf.pow (x, 3))))
#
# model_path = "/Users/fxy/PycharmProjects/Subtype-GAN-vusualize/src/BRCA.h5"
# model = load_model(model_path, custom_objects={'GeLU': GeLU(gelu), 'gelu': GeLU(gelu)})
#
# json_string = model.to_json()
# print(json_string)

# import re
# data = []
# for line in open("/Users/fxy/Desktop/500points.txt"):
#     str_list = line.split()
#     num1 = re.findall(r"\d+\.?\d*",str_list[2])
#     num2 = re.findall(r"\d+\.?\d*",str_list[3])
#     data.append([float(num1[0]), float(num2[0])])
# print(len(data))
# print(data)