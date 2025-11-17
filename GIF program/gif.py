import imageio.v3 as iio
filenames=['team-pic1.jpg', 'team-pic2.jpg']
images=[]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('test.GIF', images, duration=500, loop=0) 
