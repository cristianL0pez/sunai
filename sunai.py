import pandas as pd
import matplotlib.pyplot as plt
plt.ioff()
import glob



data=[]
for f in glob.glob("*.xlsx"):
    df=pd.read_excel(f)
    df['active_power_im']=pd.to_numeric(df['active_power_im'], errors='coerce')
    plt.plot(df['fecha_im'],df['active_power_im'])
    plt.savefig('images/{0}.png'.format(f))
    plt.clf()
    sumdia = df['active_power_im'].sum()
    max= sumdia = df['active_energy_im'].max()
    min= sumdia = df['active_energy_im'].min()
    ruta = 'images/{0}.png'.format(f)
    filetxt = open('documentos/sunai.txt','a')
    filetxt.write(f'archivo {f} \n suma diaria {sumdia}\n el valor maximo y minimo del active energy \n maximo : {max}\n minimo: {min}\n ruta de la imagen: {ruta}\n\n\n ')
    filetxt.close()
    data.append(pd.read_excel(f))
print('la suma total del active power por día ',sumdia)