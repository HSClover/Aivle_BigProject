import pandas as pd

# 파일 경로 지정
file_path = r"C:\Users\User\바탕화면용 폴더\AIVLE\19. 빅프로젝트\FDS\fds-master\Validation\NBS_Multi-Room\FDS_Input_Files\NBS_100A_1_1.sf"  # 경로를 필요에 따라 수정하세요

# 파일 전체를 읽어서 라인 단위로 나눔
with open(file_path, "r") as f:
    lines = f.readlines()

# 데이터를 저장할 리스트
data = []

# 각 줄을 공백 기준으로 나누고 파싱
for line in lines:
    parts = line.strip().split()
    if len(parts) == 3:
        try:
            time = float(parts[0])
            index = int(float(parts[1]))  # index는 정수형 처리
            value = float(parts[2])
            data.append((time, index, value))
        except ValueError:
            continue  # 숫자 변환 실패 시 무시

# 데이터프레임 생성
df = pd.DataFrame(data, columns=["time", "index", "value"])

# 결과 확인 (선택)
print(df.head())
