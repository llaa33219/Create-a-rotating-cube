import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # 그래픽 백엔드를 Agg로 설정
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 이미지를 저장할 폴더 생성
output_folder = 'images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 정육면체를 그리는 함수
def draw_cube(angle):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1,1,1])
    
    vertices = np.array([
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
    ])
    
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]], 
        [vertices[0], vertices[1], vertices[5], vertices[4]], 
        [vertices[2], vertices[3], vertices[7], vertices[6]], 
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[0], vertices[3], vertices[7], vertices[4]]
    ]
    
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    ax.view_init(30, angle)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    ax.set_axis_off()
    
    # 이미지 저장 경로 수정
    file_path = os.path.join(output_folder, f'cube_rotation_{angle}.png')
    plt.savefig(file_path, dpi=300)
    plt.close()
    print(f'Saved: {file_path}')  # 저장된 파일 경로 출력

# 0도부터 359도까지 1도씩 회전하며 이미지 생성
for angle in range(360):
    draw_cube(angle)
