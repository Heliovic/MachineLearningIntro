from chapter03.trees import *
from chapter03.tree_plotter import *

data_set = [
    [1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']]

# 以下标签对应数据集的两个特征
labels = ['no surfacing', 'flippers']

# print(calc_shannon_ent(data_set))

# print(split_data_set(data_set, 0, 1))

# print(choose_best_feature_to_split(data_set))

my_tree = create_tree(data_set, labels)
print(my_tree)

my_tree = retrieve_tree(0)

create_plot(my_tree)

# print(get_leaf_num(my_tree))
# print(get_tree_depth(my_tree))
