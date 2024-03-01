import cv2
import easyocr
import re
import time

todetect=input("Enter Vehicle Number to Detect:")

harcascade = r"D:\VScode\Python\Vehicle_detection\Vehicle_Number_Plate_Recognition\model\indian_license_plate.xml"

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

reader = easyocr.Reader(['en'])

# Initialize the cascade classifier
plate_cascade = cv2.CascadeClassifier(harcascade)

def replace_characters(text):
    replacements = {
        'O': '0',
        'I': '1',
        'J': '3',
        'Z': '2',
        'A': '4',
        'G': '6',
        'B': '8',
        'S': '5',
        '0': 'O',
        '1': 'I',
        '2': 'Z',
        '3': 'J',
        '4': 'A',
        '6': 'G',
        '5': 'S',
        '8': 'B'
    }
    
    return ''.join(replacements[text] if text in replacements else text)
    # return ''.join(replacements[char] if char in replacements else char for char in text)


codes=['AN','AP','AR','AS','BR','CH','CG','DD','DL','GA','GJ','HR','HP','JK','JH','KA','KL','LA','LD','MP','MH','MN','ML','MZ','NL','OD','PY','PB','RJ','SK','TN','TS','TR','UP','UK','WB','UN','DN','OR']
prev=""
while True:
    success, img = cap.read()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
    
    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            img_roi = img[y: y + h, x:x + w]

            img_roi_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)

            # Read text from the detected number plate
            output = reader.readtext(img_roi_gray)
            if output:
                detected_text = output[0][-2].upper()
                
                # Remove spaces and special characters from the detected text
                modified_text = re.sub('[^a-zA-Z0-9]', '', detected_text)

                # Check conditions for modifying and highlighting the detected text
                if len(modified_text) >= 9 and len(modified_text) <= 11:
                    
                    # Check and replace characters
                    for i in range(2):
                        if modified_text[i].isdigit():
                            modified_text = modified_text[:i] + replace_characters(modified_text[i]) + modified_text[i+1:]
                    for i in range(-4, 0):
                        if modified_text[i].isalpha():
                            modified_text = modified_text[:i] + replace_characters(modified_text[i]) + modified_text[i+1:]
                    for i in range(4, len(modified_text) - 4):
                        if modified_text[i].isdigit():
                            modified_text = modified_text[:i] + replace_characters(modified_text[i]) + modified_text[i+1:]
                    for i in range(2):
                        if modified_text[i+2].isalpha():
                            modified_text = modified_text[:i+2] + replace_characters(modified_text[i+2]) + modified_text[i+3:]

                    # Check if the modified text includes two alphabets at the beginning as state/UT codes and four digits at the end
                    if modified_text[:2].isalpha() and modified_text[-4:].isdigit() and modified_text[:2] in codes :
                        if prev !=modified_text:
                            DetectTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            print(f"Detected Text:{modified_text}\nTime:{DetectTime}")
                            if(modified_text==todetect):
                                print("Car found!")

                            prev=modified_text

                        # Draw a rectangle around the object
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        # Display the modified text on the rectangle
                        cv2.putText(img, modified_text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                        # Save the image with detected number plate and text
                        cv2.imwrite(r"D:\VScode\Python\Vehicle_detection\Vehicle_Number_Plate_Recognition\plates\img" + str(count) + ".jpg", img_roi)
                        count += 1

    cv2.imshow("Result", img)

    if cv2.waitKey(1)!=-1 :
        break

cap.release()
cv2.destroyAllWindows()
