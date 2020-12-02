from torchvision import models, transforms

class HK_Resize(transforms.Resize):
    def __call__(self, *args, **kwargs):
        img, label = args[0]
        return F.resize(img, self.size, self.interpolation), F.resize(label, self.size, self.interpolation)

class HK_CenterCrop(transforms.CenterCrop):
    def __call__(self, *args, **kwargs):
        img, label = args[0]
        return F.center_crop(img, self.size), F.center_crop(label, self.size)

class HK_RandomResizedCrop(transforms.RandomResizedCrop):
    def __call__(self, *args, **kwargs):
        img, label = args[0]
        i, j, h, w = self.get_params(img, self.scale, self.ratio)
        cropped_img = F.resized_crop(img, i, j, h, w, self.size, self.interpolation)
        cropped_label = F.resized_crop(label, i, j, h, w, self.size, self.interpolation)
        return cropped_img, cropped_label
    
class HK_RandomHorizontalFlip(transforms.RandomHorizontalFlip):
    def __call__(self, *args, **kwargs):
        img, label = args[0]
        if torch.rand(1) < self.p:
            return F.hflip(img), F.hflip(label)
        else:
            return img, label
        
class HK_ToTensor(transforms.ToTensor):
    def __call__(self, *args, **kwargs):
        img, label = args[0]
        label = F.to_grayscale(label)
        return F.to_tensor(img), F.to_tensor(label)
    
class ImageTransform():
    def __init__(self, resize):
        self.data_transform = {
            "train":transforms.Compose([
                HK_RandomResizedCrop(resize, scale=(0.5, 1.0)),
                HK_RandomHorizontalFlip(),
                HK_ToTensor()
            ]),
            "val":transforms.Compose([
                HK_Resize(resize),
                HK_CenterCrop(resize),
                HK_ToTensor(),
            ]),
            "test":transforms.Compose([
                transforms.Resize(resize),
                transforms.CenterCrop(resize),
                transforms.ToTensor(),
            ]) 
        }
        
    def __call__(self, img, label=[], phase="train", height=128, width=416):
        if phase == "test": return self.data_transform[phase](img).view(1, 3, height, width)
        else: return self.data_transform[phase]((img, label))
    

