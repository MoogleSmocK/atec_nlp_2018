TRAIN = 'atec_nlp_sim_train.csv'
VALID = 'valid.csv'



def get_resultx():

    result = dict()
    ## result[(train_label,label_label)]
    result[(1,1)]=0
    result[(0,0)]=0
    result[(1,0)]=0
    result[(0,1)]=0
    with open(TRAIN,'r') as f1, open(VALID,'r') as f2:
        content1 = f1.readlines()
        content2 = f2.readlines()
    length = len(content1)
    length2 = len(content2)
    if length != length2:
        print('lines length not match')
        return
    print('\t total lines is {}'.format(length))
    for i in range(length):
        valid_label = content2[i].strip().split('\t')[-1]
        train_label = content1[i].strip().split('\t')[-1]
        result[(int(train_label),int(valid_label))] += 1
    return result

def score(dict_x):
    pr_rate = float(dict_x[(1,1)]) / ( dict_x[(1,1)] +dict_x[(0,1)])
    print('precision rate = TP / (TP + FP)')
    print('{} \n'.format(pr_rate))

    re_rate = float(dict_x[(1,1)]) /( dict_x[(1,1)] + dict_x[(1,0)])
    print('recall rate = TP / (TP + FN)')
    print('{} \n'.format(re_rate))

    accuracy = float(dict_x[(1,1)]) / ( dict_x[(1,1)] + dict_x[(1,0)] + dict_x[(0,1)] +dict_x[(0,0)])
    print('accuracy = (TP + TN) / (TP + FP + TN + FN)')
    print('{} \n'.format(accuracy))

    f1_score = 2* pr_rate * re_rate / ( pr_rate + re_rate)
    print('F1-score = 2 * precision rate * recall rate / (precision rate + recall rate)')
    print('{} \n'.format(f1_score))

if __name__ =='__main__':

    res = get_resultx()
    print(res)
    score(res)
