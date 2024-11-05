# 수치 계산 및 배열 작업에 사용
import numpy as np
# 이미지 처리 작업에 사용
import cv2

# 이미지 파일을 바이너리 형식으로 읽어서 numpy 배열로 변환
ff = np.fromfile('poto.jpg', np.uint8)

# 바이너리 데이터를 이미지로 디코딩하여 원본 채널 정보에 맞게 읽어옴
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

# 이미지를 리사이즈 (dsize=(0, 0)은 크기를 그대로 유지, fx와 fy는 배율 설정)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 카툰 스타일 필터를 적용
cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)

# 'cartoon view'라는 이름의 윈도우에 카툰 스타일 이미지 표시
cv2.imshow('cartoon view', cartoon_img)

# 키 입력을 대기 (0은 무한 대기)
cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()