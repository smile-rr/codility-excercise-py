def gale_shapley(men_prefs, women_prefs):
    """
    使用 Gale-Shapley 算法解决稳定婚配问题。

    参数：
    - men_prefs: 一个字典，键是男性的名字，值是一个列表，表示男性的偏好列表（女性的名字的顺序）
    - women_prefs: 一个字典，键是女性的名字，值是一个列表，表示女性的偏好列表（男性的名字的顺序）

    返回值：
    - 一个字典，表示每个男性的配偶
    """
    men = list(men_prefs.keys())
    women = list(women_prefs.keys())

    # 初始化配对结果
    free_men = set(men)
    men_partner = {man: None for man in men}
    women_partner = {woman: None for woman in women}
    
    # 为每个女性创建一个偏好排名表
    women_rank = {woman: {man: rank for rank, man in enumerate(prefs)} for woman, prefs in women_prefs.items()}

    # 男性提议和女性的接受状态
    proposals = {man: 0 for man in men}

    while free_men:
        man = free_men.pop()
        woman = men_prefs[man][proposals[man]]
        proposals[man] += 1
        
        if women_partner[woman] is None:
            # 女性没有配对，直接配对
            men_partner[man] = woman
            women_partner[woman] = man
        else:
            # 女性已配对，检查是否接受新配对
            current_partner = women_partner[woman]
            if women_rank[woman][man] < women_rank[woman][current_partner]:
                # 如果女性更喜欢当前提议的男性
                men_partner[man] = woman
                women_partner[woman] = man
                free_men.add(current_partner)  # 当前配对的男性变为自由男性
            else:
                # 保持当前配对不变，男性重新成为自由男性
                free_men.add(man)

    return men_partner

# 测试用例
def test_gale_shapley():
    men_prefs = {
        'A': ['X', 'Y', 'Z'],
        'B': ['Y', 'X', 'Z'],
        'C': ['X', 'Y', 'Z']
    }
    
    women_prefs = {
        'X': ['A', 'B', 'C'],
        'Y': ['B', 'A', 'C'],
        'Z': ['C', 'A', 'B']
    }
    
    result = gale_shapley(men_prefs, women_prefs)
    print("Matching result:", result)

# 运行测试用例
test_gale_shapley()