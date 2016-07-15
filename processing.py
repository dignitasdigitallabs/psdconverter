from psd_tools import PSDImage
from PIL import Image
import os
import shutil
import sys
name_folder = raw_input('Enter the name of the folder : ')  #Inputting folder name
psds = raw_input('Enter the name of PSD FILE : ')   #Inputting the PSD name
psd = open(psds,'r')     
def read(fp):   #Checking if the loaded document is PSD or not
    signature = fp.read(4)
    if signature != b'8BPS':
        print 'This is not a PSD'
        quit()
read(psd)        
psd = PSDImage.load(psds)   #Loading the PSD
dir = os.path.dirname(os.path.abspath(psds))    #Getting the path of the loaded PSD
dir = dir +'\\'+ name_folder
temp = dir
if not os.path.exists(dir): #Creating a Directory
    os.makedirs(dir)   
os.chdir(dir)
print psd.header
layer_psd = psd.layers  #Getting the layers of PSD stored in a variable
print len(layer_psd)    #Calculating the number  of layers in a group
print layer_psd
count1 = 0
i = 0
j = 0
while (count1 < len(layer_psd)):    #Iterating through the group to extract the layers
    group1 = psd.layers[count1] #Taking a layer at a time
    count4 = count1 + 1
    try:
        group2 = psd.layers[count4]
    except IndexError:
        print 'Index out of Bound'    
    if( group1.name == group2.name):    #Checking if two groups have the same name 
        os.chdir(temp)  #Changing the directory
        dir = temp
        dir = dir+'\\'+group1.name+str(j)   #Changing the name of one of the groups by appending an integer
        if not os.path.exists(dir): #Creating a sub directory to store the layers 
            os.makedirs(dir)    
        os.chdir(dir)        
        j = j + 1
    else:   #In case two consecutive groups have different names
        os.chdir(temp) 
        dir = temp
        dir = dir+'\\'+group1.name
        if not os.path.exists(dir):
            os.makedirs(dir)
        os.chdir(dir)    
    try:
        group_image = group1.as_PIL()   #Converting the layer as an Image
        group_image.save(group1.name+'.png','PNG')  #Saving the Image in .png extension
    except AttributeError:  #Raised in case of failure of attribute reference or assignment.
        print 'Height and Width are null'
        print group1.name
    except ValueError: #Raised in case of height = width = 0
        print 'Value either too small or too large'
        print group1.name
    if hasattr(group1, 'layers'):   #Checking for layers in a group
        count2 = 0
        while( count2 < len(group1.layers)):    #Iterating through the layers 
            layer = group1.layers[count2]   #Accessing one layer at a time
            name = layer.name   #Assigning name of the layer in name variable
            #print name
            try:
                    layer_image = layer.as_PIL()    #Extracting layer as an Image
                    layer_image.save(layer.name+'.png','PNG')   #Saving the Image in .png extension
            except KeyError:    #Raised when the specified key is not found in the dictionary.
                layer_image.save(layer.name+'.jpg','JPEG') #Saving the layer in .jpg extension
                #print layer.name
                print 'Saved in JPEG'
            except AttributeError:  #Raised in case of failure of attribute reference or assignment.
                print 'Invalid assignment'
                #print layer.name
            except IOError: #Raised in case of text occurs
                print 'text occurred'
                #print layer.name
                file = open('text.txt','a+') #Creating a text file to store the text and appending the text in single text file occurring in a group
                file.write(name.encode('ascii', 'ignore'))  #Writitng in a text file
                file.close()    #Closing the text file
            except ValueError: #Raised when Value either too small or too large
                print 'Value either too small or too large'
                #print layer.name
                if ( layer.bbox.height == 0 and layer.bbox.width == 0):
                    print 'Empty layer'
                else:
                    print 'Image is presesnt'
            if hasattr(layer, 'layers'): #Checking for more layers
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

######Function to Resize the Extracted Layers######

def assetsizes(size,dir):   #Size and dir are taken as Parameters
    name_folder = str(size) #Assigning a name to the new folder which contains Resized images     
    outfile = dir + "\\" + name_folder
    if not os.path.exists(outfile): #Creating a directory
        os.makedirs(outfile)
    os.chdir(outfile)    
    #print os.walk(dir)
    #print [x[0] for x in os.walk(dir)]
    subdir = os.listdir(dir)    #Gathering the list of all the groups whose layers are to be resized
    print len(subdir)
    count = 0
    while( count < len(subdir)): #Iterating through the layers and resizing them 
        infile = dir + "\\" + str(subdir[count])    
        os.chdir(outfile)
        outfile2 = outfile + "\\" + str(subdir[count])
        if not os.path.exists(outfile2):    #Creating a sub directory with the same group name
            os.makedirs(outfile2)
        os.chdir(outfile2)    #Changing the directory
        os.listdir(infile)
        print os.listdir(infile) #Getting the layers in the sub directory
        subsub = os.listdir(infile)
        count2 = 0
        while( count2 < len(subsub)): #Iterating through the layers extracted
            inin = infile + "\\"+str(subsub[count2])
            print inin
            if inin.endswith('.png') | inin.endswith('.jpg'):   #Resizing Images only with .png or .jpg extension
                try:
                    im = Image.open(inin)   #Opening the image
                    im.thumbnail(size1, Image.ANTIALIAS)    #Changing the Size of the image without changing the aspect ratio
                    im.save(str(subsub[count2])+'.png', "PNG")  #Saving the Resized image in .png extension
                except IOError: #Raised if Name of the image contains Special characters
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

