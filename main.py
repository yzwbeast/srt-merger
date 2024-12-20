import os

def merge_srt(files, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        total_subtitles = 0
        for file in files:
            with open(file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
                for line in lines:
                    if line.strip().isdigit():
                        total_subtitles += 1
                        outfile.write(f"{total_subtitles}\n")
                    elif "-->" in line:
                        # 复制时间戳行
                        outfile.write(line)
                    else:
                        # 复制其他内容
                        outfile.write(line)
            outfile.write("\n")

# 输入文件夹路径
folder_path = "./sss"  # 替换为你的文件夹路径
files = []

# 遍历文件夹，收集所有 .srt 文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".srt"):
        files.append(os.path.join(folder_path, file_name))

# 按照文件名前面的数字部分进行排序
files.sort(key=lambda x: int(os.path.basename(x).split()[0]))

# 输出文件路径
output_file = "merged.srt"

merge_srt(files, output_file)
print(f"Merged subtitles saved to {output_file}")
