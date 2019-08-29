import re
import pandas as pd


def read_file(file):

    MyText = open(file, "r")
    MyText = MyText.read()
    MyText = re.sub(r'\t[0-9]+\n', r'\n', MyText)
    MyText = re.sub(r' +', r' ', MyText)

    lines0 = MyText.split('\n')
    lines1 = [line.strip('\n') for line in lines0 if '*' not in line]
    lines2 = [line.split(' ') for line in lines1]
    return lines2


def seq_compare(andra_seq, jbg18_seq):

    pairs_vec = list(zip(andra_seq, jbg18_seq))
    non_equal = list()
    for i, pair in enumerate(pairs_vec):
        if pair[0] != pair[1]:
            non_equal.append(i)

    diff_pairs = [pairs_vec[i] for i in non_equal]
    return non_equal, diff_pairs


def extract_hybrid_indexes(lines):
    indexes_list = []
    for line in lines:
        if '_Hybrid_' in line[0]:
            comps = line[0].split('_')
            indexes_list.append(int(comps[2].strip()))
    indexes_list = set(indexes_list)
    indexes_list = sorted(list(indexes_list))
    return indexes_list


lines = read_file('Hybrids_1-8_alignment.clustal_num.txt')
hybrid_index = extract_hybrid_indexes(lines) # old version -> hybrid_index = [1,2,3,4,5,6,7,8]

#print(hybrid_index)

andra_vec = [line[1] for line in lines if line[0] == 'Andhra']
jbg18_vec = [line[1] for line in lines if line[0] == 'JBug18']



andra_seq = ''.join(andra_vec)
jbg18_seq = ''.join(jbg18_vec)

indices, diff_pairs = seq_compare(andra_seq, jbg18_seq)


#print(indices)

andra_set = [andra_seq[i] for i in indices]
andra_bin = [0 for i in indices]
jbg18_set = [jbg18_seq[i] for i in indices]
jbg18_bin = [0 for i in indices]

for i in hybrid_index:

    name = 'AJ_Hybrid_'+str(i)
    vec = [line[1] for line in lines if line[0] == name]
    #print('Lenght of ' + name + ' = ' + str(len(vec)))
    seq = ''.join(vec)
    sample_set = [seq[i] for i in indices]


    for i in range(len(sample_set)):
        if andra_set[i] == sample_set[i]:
            andra_bin[i] += 1

# Change the coordinate, increment by one
indices = [indice+1 for indice in indices]

frame = {
        'Location' : indices,
        'Andr_Bin' : andra_bin,
        'Fraction' : [(float(bin) / len(hybrid_index)) for bin in andra_bin]
        }

df = pd.DataFrame.from_dict(frame)
df = df[['Location', 'Andr_Bin', 'Fraction']]
df.set_index('Location', inplace=True)

print(df)

df.to_csv('Analysis_Results.csv', sep=',')

print(len(andra_seq))

