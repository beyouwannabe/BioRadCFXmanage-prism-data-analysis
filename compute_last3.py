import numpy as np
import pandas as pd
from hanshu import xuanze_Actin
from hanshu import xuanze_gene
from hanshu import random
from hanshu import compute_relexp

# 指定Excel文件路径
excel_file_path = 'last3/CK-2.xlsx'
excel_file_path1 = 'last3/Dtu-2.xlsx'

# 读取Excel文件
df = pd.read_excel(excel_file_path)
df1 = pd.read_excel(excel_file_path1)

# 初始随机化数据
num_iterations = 5
the_time = '48h'  #  '2h' '6h' '8h' '12h' '24h' '48h'
CK_Actin, gene1, gene2, gene3, chuli_Actin, genechuli1, genechuli2, genechuli3 = random(df, df1,
        'CK-Actin', 'CK-OsAos2', 'CK-OsMPK6', 'CK-OsPRla', 'Dtu-Actin', 'Dtu-OsAos2', 'Dtu-OsMPK6', 'Dtu-OsPRla', the_time)


# 循环生成四次组合并且计算
def three_gene_result(gene_name_CK, genename_chuli, num_iterations=5):
    all_results_list = []
    for i in range(num_iterations):
        single_result_array = np.zeros((4, 1))
        if i >= 3:
            shang = np.concatenate((CK_Actin[2].reshape(2, 1), gene_name_CK[i].reshape(2, 1)), axis=1)
            xia = np.concatenate((chuli_Actin[2].reshape(2, 1), genename_chuli[i].reshape(2, 1)), axis=1)
            combined_result = np.vstack((shang, xia))
            x = combined_result[0][0]
            y = combined_result[0][1]
            # result1 = compute_relexp(combined_result[0][0], combined_result[0][1], x, y)
            # result2 = compute_relexp(combined_result[1][0], combined_result[1][1], x, y)
            # result3 = compute_relexp(combined_result[2][0], combined_result[2][1], x, y)
            # result4 = compute_relexp(combined_result[3][0], combined_result[3][0], x, y)
            single_result_array[0] = compute_relexp(combined_result[0][0], combined_result[0][1], x, y)
            single_result_array[1] = compute_relexp(combined_result[1][0], combined_result[1][1], x, y)
            single_result_array[2] = compute_relexp(combined_result[2][0], combined_result[2][1], x, y)
            single_result_array[3] = compute_relexp(combined_result[3][0], combined_result[3][1], x, y)

            # 将单次结果数组添加到列表中
            all_results_list.append(single_result_array)

        else:
            shang = np.concatenate((CK_Actin[i].reshape(2, 1), gene_name_CK[i].reshape(2, 1)), axis=1)
            xia = np.concatenate((chuli_Actin[i].reshape(2, 1), genename_chuli[i].reshape(2, 1)), axis=1)
            combined_result = np.vstack((shang, xia))
            x = combined_result[0][0]
            y = combined_result[0][1]
            # result1 = compute_relexp(combined_result[0][0], combined_result[0][1], x, y)
            # result2 = compute_relexp(combined_result[1][0], combined_result[1][1], x, y)
            # result3 = compute_relexp(combined_result[2][0], combined_result[2][1], x, y)
            # result4 = compute_relexp(combined_result[3][0], combined_result[3][0], x, y)
            single_result_array[0] = compute_relexp(combined_result[0][0], combined_result[0][1], x, y)
            single_result_array[1] = compute_relexp(combined_result[1][0], combined_result[1][1], x, y)
            single_result_array[2] = compute_relexp(combined_result[2][0], combined_result[2][1], x, y)
            single_result_array[3] = compute_relexp(combined_result[3][0], combined_result[3][1], x, y)

            # 将单次结果数组添加到列表中
            all_results_list.append(single_result_array)

    return all_results_list


all_results_list1 = three_gene_result(gene1, genechuli1)
all_results_list2 = three_gene_result(gene2, genechuli2)
all_results_list3 = three_gene_result(gene3, genechuli3)

# 将三个列表合并为一个列表
all_results_list = all_results_list1 + all_results_list2 + all_results_list3

# 获取列表的长度和每个结果的形状
num_results = len(all_results_list)
result_shape = all_results_list[0].shape

# 创建一个 DataFrame
# 创建一个 DataFrame
columns = [f'OsAos2_{i+1}' for i in range(0, result_shape[0] + 1)] + \
          [f'OSMPK6_{i+1}' for i in range(0, result_shape[0] + 1)] + \
          [f'OsPRla_{i+1}' for i in range(0, result_shape[0] + 1)]
results_df = pd.DataFrame(np.concatenate(all_results_list, axis=1), columns=columns)

# 将结果保存到 Excel 文件
results_df.to_excel(f'{the_time}_results_last3.xlsx', index=False)







