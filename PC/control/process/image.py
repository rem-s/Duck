#画像処理
import numpy as np
from numba import jit

#大津の二値化
def otsu_binarize(img, indexs):
    
    #初期化
    img_flat = img.reshape(-1)[indexs]
    Imax, Imin = np.max(img_flat), np.min(img_flat)
    thr_range = np.linspace(Imin, Imax, 100)
    S, thrs = [0], [0]
    
    #閾値探索
    for thr in thr_range[1:]:
        
        #閾値による2クラス分け
        class1_index, class2_index = np.where(img_flat < thr), np.where(img_flat >= thr)        
        class1_var, class1_ave, class1_n = np.var(img_flat[class1_index]), np.average(img_flat[class1_index]), len(class1_index)
        class2_var, class2_ave, class2_n = np.var(img_flat[class2_index]), np.average(img_flat[class2_index]), len(class2_index)
        
        #クラス間分散とクラス内分散
        var1 = ((class1_n * class1_var) + (class2_n * class2_var)) / (class1_n + class2_n)
        var2 = (class1_n * ((class1_ave - class2_ave) ** 2) + class2_n * ((class1_ave - class2_ave) ** 2)) / (class1_n + class2_n)
        
        #分散割合
        S.append(var1/var2)
    
    #分散が最小の割合を閾値
    otsu_thr = S[np.argsort(S)[-1]]
    
    #二値化画像生成
    binarize_img = np.where(img <= otsu_thr, 0, 1)
    
    return binarize_img
	
#中央値による二値化
def med_binarize(img, indexs):
	
	#初期化
	img_flat = img.reshape(-1)[indexs]
	Imedian = np.median(img_flat)
	
	#二値化画像生成
	binarize_img = np.where(img <= Imedian, 0, 1)
	
	return binarize_img
	
#平均値による二値化
def mean_binarize(img, indexs):
	
	#初期化
	img_flat = img.reshape(-1)[indexs]
	Imean = np.mean(img_flat)
	
	#二値化画像生成
	binarize_img = np.where(img <= Imean, 0, 1)
	
	return binarize_img
	
#近傍ピクセルの探索 [高速化必要]
def neighbor(img, x, y, lookup_table):
	height, width = img.shape
	labels = []

	#8近傍ピクセル探索
	if(y-1>=0 and img[y-1][x]!=0): labels.append(img[y-1][x]) 
	if(y+1<height and img[y+1][x]!=0): labels.append(img[y+1][x])
	if(x-1>=0 and img[y][x-1]!=0): labels.append(img[y][x-1])
	if(x+1<width and img[y][x+1]!=0): labels.append(img[y][x+1])
	if(x-1>=0 and y-1>=0 and img[y-1][x-1]!= 0): labels.append(img[y-1][x-1])
	if(x+1<width and y-1>=0 and img[y-1][x+1]!=0): labels.append(img[y-1][x+1])
	if(x-1>=0 and y+1<height and img[y+1][x-1]!=0): labels.append(img[y+1][x-1])
	if(x+1<width and y+1<height and img[y+1][x+1]!=0): labels.append(img[y+1][x+1])

	#ラベルが存在する時 (一番小さいラベルにＬＵＴ設定)
	if len(labels) > 0: 
		min_label = np.sort(labels)[0]
		for label in labels: 
			if min_label < lookup_table[int(label)]: 
				if lookup_table[int(min_label)] < min_label:
					lookup_table[int(label)] = lookup_table[int(min_label)]
				else: lookup_table[int(label)] = min_label
				
	#ラベルが存在しない時
	else: 
		min_label = 0

	return min_label, lookup_table
	
