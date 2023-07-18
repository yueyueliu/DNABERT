#seq = "Caccctaaaccctaacccctaaccctaaccctaaccctaaccctaaccctaacccctaaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaacccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaacccaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaaccct"
# 10000个碱基的序列，这里用省略号代替

file = open("demo_data_long.txt", "r")
content = file.read()
file.close()

char_to_remove = "\n"
seq = content.replace(char_to_remove,"")
seq = seq.upper()

seq_len = len(seq)
print("length of string:",seq_len)
window_size = 512
step_size = 256

#将序列分成若干个长度为window_size的片段，末尾不足的用N进行填充
seqs = [seq[i:i+window_size].ljust(window_size, "N") for i in range(0, seq_len, step_size)]
num_seqs = len(seqs)
print("length of num_seq:", num_seqs)

# #打印输出处理后的序列
# for i in range(num_seqs):
#     print(f"Sequence {i+1}: {seqs[i]}")

#保存输出处理后的序列
with open("demo_data_512.txt","w") as file:
    for str in seqs:
        str1 = " ".join(list(str))##在每个字母中间加入空格
        file.write(str1 + "\n")

