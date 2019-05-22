from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976, delta_e_cie2000
from colormath.color_objects import XYZColor, sRGBColor,LabColor
from colormath.color_conversions import convert_color
import cv2
import csv
'''
# Reference color.
color1 = LabColor(lab_l=80.3860502814096, lab_a=31.589675033942164, lab_b=-2.9802900213355743)
# Color to be compared to the reference.
color2 = LabColor(lab_l=75.02850788843229, lab_a=37.28537148980432, lab_b=5.002160736002792)
# This is your delta E value as a float.
delta_e = delta_e_cie2000(color1, color2)
print(delta_e)

color=[252, 177, 205]
rgb = sRGBColor(rgb_r=color[0], rgb_g=color[1], rgb_b=color[2], is_upscaled=True)
xyz = convert_color(rgb, XYZColor)
lab = convert_color(xyz,LabColor)

print(rgb, xyz, lab)
'''
#csv file
f=open('tset.csv', 'w', encoding='utf-8', newline='')
wr=csv.writer(f)

#pantone color LAB values
pantone = { 'fiesta':[221, 65, 50], 'jester_red':[158, 16, 48], 'turmeric':[255, 133, 15], 'living_coral':[255, 111, 97], 'pink_peacock':[198, 35, 104], 'pepper_stem':[141,148,64], 'aspen_gold':[255, 214, 98], 'princess_blue': [0, 83, 156],
            'toffee': [117, 81, 57], 'mango_mojito':[214, 157, 48], 'terrarium_moss':[97, 98, 71], 'sweet_lilac':[232, 181, 206], 'soybean':[210, 194, 157], 'eclipse':[53, 49, 72], 'sweet_corn':[240, 235, 215], 'brown_granite':[97, 85, 80]}
pantone_lab_list = []
num=0



#panton color value RGB to LAB
for v in pantone.keys():
    #wr.writerow([v])
    print(v)
    tmp=pantone.get(v)
    print(tmp)
    pantone_rgb = sRGBColor(rgb_r=tmp[0], rgb_g=tmp[1], rgb_b=tmp[2], is_upscaled=True)
    pantone_xyz = convert_color(pantone_rgb, XYZColor)
    pantone_lab = convert_color(pantone_xyz, LabColor)
    pantone_lab_list += [pantone_lab]

print('###set done###')
key_list=list(pantone.keys())

for k in range(0, 16):
    wr.writerow(key_list[k])
    print(key_list[k])

#color chip
    for i in range(1, 8338):
        try:
            image = cv2.imread("./color_chip/" + str(i) + ".png")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #print(image.shape)

            #init
            image_past = [image[0][0][0], image[0][0][1], image[0][0][2]]
            image_cache_list = []
            image_cache_list += [[image[0][0][0], image[0][0][1], image[0][0][2]]]
            image_lab_list =[]

            #extract color chip rgb value
            for a in range(300):
                isNew = False

                image_present = [image[0][a][0], image[0][a][1], image[0][a][2]]
                if not ((image_past[0] == image_present[0]) and (image_past[1] == image_present[1]) and (image_past[2] == image_present[2])):
                    isNew = True

                if isNew:
                    image_cache_list += [image_present.copy()]

                image_past = image_present
            #print(image_cache_list)

            for j in range(0, 4):
                try:
                    color_chip_rgb = sRGBColor(rgb_r=image_cache_list[j][0], rgb_g=image_cache_list[j][1], rgb_b=image_cache_list[j][2], is_upscaled=True)
                    color_chip_xyz = convert_color(color_chip_rgb, XYZColor)
                    color_chip_lab = convert_color(color_chip_xyz, LabColor)
                    image_lab_list += [color_chip_lab]
                    #print('my color chip', color_chip_rgb, color_chip_xyz, color_chip_lab)
                #print(pantone_lab_list[0], image_lab_list[0])
                    delta_e = delta_e_cie2000(pantone_lab_list[k], image_lab_list[j])
                    if delta_e<=5:
                        print('%d번째 컬러칩의 %d째 칸은 %f 만큼의 delta_e값 차이가 납니다.' %(i, j, delta_e) )
                        wr.writerow([i, j, delta_e])
                    #print(delta_e)
                except IndexError as e2:
                    continue

            # for image_cache in image_cache_list:
            #     print(image_cache)
        except cv2.error as e:
            continue
        num+=1
    # delta_e = delta_e_cie2000(lab, flab)
    # print(delta_e)
f.close()

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
'''
# Red Color
color1_rgb = sRGBColor(80.3860502814096, 31.589675033942164, -2.9802900213355743)

# Blue Color
color2_rgb = sRGBColor(0.0, 0.0, 1.0);

# Convert from RGB to Lab Color Space
color1_lab = convert_color(color1_rgb, LabColor);

# Convert from RGB to Lab Color Space
color2_lab = convert_color(color2_rgb, LabColor);

# Find the color difference
delta_e = delta_e_cie2000(color1_lab, color2_lab);

print("The difference between the 2 color = ", delta_e)
'''

# from colormath.color_objects import LabColor, sRGBColor, XYZColor, AdobeRGBColor
# from colormath.color_conversions import convert_color
# import cv2
# import scipy.misc
#
#
# coral = cv2.imread('./coral.png')
# brightLAB = cv2.COLOR_RGB2LAB(coral, cv2.COLOR_BGR2LAB)
#
# cv2.cvtColor(coral, coral2, cv2.COLOR_RGB2LAB)
#
# # coral = [155, 155, 155]
# # brightLAB = cv2.COLOR_RGB2Lab(coral, cv2.COLOR_BGR2LAB)
# # print(coral)
# # print(brightLAB)
# scipy.misc.imsave('./coral1.png', brightLAB)
