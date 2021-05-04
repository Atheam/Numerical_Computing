import numpy as np
import matplotlib.pyplot as plt
from binary_img import annealing


def energy8_pull(img,row,col):
    n = img.shape[0]
    return 9 - np.sum(img[max(0,row-1):min(row+1,n-1),max(0,col-1):min(col+1,n-1)])

def energy8_push(img,row,col):
    n = img.shape[0]
    return np.sum(img[max(0,row-1):min(row+1,n-1),max(0,col-1):min(col+1,n-1)])

def energy_lines(img,row,col):
    n = img.shape[0]
    ll = img[max(0,row-1),max(0,col-1)]
    ur = img[min(n-1,row+1),min(n-1,col+1)]
    ul = img[min(n-1,row+1),max(0,col-1)]
    lr = img[max(0,row-1),min(n-1,col+1)]

    return ll + ur + ul + lr

def energy_chessboard(img,row,col):
    n = img.shape[0]
    ll = img[max(0,row-1),max(0,col-1)]
    ur = img[min(n-1,row+1),min(n-1,col+1)]
    ul = img[min(n-1,row+1),max(0,col-1)]
    lr = img[max(0,row-1),min(n-1,col+1)]
    
    return 4 - ll - ur - ul - lr

def energy_stripes(img,row,col):
    n = img.shape[0]
    ll = img[max(0,row-1),max(0,col-1)]
    ur = img[min(n-1,row+1),min(n-1,col+1)]
    ul = img[min(n-1,row+1),max(0,col-1)]
    lr = img[max(0,row-1),min(n-1,col+1)]

    return 8 - ul - lr

def energy8_16(img,row,col):
    n = img.shape[0]
    inner = np.sum(img[max(0,row-1):min(row+1,n-1),max(0,col-1):min(col+1,n-1)])
    outer = np.sum(img[max(0,row-2):min(row+2,n-1),max(0,col-2):min(col+2,n-1)]) - inner
    return outer - inner


def test_binary_image(n,rho,T,max_iter,rate,energy_func):

    init_img = np.random.choice([0,1],size = (n,n),p =[1-rho,rho])


    after_img,costs,temp = annealing(init_img, T, max_iter, rate,energy_func)
    fig,ax = plt.subplots(2,2)

    ax[0,0].imshow(init_img)
    ax[0,0].set_title("Initial image")
    ax[0,1].imshow(after_img)
    ax[0,1].set_title("Image after annealing")
    ax[1,0].plot(temp)
    ax[1,0].set_title("Temperature")
    ax[1,1].plot(costs)
    ax[1,1].set_title("Cost")
    plt.tight_layout()
    plt.show()



test_binary_image(20, 0.3, 1, 25000, 0.995,energy_stripes)