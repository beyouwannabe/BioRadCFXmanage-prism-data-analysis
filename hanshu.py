import numpy as np
import pandas as pd


# 随机选择函数
def xuanze_gene(df, Target_value, sample_value, num_combinations=5):
    selected_rows = df[(df['Target'] == Target_value) & (df['Sample'] == sample_value)]

    # 只保留'Cq'
    selected_data = selected_rows[['Cq']]

    cq_values = selected_data['Cq'].tolist()
    combinations = []

    # 随机顺序组合
    # for _ in range(num_combinations):
    #     random_combination = np.random.choice(cq_values, size=2, replace=False)
    #     combinations.append(random_combination)

    # 固定顺序组合
    combinations.append(np.array([cq_values[0], cq_values[1]]))
    combinations.append(np.array([cq_values[1], cq_values[2]]))
    combinations.append(np.array([cq_values[2], cq_values[3]]))
    combinations.append(np.array([cq_values[0], cq_values[2]]))
    combinations.append(np.array([cq_values[1], cq_values[3]]))

    return combinations


def xuanze_Actin(df, Target_value, sample_value, num_combinations=3):
    selected_rows = df[(df['Target'] == Target_value) & (df['Sample'] == sample_value)]

    # 只保留'Cq'
    selected_data = selected_rows[['Cq']]

    cq_values = selected_data['Cq'].tolist()
    combinations = []

    # # 每一次都随机组合
    # for _ in range(num_combinations):
    #     random_combination = np.random.choice(cq_values, size=2, replace=False)
    #     combinations.append(random_combination)

    # 固定顺序组合
    combinations.append(np.array([cq_values[0], cq_values[1]]))
    combinations.append(np.array([cq_values[0], cq_values[2]]))
    combinations.append(np.array([cq_values[1], cq_values[2]]))

    return combinations


# 计算relexp
def compute_relexp(can, gene, x, y):
    result = 2 ** -((gene - can) - (y - x))
    return result


# # 指定Excel文件路径
# excel_file_path = 'CK-1-Quantification Summary.xlsx'
# excel_file_path1 = 'GSDH-1-Quantification Summary.xlsx'
#
# # 读取Excel文件
# df = pd.read_excel(excel_file_path)
# df1 = pd.read_excel(excel_file_path1)


# # 打印数据框的前几行
# print(the_use.head())


# 时间 '12h' '24h' '2h' '48h' '6h' '8h'
# 基因和Ck  'CK-Actin' 'CK-OsLox2' 'CK-OsPBZ1' 'CK-OsWRKY70'
# 基因和GSDH  'GSDH-Actin' 'GSDH-OsLox2' 'GSDH-OsPBZ1' 'GSDH-OsWRKY70'
def random(data, data1, name1, name2, name3, name4, name5, name6, name7, name8, sample_value):

    CK_Actin = xuanze_Actin(data, name1, sample_value)
    gene_1 = xuanze_gene(data, name2, sample_value)
    gene_2 = xuanze_gene(data, name3, sample_value)
    gene_3 = xuanze_gene(data, name4, sample_value)

    chuli_Actin = xuanze_Actin(data1, name5, sample_value)
    genechuli_1 = xuanze_gene(data1, name6, sample_value)
    genechuli_2 = xuanze_gene(data1, name7, sample_value)
    genechuli_3 = xuanze_gene(data1, name8, sample_value)

    return CK_Actin, gene_1, gene_2, gene_3, chuli_Actin, genechuli_1, genechuli_2, genechuli_3


