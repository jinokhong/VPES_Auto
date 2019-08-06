import os
fPath = "/CT_CT_DIR_Study.xml"

# 현재 파일의 폴더 위치 저장
pathSave = os.path.dirname(os.path.realpath(__file__))
print(pathSave)
# 현재 테스트 케이스의 위치로 이동
os.chdir(pathSave)
# 상위 폴더로 이동
os.chdir('../VPES_Data')
print(os.getcwd())

# 현재 파일의 폴더 위치 저장
realpath = os.getcwd()
print(realpath)

FullPath = realpath+fPath
print(FullPath)
# dPath(upload.bat) 실행
# os.system(dPath)