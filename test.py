import cv2

print("🔥 Script started")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not accessible")
    exit()

print("✅ Camera opened")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame read failed")
        break

    cv2.imshow("ATM Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
