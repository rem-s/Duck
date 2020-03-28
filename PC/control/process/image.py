import numpy as np

#大津の二値化
def Otsu(img):
    
    #初期化
    img_flat = img.reshape(-1)
    Imax, Imin = np.max(img), np.min(img)
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
    binarize_img = np.where(img_flat <= otsu_thr, 0, 1).reshape(img.shape)
    
    return binarize_img
	
#中央値による二値化
def Med(img):
	
	#初期化
	img_flat = img.reshape(-1)
	Imedian = np.median(img_flat)
	
	#二値化画像生成
	binarize_img = np.where(img_flat <= Imedian, 0, 1).reshape(img.shape)
	
	return binarize_img
	
#平均値による二値化
def Mean(img):
	
	#初期化
	img_flat = img.reshape(-1)
	Imedian = np.mean(img_flat)
	
	#二値化画像生成
	binarize_img = np.where(img_flat <= Imedian, 0, 1).reshape(img.shape)
	
	return binarize_img
	
#近傍ピクセルの探索
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
	
#画像8近傍ラベリング
def labeling(img):

	#初期化
	label = 0
	height, width = img.shape
	label_img = np.zeros(img.shape)
	lookup_table = np.arange(width * height)
	
	#画像探索
	for h in range(height):
		for w in range(width):
			
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
	for h in range(height):
		for w in range(width):
			label_img[h][w] = lookup_table[int(label_img[h][w])]
	
	return label_img
	
#画像下半分面積比較
def under_comarea(img):
    height, width = img.shape
    img_flat = img.reshape(-1)
	
	#画像下半分のみ取得
    img_under_flat = img[int(height/2):,:].reshape(-1)
    areas = np.array([len(np.where(img_under_flat == i)[0]) for i in np.unique(img_under_flat)[1:]])
    value = np.unique(img_under_flat)[np.argmax(areas)+1]
    return np.where(img_flat == value, 1, 0).reshape(img.shape)
