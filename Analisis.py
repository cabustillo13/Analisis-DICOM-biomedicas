import imageio
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

##INICIACION
il1 = imageio.imread("./DICOM/TumorBrain1.dcm")
il2 = imageio.imread("./DICOM/TumorBrain2.dcm")

# Error
err = il1 - il2

#Error absoluto
absErr = np.abs(err)

#Error absoluto medio
meanErr = np.mean(absErr)
print(meanErr)

#Graficar
f, axes = plt.subplots(1, 4, figsize=(8, 5))
axes[0].imshow(il1)
axes[0].set_title('TumorBrain1')
axes[1].imshow(il2)
axes[1].set_title('TumorBrain2')
axes[2].imshow(err)
axes[2].set_title('Error')
axes[3].imshow(absErr)
axes[3].set_title('Error Absoluto')

for ax in axes:
    ax.axis('off')
plt.show()

## MINIMIZAR COSTO DE LA FUNCION
# Se busca alinear la imagen al1 con respecto a al2
xfm = ndi.shift(il1, shift = (-8,-8))
xfm = ndi.rotate(xfm, -25, reshape = False)
# Hay que saber mas o menos cual es el valor para rotar y traladar para obtener el menor costo de la funcion

# Calcular el costo
abs_err = np.abs(xfm - il2)
mean_abs_err = np.mean(abs_err)
print(mean_abs_err)

## INSERSECCION EN LA UNION 
## IOU = (il1 n il2)/(il1 u il2)

mask1 = il1 > 0
mask2 = il2 > 0

interseccion = mask1 & mask2
union = mask1 | mask2 
IOU = interseccion.sum()/union.sum()
print(IOU)

#Graficar
f, axes = plt.subplots(1, 2, figsize=(8, 5))
axes[0].imshow(mask1)
axes[0].set_title('Mask1')
axes[1].imshow(mask2)
axes[1].set_title('Mask2')

for ax in axes:
    ax.axis('off')
plt.show()
 
#Bibliografia: https://www.datacamp.com/courses/biomedical-image-analysis-in-python