#画像8近傍ラベリング [高速化必要]
def labeling(img, indexs):

	#初期化
	label = 0
	height, width = img.shape
	label_img = np.zeros(img.shape)
	lookup_table = np.arange(width * height)
	
	#画像探索
	for (h, w) in indexs:
		
		#画像中の黒成分の探索
		if img[h][w] == 0:
			min_label, lookup_table = neighbor(label_img, w, h, lookup_table)
			
			#近傍ラベルが0の場合
			if min_label == 0:
				label += 1
				label_img[h][w] = label
			
			#近傍ラベルの最小ラベルを割り当てる
			else: label_img[h][w] = min_label
		
		#画像中の白成分の探索
		else: label_img[h][w] = 0
	
	#ルックアップテーブルによるラベル更新
	for (h, w) in indexs: label_img[h][w] = lookup_table[int(label_img[h][w])]
	
	return label_img
	
#画像面積比較
def compare_area(img):
    height, width = img.shape
	
	#画像から最大面積ラベル算出
    img_flat = img.reshape(-1)
    areas = np.array([len(np.where(img_flat == i)[0]) for i in np.unique(img_flat)[1:]])
    value = np.unique(img_flat)[np.argmax(areas)+1]
    return np.where(img_flat == value, 1, 0).reshape(img.shape)

#画像のラインより機体の回転θ度算出
def image_line_degree(img):
	height, width = img.shape
	
	#上・下抽出点[上:1/4, 下:3/4]
	img_sum = np.sum(img, axis=1)
	indexs = np.where(img_sum>0)[0]
	under_extraction, upper_extraction = height, indexs[0]
	upper = img[indexs[0]]
	
	#θ度算出
	ave_under_index, ave_upper_index = int(width/2), np.average(np.where(upper == 1))
	theta = np.arctan(np.abs((ave_upper_index - ave_under_index)/(upper_extraction - under_extraction)))
	if (ave_upper_index - ave_under_index)/(upper_extraction - under_extraction) > 0: theta = -1 * theta
	theta = theta * 180 / np.pi
	return int(theta), upper_extraction, under_extraction, int(ave_upper_index), int(ave_under_index)
	
#画像中のindex関数
#def f1(x, h, w): return (-1*(w/h)*(x-h)).astype(np.int32)
#def f2(x, h, w): return ((w/h)*x).astype(np.int32)
def f1(x, h, w): return x * 0
def f2(x, h, w): return np.full(len(x), w-1)

#画像中の正面index
def target_indexs(height, width, target_height=60): 
	y = np.arange(target_height, height)
	index1, index2 = f1(y, height, width), f2(y, height, width)
	indexs_flat = np.array([ y[n]*width+index for n, (i1, i2) in enumerate(zip(index1, index2)) for index in range(i1, i2+1)])
	indexs_dim = np.array([ [y[n], index] for n, (i1, i2) in enumerate(zip(index1, index2)) for index in range(i1, i2+1)])
	return indexs_flat, indexs_dim
	
#ライン上に機体があるか検出
def on_line(img, target_bottom):
	height, width = img.shape
	return len(np.where(img[target_bottom:height, :].reshape(-1)==1)[0])
	
#画像中にラインが存在するか検出
def detect_line(img, online_data):
	if online_data == 1: return 4
	elif online_data == 2: return 3
	elif online_data == 3: return 2
	return 0
	
