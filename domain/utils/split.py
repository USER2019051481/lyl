def split(s: str) -> list:
    # 函数的功能是拆解"(xxx (yyy))"成[xxx, (yyy)]
    def get_next_idx(i_: int) -> int:
        left, right = 1, 0
        while left > right:
            if s[i_] == '(':
                left += 1
            elif s[i_] == ')':
                right += 1
            i_ += 1
        return i_

    word_list = []
    idx = 1
    while len(s) - 1 > idx:
        if s[idx] == '(':
            next_ = get_next_idx(idx + 1)
            if next_ == -1:
                next_ = idx
            word_list.append(s[idx: next_])
            idx = next_ + 1
        elif s[idx] != ' ':
            next_ = s.find(" ", idx)
            if next_ == -1:
                next_ = len(s) - 1
            word_list.append(s[idx: next_])
            idx = next_ + 1
        else:
            idx += 1

    for i in range(len(word_list)):
        if word_list[i][0] == '(':
            word_list[i] = split(word_list[i])

    return word_list
