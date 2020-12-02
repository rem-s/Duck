import torch
import torchvision
import torch.nn as nn

class Conv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.unit = nn.Sequential(
            nn.Conv2d(self.in_channels, self.in_channels, kernel_size=3, padding=1, groups=self.in_channels),
            nn.BatchNorm2d(self.in_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(self.in_channels, self.out_channels, kernel_size=1, padding=0),
            nn.BatchNorm2d(self.out_channels),
            nn.ReLU(inplace=True),
        )
    def forward(self, x):
        return self.unit(x)
    
class Down(nn.Module):
    def __init__(self, in_channels):
        super().__init__()
        self.in_channels = in_channels
        self.unit = nn.Sequential(
            nn.Conv2d(self.in_channels, self.in_channels, kernel_size=3, padding=1, groups=self.in_channels, stride=2),
            nn.BatchNorm2d(self.in_channels),
            nn.ReLU(inplace=True),
        )
    def forward(self, x):
        return self.unit(x)
    
class Up(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.unit = nn.Sequential(
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),
        )
    def forward(self, x):
        return self.unit(x)
    
class In(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(In, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        
        self.unit = nn.Sequential(
            nn.Conv2d(self.in_channels, self.out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(self.out_channels),
            nn.ReLU(inplace=True),
        )
    def forward(self, x):
        return self.unit(x)
    
class Out(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        
        self.unit = nn.Sequential(
            nn.Conv2d(self.in_channels, self.out_channels, kernel_size=1),
        )
    def forward(self, x):
        return self.unit(x)

class SEGNET(nn.Module):
    def __init__(self, n_channels, n_classes):
        super(SEGNET, self).__init__()
        self.n_channels = n_channels
        self.n_classes = n_classes
        
        self.inconv = In(self.n_channels, 32)
        self.down1 = Down(32)
        
        self.conv1 = Conv(32, 64)
        self.down2 = Down(64)
        
        self.conv2 = Conv(64, 128)
        self.down3 = Down(128)
        
        self.conv3 = Conv(128, 256)
        
        self.conv4 = Conv(256, 128)
        self.up1 = Up()
        
        self.conv5 = Conv(256, 128)
        self.conv6 = Conv(128, 64)
        self.up2 = Up()
        
        self.conv7 = Conv(128, 64)
        self.conv8 = Conv(64, 32)
        self.up3 = Up()
        
        self.conv9 = Conv(64, 32)
        self.outconv = Out(32, self.n_classes)
    
    def forward(self, x):
        
        x0 = self.inconv(x)
        x1 = self.down1(x0)
        
        x2 = self.conv1(x1)
        x3 = self.down2(x2)
        
        x4 = self.conv2(x3)
        x5 = self.down3(x4)
        
        x6 = self.conv3(x5)
        
        x7 = self.conv4(x6)
        x8 = self.up1(x7)
        
        x9 = self.conv5(torch.cat([x4, x8], 1))
        x10 = self.conv6(x9)
        x11 = self.up2(x10)
        
        x12 = self.conv7(torch.cat([x2, x11], 1))
        x13 = self.conv8(x12)
        x14 = self.up3(x13)
        
        x15 = self.conv9(torch.cat([x0, x14], 1))
        out = self.outconv(x15)
        return out