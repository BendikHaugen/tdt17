import os
files = os.listdir("yolov7/runs/detect/exp4/labels")
labelles=[]
for result in files:
    name = f"{result.split('.')[0]}.jpg,"
    labelles.append(name.strip())
    with open(f"yolov7/runs/detect/exp4/labels/{result}") as file:
        lines = file.readlines()
        file.close()
    with open("output.txt", "a") as file:
        file.write(name)
        num_lines = 0 
        for line in lines:
            if num_lines == 5: break
            label = int(line.split()[0]) + 1
            if label in [5, 6, 7, 8, 9]:
                label -= 4
            line = line.split(" ")[1:5]
            line = [float(res.strip()) for res in line]
            formatted_line = []    
            x, y, w, h = line[0] * 3650, line[1] * 2044, line[2] * 3650, line[3] * 2044
            formatted_line.append(f"{label} {int(x)} {int(y)} {int(x+w)} {int(y+h)}")
            file.write(f"{formatted_line[0]} ")
            num_lines += 1
        file.write("\n")
        file.close()

files = os.listdir("/cluster/projects/vc/courses/TDT17/2022/open/RDD2022/Norway/test/images")
for name in files:
    if name not in labelles:
        with open("output.txt", "a") as file:
            file.write(f"{name},")
            file.write("\n")
            file.close()

 


