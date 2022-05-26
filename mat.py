from matplotlib import pyplot as plt

la = ["Gilber", "Harison", 'Kevin']
data =[90,10,5]
ex = [0.0,0.0,1]
plt.pie(data,labels=la,explode=ex )
plt.show()
