# -*- coding: utf-8 -*-
"""Monitoring.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1REvGZ2DlynuXvuxbJzL6aVbTmr-w_gDK
"""

import cv2
import numpy as np
from numpy.linalg import norm
import keras 
import tensorflow as tf

base_features = [0.03915184,
 0.013195981,
 0.027549112,
 0.8607302,
 0.1109071,
 0.0032494182,
 0.08625528,
 0.32634592,
 0.029210793,
 0.17364223,
 0.43175665,
 0.020937495,
 0.59847903,
 0.0,
 0.003208762,
 0.55149275,
 0.09706237,
 0.721114,
 0.01751454,
 0.2071178,
 0.0384623,
 0.024567971,
 0.20676605,
 0.18372466,
 0.011446872,
 0.01904445,
 0.68443185,
 0.3667861,
 0.44036722,
 0.010041509,
 0.09579524,
 3.5704877,
 0.5961673,
 0.9569764,
 2.6899402,
 0.1689937,
 7.094484,
 0.026872685,
 0.13783644,
 0.019943094,
 0.035713356,
 0.017425017,
 0.51310384,
 0.82492036,
 0.10886457,
 0.33276305,
 0.3278915,
 0.70554376,
 0.011344768,
 0.15917754,
 0.19256361,
 0.05121092,
 0.4202917,
 0.059851486,
 0.14295886,
 4.9946604,
 1.0540873,
 0.07656163,
 0.065708704,
 0.7444903,
 0.023718111,
 0.024162723,
 0.14118396,
 2.1618586,
 0.0,
 0.30093506,
 0.035507154,
 0.6277181,
 0.06348739,
 0.041781995,
 0.0083355615,
 0.33324674,
 0.44746795,
 0.7212487,
 0.0065597934,
 0.0069385604,
 8.269691,
 0.39001358,
 0.00032137183,
 0.1647984,
 0.007900528,
 0.026775464,
 0.48895773,
 0.18467408,
 0.74383634,
 0.03526317,
 0.0565,
 0.27917078,
 0.060362395,
 0.96090984,
 0.0011635233,
 0.01995012,
 0.14816253,
 0.08776745,
 0.029733116,
 0.3667306,
 0.011289208,
 2.8280728,
 0.24079512,
 1.1739837,
 0.70863146,
 0.11879598,
 0.15769626,
 0.6105102,
 0.057439346,
 0.0,
 0.54263824,
 0.05286457,
 1.2608701,
 5.853935,
 0.2729598,
 0.09975902,
 0.19249701,
 0.8380378,
 0.01314953,
 0.0121967355,
 1.4474701,
 1.9036646,
 0.03997679,
 1.7757257,
 0.026547035,
 0.0,
 0.038270608,
 3.5145485,
 0.10724745,
 1.2321529,
 0.0,
 0.0,
 0.30419242,
 0.29168466,
 0.0,
 0.023512304,
 0.011852519,
 0.050682187,
 0.16616707,
 0.021857897,
 0.35361755,
 0.13018106,
 0.20759766,
 1.0721426,
 0.035037246,
 0.15751272,
 0.004600581,
 1.7061054,
 0.11562412,
 0.08961592,
 0.63506645,
 0.0018971087,
 0.7250695,
 1.1827271,
 0.933805,
 0.0039661787,
 3.048829,
 0.048051614,
 0.2487645,
 3.2782412,
 0.09503504,
 1.8093029,
 0.014858519,
 1.0972639,
 0.6930561,
 1.2340341e-05,
 0.0011919677,
 0.7188361,
 0.24509685,
 0.030242508,
 0.7184148,
 0.0,
 1.5697829,
 0.10808271,
 0.1403281,
 0.106051765,
 3.0331686,
 0.24683177,
 0.05941399,
 0.9159775,
 0.075858794,
 0.09877536,
 0.05390202,
 0.8128225,
 0.23954333,
 0.013070273,
 0.00093912566,
 0.03331114,
 0.46942326,
 1.4791902,
 0.38580665,
 0.8991855,
 0.06289806,
 0.0,
 0.08840234,
 0.64016783,
 0.026010754,
 0.27498755,
 0.23432632,
 0.0138499215,
 10.56429,
 0.0,
 0.04966275,
 0.32520857,
 0.005330386,
 0.08058562,
 0.01932034,
 0.020971948,
 0.025205567,
 0.0039041757,
 0.47526252,
 0.015614682,
 0.019682236,
 0.0023725827,
 0.009213154,
 0.045546517,
 0.14646424,
 0.10386323,
 0.06790388,
 0.90383035,
 0.0,
 0.11667511,
 0.3258262,
 0.05388544,
 0.07565282,
 0.0931797,
 0.3338503,
 0.005814005,
 0.0,
 0.37209824,
 0.0,
 0.07581672,
 0.080551624,
 4.824841,
 0.82438165,
 0.79437804,
 1.9996754,
 0.22803652,
 0.0011574895,
 0.00037509316,
 0.15771295,
 4.3324866,
 0.09683626,
 0.12927999,
 2.060619,
 0.0,
 0.33076364,
 0.20697218,
 0.248753,
 0.10013776,
 0.0983799,
 0.020987371,
 2.4237654,
 0.28180137,
 0.35294124,
 0.02068208,
 0.0,
 0.042037148,
 11.584945,
 0.1511621,
 0.1490182,
 0.04857341,
 1.2708054,
 1.8222862,
 0.1405889,
 1.0219464,
 0.7166924,
 0.027632982,
 0.38204694,
 5.107989,
 0.019126354,
 0.2096634,
 0.08458769,
 0.0,
 0.2677432,
 0.6436539,
 0.08102354,
 0.11641153,
 0.58693963,
 5.0917745,
 1.3274158,
 0.001805509,
 0.01795997,
 0.1855036,
 0.10145476,
 0.2446397,
 0.0,
 0.08556622,
 0.0010194347,
 0.04449041,
 0.0013543436,
 0.031067973,
 0.11564361,
 0.032590088,
 0.8782746,
 0.546982,
 1.3790125,
 0.4083489,
 0.04440527,
 0.020478347,
 0.9128774,
 0.004045686,
 2.830413,
 0.14603718,
 0.0,
 0.0,
 0.0,
 0.090398185,
 0.0,
 0.074286036,
 0.15234214,
 0.4141543,
 0.15651059,
 0.028892154,
 0.0,
 0.08265158,
 0.068674795,
 0.07034832,
 0.044274796,
 2.451639,
 0.40672007,
 10.530266,
 0.009447828,
 0.482056,
 0.39368105,
 0.2772167,
 0.21000421,
 1.3039927,
 0.10515588,
 1.9406074,
 5.7762895,
 0.0,
 2.495331,
 0.108950175,
 0.43756545,
 0.29430124,
 0.38696483,
 0.017376646,
 0.14966042,
 5.025813,
 0.12073646,
 0.0033135898,
 0.35064244,
 0.0619265,
 0.84513503,
 0.31246617,
 0.007774686,
 0.59853387,
 0.0032365434,
 2.6189213,
 9.82351,
 4.2780156,
 0.0012975094,
 0.21630287,
 0.00053295057,
 0.0042569283,
 7.553659,
 1.1698451,
 0.06251455,
 0.27689785,
 4.227521,
 0.031352125,
 0.011288352,
 0.01618399,
 0.0,
 4.380626,
 0.39982232,
 7.3283324,
 0.0008491879,
 0.70066005,
 0.16742294,
 0.93117285,
 0.027995763,
 4.68315,
 0.046544746,
 0.07507066,
 0.52403396,
 0.008560716,
 0.60676587,
 0.09707082,
 0.045957983,
 0.029845372,
 0.0,
 0.015110674,
 0.030799692,
 0.91251427,
 0.13921648,
 0.46640348,
 0.14326836,
 0.3657365,
 0.43075967,
 0.43293706,
 0.0,
 0.0011528328,
 1.4232875,
 0.22217518,
 0.45955715,
 0.06511581,
 0.04013029,
 0.09115752,
 0.060065255,
 0.0023252775,
 0.16308928,
 0.0237616,
 0.5394153,
 0.016983135,
 0.60284853,
 0.5254834,
 0.30620384,
 0.47150043,
 0.04176609,
 0.00974947,
 0.74453425,
 0.008609938,
 0.19102043,
 2.9216554,
 0.00911307,
 0.052418277,
 3.628919,
 0.0018647067,
 1.0724316,
 0.36866918,
 0.0,
 0.010131689,
 0.050121844,
 0.023634294,
 0.0,
 0.00035658074,
 0.026442057,
 0.54749435,
 0.13911973,
 0.0039334535,
 0.0075825932,
 0.0044999123,
 0.10939627,
 0.0022633024,
 0.02784056,
 0.2872221,
 0.0018506338,
 0.6017221,
 0.4790692,
 1.2223891,
 1.7005968,
 0.010237264,
 0.0747119,
 15.515312,
 0.06098963,
 0.0,
 9.731318,
 0.0,
 0.0,
 0.022777462,
 0.04507948,
 0.0018115556,
 0.62879664,
 0.5880329,
 0.9392462,
 0.0062011373,
 0.45358518,
 0.30056787,
 0.080623545,
 0.00015965351,
 2.3592968,
 0.52323216,
 0.0,
 0.04825707,
 0.08848568,
 0.2359774,
 4.4993663,
 0.8926263,
 0.12436297,
 0.22483248,
 0.8081294,
 1.8990346,
 0.07966234,
 0.052501783,
 0.29399645,
 0.16889524,
 0.6701293,
 0.19053476,
 0.0050840788,
 0.0071427342,
 0.20998168,
 0.038248513,
 0.24862866,
 0.12675476,
 0.017173545,
 0.24622822,
 0.15426333,
 0.008882421,
 1.6075115,
 0.8015699,
 1.7971226,
 0.0,
 0.230702,
 3.277921,
 0.114552796,
 0.0,
 1.9883208,
 0.33279008,
 0.37800992,
 0.13640745,
 0.21009777,
 1.5080227,
 5.2599177,
 0.0040928405,
 13.697116,
 0.1717779,
 5.204149,
 2.070883,
 0.44201365,
 2.4697044,
 0.10919567,
 0.70932716,
 4.937103,
 0.006059471]

