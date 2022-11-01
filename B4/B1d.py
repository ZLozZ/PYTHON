
import shutil
 
source_path = "D://CODE//Hoc_Python//B4//random_ptu.py"
destination_path = "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python310\\lib\\random_ptu.py"
 
destination_path = shutil.copyfile(source_path, destination_path)
print("Đường dẫn:", destination_path)