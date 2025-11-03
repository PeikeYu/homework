if __name__ == "__main__":
    list = list(range(1000))
    for idx in range(len(list)-1, -1, -1):
        if list[idx] % 2 == 1:
            list.pop(idx)
    print(list)
# 注意：在遍历列表时删除元素会导致索引变化
# 可能导致索引越界或漏删元素