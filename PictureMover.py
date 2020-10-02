#This program will organize images from your downloads
#based on their extension. 

import os

name = os.getlogin() #get your users name to traverse folders quickly

#quick folder name shortcut so you're not typing this over and over
fold_dnld = 'C:\\Users\\'+name+'\\Downloads\\'
fold_pic = 'C:\\Users\\'+name+'\\pictures\\'

#checks if your folders exist and makes them if they don't
if not os.path.exists(fold_pic+'png\\'):
    os.makedirs(fold_pic+'png\\')
if not os.path.exists(fold_pic+'jpg\\'):
    os.makedirs(fold_pic+'jpg\\')
if not os.path.exists(fold_pic+'gif\\'):
    os.makedirs(fold_pic+'gif\\')

#moves to your downloads folder
os.chdir(fold_dnld)
for f in os.listdir(): #traverses the lists of files
    f_name, f_ext = os.path.splitext(f) #splits it into (file name, file extention)
    
    #checks your file extension to see what it is and moves it if its one of these 
    if f_ext == '.png':
        f_name = f_name.strip()
        f_ext = f_ext.strip()
        new_name = fold_pic+'png\\{}{}'.format(f_name,f_ext)
        os.rename(f, new_name)
    elif f_ext == '.jpg' or f_ext == '.jpeg':
        f_name = f_name.strip()
        f_ext = f_ext.strip()
        new_name = fold_pic+'jpg\\{}{}'.format(f_name,f_ext)
        os.rename(f, new_name)
    elif f_ext == '.gif':
        f_name = f_name.strip()
        f_ext = f_ext.strip()
        new_name = fold_pic+'gif\\{}{}'.format(f_name,f_ext)
        os.rename(f, new_name)
