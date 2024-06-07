import os
from moviepy.editor import VideoFileClip


# 检查该文件是否已保存过
def is_exist(file_name,find_name):
    results = []
    with open(file_name, 'r') as file:
        context = file.read()
        # print(context)
    word = list(context.split('\n'))
    for k in range(len(word)):
        results.append(word[k].split())
    for i in range(len(results)):
        if len(results[i]) != 0 and find_name == results[i][0]:
            return True
    file.close()
    return False

def get_file_duration(file_path):#获取视频时长
    video = VideoFileClip(file_path)
    duration = video.duration
    return duration


def get_file(s):
    file_name='file.txt'
    name=get_file_prefix(file_name)
    # print(name)
    #文件名 手肘最低点坐标值lx,ly 手肘最高点坐标值hx,hy
    context=[]
    results = []
    with open(file_name, 'r') as file:
        context = file.read()
        # print(context)
    word = list(context.split('\n'))
    for k in range(len(word)):
        results.append(word[k].split())
    file.close()

    for i in range(len(results)):
        if len(results[i])!=0 and name==results[i][0]:
            return results[i][1],results[i][2],results[i][3],results[i][4]
    return 0,0,0,0
#将打开过的文件信息存档
def write_file_information(file_name,lx,ly,hx,hy):
    print(file_name)
    print(lx,ly,hx,hy)
    if is_exist('file.txt',file_name):
        print('write_file_information:','The file has been recorded')
        return True
    with open('file.txt', 'a') as file:
        file.write('\n')
        file.write(file_name+' ')
        file.write(str(lx)+' ')
        file.write(str(ly)+' ')
        file.write(str(hx)+' ')
        file.write(str(hy))
    file.close()

# 存储视频结果
def write_results(type,file_name,count,uncount):
    #文件名，合格个数 不合格个数 分数

    if type==0:
        file_='ywqz.txt'
    else:
        file_='fwc.txt'

    #视频长度
    duration=get_file_duration(file_name)
    # print(count/duration)
    #文件前缀
    name=get_file_prefix(file_name)

    #在结果记录中查询是否已存储
    if is_exist(file_,name):
        print('write_results:','The file has been recorded')
        return True

    with open(file_, 'a') as file:
        file.write(name+' ')
        file.write(str(count)+' ')
        file.write(str(uncount)+' ')
        file.write(str(int((count/duration)*100))+'\n') #分数=个数/视频时长

#获取文件名称（前缀）
def get_file_prefix(file_name):
    filename_with_extension = os.path.basename(file_name)
    name, _ = os.path.splitext(filename_with_extension)
    return name


#
# get_file('file.txt')
# write_ywqz_results('img/ywqz1.mp4',8,2)
