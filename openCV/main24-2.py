# 수치 계산 및 배열 작업에 사용
import numpy as np

# 이미지 처리 작업에 사용
import cv2

# 이미지 파일을 바이너리로 읽어서 numpy 배열로 변환
ff = np.fromfile('openCV/poto.jpg', np.uint8)

# 바이너리 데이터에서 이미지로 디코딩, 원본 이미지의 채널과 동일하게 읽음
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

# 이미지를 리사이즈 (현재 크기를 유지)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 트랙바가 이동될 때 호출될 콜백 함수 
def onChange(pos):
    pass

# 트랙바와 이미지를 표시할 윈도우 생성
cv2.namedWindow("Trackbar Windows")

# 'sigma_s' 트랙바 생성, 0~200, 콜백 함수 onChange 설정
cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onChange)

# 'sigma_r' 트랙바 생성, 0~100, 콜백 함수 onChange 설정
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onChange)

# 'sigma_s'의 초기 값을 100으로 설정
cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)

# 'sigma_r'의 초기 값을 10으로 설정
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)

# 'q' 키가 눌릴 때까지 반복
while True:
    # 100ms마다 키 입력을 대기하고 'q' 키가 입력되면 종료
    if cv2.waitKey(100) == ord('q'):
        break

    # 트랙바에서 sigma_s 값 가져오기
    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")

    # 트랙바에서 sigma_r 값 가져오고 100으로 나눠서 실수 값으로 변환
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0

    # 입력 이미지에 카툰 효과 적용 (sigma_s와 sigma_r 값을 사용)
    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)

    # 트랙바 윈도우에 카툰 이미지 표시
    cv2.imshow("Trackbar Windows", cartoon_img)

# 모든 윈도우 닫기
cv2.destroyAllWindows()
