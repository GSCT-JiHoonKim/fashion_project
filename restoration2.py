from PIL import Image

#hat = (0, 255, 255)
#hair = (255, 0, 255)
gloves = (255, 255, 0)
sunglasses = (252, 112, 222)
u_clothes = (255, 255, 170)
scarf = (146, 208, 80)
skirt = (255, 192, 0)
#l_arm = (129, 255, 129)
#r_arm = (0, 246, 82)
#l_leg = (255, 0, 85)
coat = (85, 255, 255)
socks = (87, 167, 252)
pants = (105, 45, 190)
jumpsuits = (153, 74, 202)
#r_leg = (255, 85, 85)
l_shoe = (0, 85, 255)
r_shoe = (85, 85, 255)
background = (0, 0, 0)
dress = (170, 255, 255)
#face = (255, 85, 170)

img_num = 1

for a in range(1, 3618):
    #for i in range(1, 3618):

    #original = Image.open('./real/26_real_A.png')
    #processing = Image.open('./fake/26_fake_B.png').resize(original.size)
    original = Image.open('./real/'+str(img_num)+'_real_A.png')
    processing = Image.open('./fake/'+str(img_num)+'_fake_B.png').resize(original.size)


    pixels1 = original.load()
    pixels2 = processing.load()
    for i in range(processing.size[0]):
        for j in range(processing.size[1]):
            if pixels2[i,j] != gloves and pixels2[i, j] != sunglasses and pixels2[i,j] != u_clothes and  \
                    pixels2[i, j] != scarf and pixels2[i, j] != skirt and pixels2[i, j] != coat and pixels2[i, j] != socks \
                    and pixels2[i, j] != pants and pixels2[i, j] != jumpsuits and pixels2[i, j] != l_shoe \
                    and pixels2[i, j] != r_shoe and pixels2[i, j] != dress:
                pixels1[i,j] = (0, 0 ,0)
    #original.show()
    original.save(str(img_num)+'.png')
    img_num += 1