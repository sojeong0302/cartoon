import numpy as np
import cv2

# 이미지 파일을 바이너리로 읽어서 numpy 배열로 변환
ff = np.fromfile('openCV/poto.jpg', np.uint8)

# 바이너리 데이터에서 이미지로 디코딩, 원본 이미지의 채널과 동일하게 읽음
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

# 이미지를 리사이즈 (현재 크기를 유지)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

while True:
    # 사용자로부터 sigma_s와 sigma_r 값 입력받기
    try:
        sigma_s_input = input("Enter sigma_s (0-200): ")
        sigma_r_input = input("Enter sigma_r (0-100): ")

        # 입력값을 정수로 변환
        sigma_s_value = int(sigma_s_input)
        sigma_r_value = int(sigma_r_input) / 100.0  # sigma_r 값은 실수로 변환

        # 입력값이 유효한지 확인
        if sigma_s_value < 0 or sigma_s_value > 200 or sigma_r_value < 0 or sigma_r_value > 1:
            print("Invalid input, please enter valid values for sigma_s and sigma_r.")
            continue

    except ValueError:
        print("Invalid input, please enter integers for sigma_s and sigma_r.")
        continue

    # 입력 이미지에 카툰 효과 적용 (sigma_s와 sigma_r 값을 사용)
    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)

    # 카툰 이미지 표시
    cv2.imshow("Cartoon View", cartoon_img)

    # 'q' 키를 누르면 종료
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# 모든 윈도우 닫기
cv2.destroyAllWindows()
