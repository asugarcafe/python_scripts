# -*- coding: utf-8 -*-

# https://developer.gimp.org/api/3.0/libgimp/method.Image.merge_down.html
# https://developer.gimp.org/api/3.0/libgimp/class.TextLayer.html

#run first
images = Gimp.get_images()
image = images[0]
layers = image.get_layers()
text_layer = layers[0]
layer_ind = []
for index in range(1,len(layers)):
    layer_ind.append(index)
    
#run next
for n in reversed(layer_ind):
    new_layer = text_layer.copy()
    image.insert_layer(new_layer,None,n) #adds layer at the top
    image.merge_down(new_layer, Gimp.MergeType.EXPAND_AS_NECESSARY)
    