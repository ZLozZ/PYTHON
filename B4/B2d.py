
import shutil 
#không lấy đường dẫn thư viện cố định 
source_path = 'D:\CODE\Hoc_Python\B4\Package_113'
destination_path = 'C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python310\\lib\\Package_113'

destination_path = shutil.copytree(source_path, destination_path, copy_function = shutil.copy) 
print("Đường dẫn:", destination_path)