#画像の歪曲調整
def distortion(img, k1=-6.25*(10**-7), k2=0):
    
    #初期処理
    height, width, channel = img.shape
    h_mid, w_mid = height//2, width//2
    dist_img = np.zeros((img.shape))
    
    #歪曲修正
    w = np.arange(width)
    for h in range(height):
        
        #歪曲演算
        r = np.sqrt((h_mid-h)**2+(w_mid-w)**2)
        wd = ((1 + k1*(r**2) + k2*(r**4))*(w-width//2)).astype(np.int32) + width//2
        hd = ((1 + k1*(r**2) + k2*(r**4))*(h-height//2)).astype(np.int32) + height//2
        
        wd = np.where(wd>=width, width-1, wd)
        wd = np.where(wd<0, 0, wd)
        hd = np.where(hd>=height, height-1, hd)
        hd = np.where(hd<0, 0, hd)
        
        #画像編集
        dist_img[h, w, :] = img[hd, wd, :]
    return dist_img
	
#HSVモデル
def HSV(img):
    
    height, width, channel = img.shape
    
    #画像のフラット
    flat_img = img.reshape(height*width, channel)
    HSV_pixels = np.zeros(flat_img.shape)
    
    #最大・最小ピクセル
    Imax, Imax_arg = np.max(flat_img, axis=1), np.argmax(flat_img, axis=1)
    Imin, Imin_arg = np.min(flat_img, axis=1), np.argmin(flat_img, axis=1)
    
    #HSV変換    
    for color in range(3):
        red_index = np.intersect1d(np.where(Imax_arg==color), np.where(Imax != Imin))
        H = (flat_img[red_index, (color+1)%3] - flat_img[red_index, (color+2)%3]) / (Imax[red_index] - Imin[red_index]) * (np.pi/3) + (color*2/3)*np.pi
        H = np.where(H < 0, H+np.pi*2, H)
        S = (Imax[red_index]-Imin[red_index])/Imax[red_index]
        I = Imax[red_index]
        HSV_pixels[red_index] = np.stack([I, S, H/(2*np.pi)], 1)
        
    zero_indexs = np.where(Imax==Imin)
    HSV_pixels[zero_indexs] = np.stack([Imax[zero_indexs], np.zeros(len(zero_indexs[0])), np.zeros(len(zero_indexs[0]))], 1)
    HSV_pixels = HSV_pixels.reshape(height, width, 3)
    return HSV_pixels

#HSVモデル(逆変換)
def iHSV(img, alpha=1):
    
    height, width, channel = img.shape
    
    #画像のフラット
    flat_img = img.reshape(height*width, channel)
    RGB_pixels = np.zeros(flat_img.shape)
    
    I, S, H = flat_img[:, 0], flat_img[:, 1], flat_img[:, 2]*2*np.pi
    
    h = (3 * H / np.pi).astype(np.int16)
    P = I * (1 - S)
    Q = I * (1 - S*(3/np.pi * H - h))
    T = I * (1 - S*(1 - 3/np.pi * H + h))

    P = np.where(P<0, 0, P)
    Q = np.where(Q<0, 0, Q)
    T = np.where(T<0, 0, T)
        
    for i in range(6): 
        index=np.where(h==i)[0]
        if i == 0: RGB_pixels[index, :] = np.stack([I[index], T[index], P[index]], 1)
        if i == 1: RGB_pixels[index, :] = np.stack([Q[index], I[index], P[index]], 1)
        if i == 2: RGB_pixels[index, :] = np.stack([P[index], I[index], T[index]], 1)
        if i == 3: RGB_pixels[index, :] = np.stack([P[index], Q[index], I[index]], 1)
        if i == 4: RGB_pixels[index, :] = np.stack([T[index], P[index], I[index]], 1)
        if i == 5: RGB_pixels[index, :] = np.stack([I[index], P[index], Q[index]], 1)
   
    RGB_pixels = RGB_pixels.reshape(height, width, 3)*alpha
    RGB_pixels = np.where(RGB_pixels>1.0, 1.0, RGB_pixels)
    return RGB_pixels
	
# モーメント特徴量
@jit
def morment(img, p, q, target=1):
    height, width = img.shape
    
    m = 0
    for h in range(height):
        for w in range(width):
            m += (img[h][w] == target) * (h ** p) * (w ** q)
    return m
	
# 重心
def center_grav(img, target=1):
    m1 = morment(img, 1, 0)
    m2 = morment(img, 0, 0)
    grab_x=m1/m2
    
    m1 = morment(img, 0, 1)
    m2 = morment(img, 0, 0)
    grab_y=m1/m2
    
    return(int(grab_y), int(grab_x))
	
# 主軸方向
def pricipal_axis(img, target=1):
    
    A = (morment(img, 2, 0)-morment(img, 0, 2))/morment(img, 1, 1)
    y1 = (-1*A+np.sqrt(A**2+4))/2
    theta1 = np.arctan(y1)
    
    return np.rad2deg(theta1)