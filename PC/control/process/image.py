import numpy as np

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
	upper_extraction, under_extraction = indexs[0], indexs[-1]
	upper, under = img[upper_extraction], img[under_extraction] 
	
	#θ度算出
	upper_index, under_index = np.where(upper == 1), np.where(under == 1)
	ave_upper_index, ave_under_index = np.average(upper_index), np.average(under_index)
	theta = np.arctan(np.abs((ave_upper_index - ave_under_index)/(upper_extraction - under_extraction)))
	if (ave_upper_index - ave_under_index)/(upper_extraction - under_extraction) > 0: theta = -1 * theta
	theta = theta * 180 / np.pi
	return int(theta), upper_extraction, under_extraction, int(ave_upper_index), int(ave_under_index)
	
#画像中のindex関数
def f1(x, h, w): return (-1*(w/h)*(x-h)).astype(np.int32)
def f2(x, h, w): return ((w/h)*x).astype(np.int32)

#画像中の正面index
def target_indexs(height, width, target_height=60): 
	y = np.arange(target_height, height)
	index1, index2 = f1(y, height, width), f2(y, height, width)
	indexs_flat = np.array([ y[n]*width+index for n, (i1, i2) in enumerate(zip(index1, index2)) for index in range(i1, i2+1)])
	indexs_dim = np.array([ [y[n], index] for n, (i1, i2) in enumerate(zip(index1, index2)) for index in range(i1, i2+1)])
	return indexs_flat, indexs_dim