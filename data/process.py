#coding:utf-8

def t_2_s(seq):
    
    seq = seq.replace('花贝','花呗')
    seq = seq.replace('花坝','花呗')
    seq = seq.replace('唄','呗')
    seq = seq.replace('車','车')
    seq = seq.replace('嗎','吗')
    seq = seq.replace('唄','呗')
    seq = seq.replace('麼','么')
    seq = seq.replace('麽','么')
    seq = seq.replace('調','调')
    seq = seq.replace('証','证')
    seq = seq.replace('個','个')
    seq = seq.replace('還','还')
    seq = seq.replace('開','开')
    seq = seq.replace('螞蟻','蚂蚁')
    seq = seq.replace('説','说')
    seq = seq.replace('貸','贷')
    seq = seq.replace('碼','码')
    seq = seq.replace('時','时')
    seq = seq.replace('無','无')
    seq = seq.replace('請','请')
    seq = seq.replace('負','负')
    seq = seq.replace('減','减')
    #print(seq)
    return seq

#sequence('花呗分期能提前还清麽')
