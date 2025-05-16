import os
import cv2

color = "black"
save_folder = "22520109"

folders = [x for x in os.listdir() if x != save_folder and x != "rename.py"]
print(folders)

save_path = os.path.join(".", save_folder)
if not os.path.exists(save_path):
    os.makedirs(save_path)
    print(f"Created folder '{save_folder}' to save resized images.")
else:
    print(f"Folder '{save_folder}' already exists. Resized images will be saved here.")

for folder in folders:
    path = os.path.join(".", folder)
    files = os.listdir(path)
    print(f"Processing {folder}...")
    count = 0
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
            count += 1
            # Read the image
            img = cv2.imread(os.path.join(path, file))
            # Get the dimensions of the image
            height, width, _ = img.shape
            # Calculate the new dimensions
            new_width = 495
            new_height = 650
            # Resize the image
            resized_img = cv2.resize(img, (new_width, new_height))
            # Save the resized image with a new name
            new_name = f"{file[0]}_{folder}_{count}.jpg"
            cv2.imwrite(os.path.join(save_path, new_name), resized_img)
    print(f"Processed {count} images in '{folder}' folder.")