def scale_image(image):
  image = cv2.imread(image)
  new_image = cv2.resize(image, (224,224))
  img = new_image.reshape(-1, 224,224,3)
  return np.asarray(img)
def calcualte_embeddings(model, image):
  image = scale_image(image)
  emb = model.predict(image)
  return np.array(emb)

def monitor_disease(daily_image, base_features = base_features):
  model = tf.keras.applications.VGG16(include_top=False, pooling='avg', input_shape=(224,224,3))
  A = calcualte_embeddings(model, daily_image)
  B = base_features
  cosine = np.dot(A,B)/(norm(A)*norm(B))
  return cosine[0]

# print(monitor_disease('images/1311380923053485284.jpg')[0])



























# feat=[]
# model = tf.keras.applications.VGG16(include_top=False, pooling='avg', input_shape=(224,224,3))

# for each in os.listdir('test'):
#   img_path = '/content/test/'
#   img = (img_path+each)
#   feat.append(calcualte_embeddings(model, img))

# len(feat)

# import pandas as pd
# feat = np.array(feat).reshape(-1, 512)
# dd = pd.DataFrame(feat)

# dd

# fin = []
# for each in dd.columns:
#   fin.append(dd[each].mean())

# fin

# np.dot((base_features[0], embeddings[0])/ (norm(base_features[0])*norm(embeddings[0])))





