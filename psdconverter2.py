from psd_tools import PSDImage
from PIL import Image
import os
import shutil
import sys
name_folder = raw_input('Enter the name of the folder : ')
psds = raw_input('Enter the name of PSD FILE : ')
psd = open(psds,'r') 
def read(fp):
    signature = fp.read(4)
    if signature != b'8BPS':
        print 'This is not a PSD'
        quit()
read(psd)        
psd = PSDImage.load(psds)
dir = os.path.dirname(os.path.abspath(psds))
dir = dir +'\\'+ name_folder
temp = dir
if not os.path.exists(dir):
    os.makedirs(dir)   
os.chdir(dir)
print psd.header
layer_psd = psd.layers
print len(layer_psd)
print layer_psd
count1 = 0
i = 0
j = 0
while (count1 < len(layer_psd)):
    group1 = psd.layers[count1]
    count4 = count1 + 1
    try:
        group2 = psd.layers[count4]
    except IndexError:
        print 'Index out of Bound'    
    if( group1.name == group2.name):    
        os.chdir(temp)
        dir = temp
        dir = dir+'\\'+group1.name+str(j)
        if not os.path.exists(dir):
            os.makedirs(dir)    
        os.chdir(dir)        
        j = j + 1
    else:
        os.chdir(temp)
        dir = temp
        dir = dir+'\\'+group1.name
        if not os.path.exists(dir):
            os.makedirs(dir)
        os.chdir(dir)    
    try:
        group_image = group1.as_PIL()
        group_image.save(group1.name+'.png','PNG')
    except AttributeError:
        print 'Invalid assignment'
        print group1.name
    except ValueError:
        print 'Value either too small or too large'
        print group1.name
    if hasattr(group1, 'layers'):
        count2 = 0
        while( count2 < len(group1.layers)):
            layer = group1.layers[count2]
            name = layer.name
            #print name
            try:
                    layer_image = layer.as_PIL()
                    layer_image.save(layer.name+'.png','PNG')
            except KeyError:
                layer_image.save(layer.name+'.jpg','JPEG')
                #print layer.name
                print 'Saved in JPEG'
            except AttributeError:
                print 'Invalid assignment'
                #print layer.name
            except IOError:
                print 'text occurred'
                #print layer.name
                file = open('text.txt','a+')
                file.write(name.encode('ascii', 'ignore'))
                file.close()
            except ValueError:
                print 'Value either too small or too large'
                #print layer.name
                if ( layer.bbox.height == 0 and layer.bbox.width == 0):
                    print 'Empty layer'
                else:
                    print 'Image is presesnt'
            if hasattr(layer, 'layers'):
                count3 = 0
                while( count3 < len(layer.layers)):
                    layers = layer.layers[count3]
                    name = layers.name
                    #print name
                    try:
                        layers_image = layers.as_PIL()
                        layers_image.save(layers.name+'.png','PNG')
                    except KeyError:
                        layers_image.save(layers.name+'.jpg','JPEG')
                        #print layer.name
                        print 'Saved in JPEG'
                    except AttributeError:
                        print 'Invalid assignment'
                        #print layer.name
                    except IOError:
                        print 'text occurred'
                        #print layer.name
                        file = open('text2.txt','a+')
                        file.write(name.encode('ascii', 'ignore'))
                        file.close()
                    except ValueError:
                        print 'Value either too small or too large'
                        #print layer.name
                        if ( layers.bbox.height == 0 and layers.bbox.width == 0):
                            print 'Empty layer'
                        else:
                            print 'Image is present'
                    count3 = count3 + 1        
            count2 = count2 + 1
    count1 = count1 + 1


size1 = 50, 50
size2 = 100, 100
size3 = 150, 150

def assetsizes(size,dir):
    name_folder = str(size)
    outfile = dir + "\\" + name_folder
    if not os.path.exists(outfile):
        os.makedirs(outfile)
    os.chdir(outfile)    
    #print os.walk(dir)
    #print [x[0] for x in os.walk(dir)]
    subdir = os.listdir(dir)
    print len(subdir)
    count = 0
    while( count < len(subdir)):
        infile = dir + "\\" + str(subdir[count])
        os.chdir(outfile)
        outfile2 = outfile + "\\" + str(subdir[count])
        if not os.path.exists(outfile2):
            os.makedirs(outfile2)
        os.chdir(outfile2)    
        os.listdir(infile)
        print os.listdir(infile)
        subsub = os.listdir(infile)
        count2 = 0
        while( count2 < len(subsub)):
            inin = infile + "\\"+str(subsub[count2])
            print inin
            if inin.endswith('.png') | inin.endswith('.jpg'):
                try:
                    im = Image.open(inin)
                    im.thumbnail(size1, Image.ANTIALIAS)
                    im.save(str(subsub[count2])+'.png', "PNG")
                except IOError:
                    print 'Change the name'
            count2 = count2 + 1
        count = count + 1

dir = temp
assetsizes(size1,dir)



                                                                                                                                                                            

#print layer_psd
#group = psd.layers[0]
#print group.name
#print group.visible
#print group.opacity
#from psd_tools.constants import BlendMode
#print group.blend_mode == BlendMode.NORMAL
#print group.layers
#layer = group.layers[0]
#print layer.name
#print layer.bbox

