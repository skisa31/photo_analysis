def extract_photo_log(file_path):
    photo_lines = []  # 写真の情報がある行を格納するリスト
    photo_logs = []  # 出力するログを格納するリスト
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'SET-BUFFER-CHUNK RETRIEVAL P' in line:
                photo_lines.append(line)

    with open('./log/photo_log.txt', 'w') as f:
        for log in logs:
            f.write(log)


if __name__ == '__main__':
    extract_photo_log('./log/trace.txt')
