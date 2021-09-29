from .models import Task
from django.forms import ModelForm
from pyzbar.pyzbar import decode
import cv2

# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ["","","",""]

def Camera(request):
    if request.method == "POST":
        # https:// pypi.org/project/qrcode/
        cap = cv2.VideoCapture(0)
        # инициализируем детектор QRCode cv2
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cap.read()
            # обнаружить и декодировать
            data, bbox, _ = detector.detectAndDecode(img)
            # проверяем, есть ли на изображении QRCode
            if bbox is not None:
                # отображаем изображение с линиями
                for i in range(len(bbox)):
                    # рисуем все линии
                    cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
                if data:
                    #print("[+] QR Code detected, data:", data)
                    return data
            # отобразить результат
            #cv2.imshow("img", img)
           # if cv2.waitKey(1) == ord("q"):
           #     break
        #cap.release()
        #cv2.destroyAllWindows()

        # src = '' #'Images/view1.png'
        #
        # img = cv2.imread(src, cv2.IMREAD_COLOR)
        # size = img.shape
        #
        # input_corners = np.array(calibrate.extractCorners(calibrate.extractFieldLines(img)))
        # output_corners = np.array([[0, 500.0, 0], [800.0, 500.0, 0], [800.0, 0, 0], [0, 0, 0]])
        #
        # input_corners = input_corners.astype('float32')
        # output_corners = output_corners.astype('float32')
        #
        # cam_mat = cv2.initCameraMatrix2D([output_corners], [input_corners], size)
        # #    cam_mat = np.array([[2200, 0, 750], [0, 2200, 750.0], [0, 0, 1.0]])
        # #    dist_coefs = np.zeros(4)
        # #    projMat = cv2.calibrateCamera([output_corners], [input_corners], size, cam_mat, dist_coefs, flags=cv2.CALIB_USE_INTRINSIC_GUESS)
        # decoded = decode(img)
        # print(decoded[0].data.decode("utf-8"))