# -*- coding: utf-8 -*-
"""Criacao_Datasets_AME.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11kmMF_OIqcb1QJQlwywFmxAz5VAsSale

TAMANHO DA CU PARA CRIAR A SUA ÁRVORE DE DECISÃO
"""

cu_eixo_x = 128
cu_eixo_y = 128

"""PREPARAÇÃO DOS ARQUIVOS"""

!pip install pandas

from google.colab import drive
drive.mount('/content/drive')

"""DATASET TESTE"""

!ls 'drive/My Drive/Mestrado/Dissertação/Treinamento DTs AME/VTM 16.2 - AME - Dataset Teste'

import glob
lista = glob.glob ('drive/My Drive/Mestrado/Dissertação/Treinamento DTs AME/VTM 16.2 - AME - Dataset Teste/*.csv')

labels = ["qp", "depth", "qt_depht", "mt_depth", "video_width", "video_heigh", "cu_pos_x", "cu_pos_y", "cu_width", "cu_height", "bcw_index", "imv", "mv_uni_l0_hor_x", "mv_uni_l0_ver_y", "mv_uni_l1_hor_x", "mv_uni_l1_ver_y", "cost_mv_uni_l0", "cost_mv_uni_l1", "bits_mv_uni_l0", "bits_mv_uni_l1", "mv_bi_l0_hor_x", "mv_bi_l0_ver_y", "mv_bi_l1_hor_x", "mv_bi_l1_ver_y", "cost_bi", "bits_mv_bi", "smvd", "inter_dir_normal", "atual_QP", "affine_pai", "custo_pai", "aff_viz_esq", "aff_viz_esq_1", "custo_viz_esq", "aff_viz_acima", "aff_viz_acima_1", "custo_viz_aci", "cu_atual_affine", "aff_inter_dir", "sum", "media", "vari", "gradH", "gradV", "razao_grad", "grad_razao_pixels", "desvioPadrao", "executaAffine"]

blocksize = [cu_eixo_x, cu_eixo_y]

import pandas as pd
import gc

dataframe_teste = pd.DataFrame()
for csv in lista:
  print (csv)
  d = pd.read_csv (csv, sep=";", nrows=1000000)
  d = d[d["cu_width"] == blocksize[0]]
  d = d[d["cu_height"] == blocksize[1]]

  n_linhas = len(d)
  if n_linhas > 10000:
    n_linhas_remover = n_linhas - 10000
    linhas_remover = d.sample(n=n_linhas_remover).index
    d = d.drop(linhas_remover)

  dataframe_teste = pd.concat([dataframe_teste, d], axis=0)
  del d
  gc.collect()

dataframe_teste.to_csv('/content/drive/MyDrive/Mestrado/Dissertação/Treinamento DTs AME/VTM 16.2 - AME - Datasets Para Cada CU/dataset_ame_'+str(cu_eixo_x)+'x'+str(cu_eixo_y)+'_test.csv', sep=',', index=False)
dataframe_teste

"""DATASET TREINO"""

!ls 'drive/My Drive/Mestrado/Dissertação/Treinamento DTs AME/VTM 16.2 - AME - Dataset Treino'

import glob
lista = glob.glob ('drive/My Drive/Mestrado/Dissertação/Treinamento DTs AME/VTM 16.2 - AME - Dataset Treino/*.csv')

labels = ["qp", "depth", "qt_depht", "mt_depth", "video_width", "video_heigh", "cu_pos_x", "cu_pos_y", "cu_width", "cu_height", "bcw_index", "imv", "mv_uni_l0_hor_x", "mv_uni_l0_ver_y", "mv_uni_l1_hor_x", "mv_uni_l1_ver_y", "cost_mv_uni_l0", "cost_mv_uni_l1", "bits_mv_uni_l0", "bits_mv_uni_l1", "mv_bi_l0_hor_x", "mv_bi_l0_ver_y", "mv_bi_l1_hor_x", "mv_bi_l1_ver_y", "cost_bi", "bits_mv_bi", "smvd", "inter_dir_normal", "atual_QP", "affine_pai", "custo_pai", "aff_viz_esq", "aff_viz_esq_1", "custo_viz_esq", "aff_viz_acima", "aff_viz_acima_1", "custo_viz_aci", "cu_atual_affine", "aff_inter_dir", "sum", "media", "vari", "gradH", "gradV", "razao_grad", "grad_razao_pixels", "desvioPadrao", "executaAffine"]

blocksize = [cu_eixo_x, cu_eixo_y]

import pandas as pd
import gc
dataframe_treino = pd.DataFrame()
for csv in lista:
  print (csv)
  d = pd.read_csv (csv, sep=";", nrows=1000000)
  d = d[d["cu_width"] == blocksize[0]]
  d = d[d["cu_height"] == blocksize[1]]

  n_linhas = len(d)
  if n_linhas > 10000:
    n_linhas_remover = n_linhas - 10000
    linhas_remover = d.sample(n=n_linhas_remover).index
    d = d.drop(linhas_remover)

  dataframe_treino = pd.concat([dataframe_treino, d], axis=0)
  del d
  gc.collect()

dataframe_treino.to_csv('/content/drive/MyDrive/Mestrado/Dissertação/Treinamento DTs AME/VTM 16.2 - AME - Datasets Para Cada CU/dataset_ame_'+str(cu_eixo_x)+'x'+str(cu_eixo_y)+'_train.csv', sep=',', index=False)
dataframe_treino