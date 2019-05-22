from PIL import Image



for i in range(1, 8404):
    img = Image.open('./back_tra/'+str(i)+'.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 140 and item[1] == 250 and item[2] == 5:
            #newData.append((255, 255, 255, 0))#투명화 코드
            newData.append((0, 0, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("./final2/" + str(i)+".png")