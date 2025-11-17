import imageio.v3 as iip
filenames=['team-pic1.jpg', 'team-pic2.jpg']
images=[]
for filename in filenames:
    images.append(iip.imread(filename))
iip.imwrite('test.GIF', images, duration=500, loop=0) 
