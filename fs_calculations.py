import numpy as np

def calculate_fs(B, Br, H, Fi, Alfa, SNort_K, SNort_D, SNort_T):
    """
    Fs_K, Fs_D ve Fs_S güvenlik sayıları hesaplanır.
    """
    # Kayma güvenlik sayısı
    ksiH_K = -0.0013*H**3 + 0.0382*H**2 - 0.4404*H + 3.2014
    ksiB_K = 18.765*(B/H)**3 - 44.867*(B/H)**2 + 46.528*(B/H) - 12.7306
    ksiBr_K = 11*(Br/B)**3 - 18.9*(Br/B)**2 + 11.32*(Br/B) - 2.572
    ksiAlfa_K = (-0.34134*(np.tan(np.radians(Alfa))**3) 
                 + 4.3408*(np.tan(np.radians(Alfa))**2) 
                 - 8.11*(np.tan(np.radians(Alfa))) 
                 + 2.3974)
    ksiFi_K = (18.167*(np.tan(np.radians(Fi))**3) 
               - 52.403*(np.tan(np.radians(Fi))**2) 
               + 74.036*(np.tan(np.radians(Fi))) 
               - 27.3276)
    Lk = ksiH_K + ksiB_K + ksiBr_K + ksiAlfa_K + ksiFi_K + SNort_K
    Fs_K = np.sqrt(1/(10**(-Lk/10)))

    # Devrilme güvenlik sayısı
    if (H >= 4) and (H <= 6):
        ksiH_D = -0.251*H - 14.882
    elif (H > 6) and (H <= 10):
        ksiH_D = 0.013*H**2 - 0.325*H + 4.208
    
    ksiB_D = 33.63*(B/H)**3 - 79.956*(B/H)**2 + 87.063*(B/H) - 25.2144
    ksiBr_D = 20.95*(Br/B)**3 - 37.755*(Br/B)**2 + 23.25*(Br/B) -2.493
    ksiAlfa_D = (20.241*(np.tan(np.radians(Alfa))**3) 
                 - 2.1471*(np.tan(np.radians(Alfa))**2) 
                 + 12.028*(np.tan(np.radians(Alfa))) 
                 + 1.364)
    ksiFi_D = (4.6527*(np.tan(np.radians(Fi))**3) 
               - 15.464*(np.tan(np.radians(Fi))**2) 
               + 29.653*(np.tan(np.radians(Fi))) 
               - 10.392)
    Ld = ksiH_D + ksiB_D + ksiBr_D + ksiAlfa_D + ksiFi_D + SNort_D
    Fs_D = np.sqrt(1/(10**(-Ld/10)))

    # Toptan göçme güvenlik sayısı
    ksiH_S = -0.00004*H**3 + 0.0025*H**2 - 0.0403*H + 0.777
    ksiB_S = 0.0494*(B/H)**3 - 2.8889*(B/H)**2 + 10.006*(B/H) - 3.774
    ksiBr_S = 4*(Br/B)**3 - 7.8*(Br/B)**2 + 5.2*(Br/B) + 1.839 - 2.443
    ksiAlfa_S = (58.99*(np.tan(np.radians(Alfa))**3) 
                 - 21.487*(np.tan(np.radians(Alfa))**2) 
                 + 5.6187*(np.tan(np.radians(Alfa))) 
                 + 0.204)
    ksiFi_S = (14.663*(np.tan(np.radians(Fi))**3) 
               - 39.803*(np.tan(np.radians(Fi))**2) 
               + 46.387*(np.tan(np.radians(Fi))) 
               - 15.669)
    Ls = ksiH_S + ksiB_S + ksiBr_S + ksiAlfa_S + ksiFi_S + SNort_S
    Fs_S = np.sqrt(1/(10**(-Ls/10)))

    return Fs_K, Fs_D, Fs_S
