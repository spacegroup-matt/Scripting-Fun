#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MaxNLocator
from scipy.interpolate import splrep, splev

width = 0.8

#MUE				            MSE		
#PHAST-TT*	PHAST*	PHAST		PHAST-TT*	PHAST*	PHAST

C2H6_C2H6_C2H6 = [0.480921298250999, 0.489897035966024, 0.463316005999636, -0.189435857491501, 0.011269726387855, -0.126875865660527]
C2H6_C2H6_C2H4 = [0.647735521368268, 0.831458207304431, 0.790300969032204, 0.116781641981304, 0.324489113450006, 0.262111631629933]
C2H6_C2H6_C2H2 = [0.732278589888828, 1.29578232955585, 1.2456060482908, 0.113553048134039, 0.186363137687121, 0.146543005244547]
C2H6_C2H4_C2H4 = [0.797445174607282, 1.42406274800196, 1.3958441933393, -0.042257584598894, 0.351602065992494, 0.363630882827102]
C2H6_C2H4_C2H2 = [0.831002051224987, 1.22409057599764, 1.16817552922599, 0.29955488665937, 0.334891026281484, 0.330002512631785]
C2H6_C2H2_C2H2 = [0.802300650050844, 1.56191012049862, 1.50469630024674, 0.267198738053375, 0.245988773186753, 0.216254093676975]
C2H4_C2H4_C2H4 = [0.737784448517327, 1.23170968404042, 1.19750596529137, -0.201966604302165, 0.117673233649971, 0.153472029972026]
C2H4_C2H4_C2H2 = [0.952952619876513, 1.73543870403081, 1.70705941445849, -0.20312369050518, 0.178490060485629, 0.218724669590594]
C2H4_C2H2_C2H2 = [0.835778021482067, 1.77971599682716, 1.71254795538702, 0.080708539504405, 0.574811015552278, 0.566100731569556]
C2H2_C2H2_C2H2 = [0.675755852733675, 1.54530633246127, 1.49846285393422, -0.322970699217541, 0.130904796374836, 0.064830036823922]

phahst_mue = [C2H6_C2H6_C2H6[0], C2H6_C2H6_C2H4[0], C2H6_C2H6_C2H2[0], C2H6_C2H4_C2H4[0], C2H6_C2H4_C2H2[0], C2H6_C2H2_C2H2[0], C2H4_C2H4_C2H4[0], C2H4_C2H4_C2H2[0], C2H4_C2H2_C2H2[0], C2H2_C2H2_C2H2[0]]
phast_star_mue = [C2H6_C2H6_C2H6[1], C2H6_C2H6_C2H4[1], C2H6_C2H6_C2H2[1], C2H6_C2H4_C2H4[1], C2H6_C2H4_C2H2[1], C2H6_C2H2_C2H2[1], C2H4_C2H4_C2H4[1], C2H4_C2H4_C2H2[1], C2H4_C2H2_C2H2[1], C2H2_C2H2_C2H2[1]]
phast_mue = [C2H6_C2H6_C2H6[2], C2H6_C2H6_C2H4[2], C2H6_C2H6_C2H2[2], C2H6_C2H4_C2H4[2], C2H6_C2H4_C2H2[2], C2H6_C2H2_C2H2[2], C2H4_C2H4_C2H4[2], C2H4_C2H4_C2H2[2], C2H4_C2H2_C2H2[2], C2H2_C2H2_C2H2[2]]
phahst_mse = [C2H6_C2H6_C2H6[3], C2H6_C2H6_C2H4[3], C2H6_C2H6_C2H2[3], C2H6_C2H4_C2H4[3], C2H6_C2H4_C2H2[3], C2H6_C2H2_C2H2[3], C2H4_C2H4_C2H4[3], C2H4_C2H4_C2H2[3], C2H4_C2H2_C2H2[3], C2H2_C2H2_C2H2[3]]
phast_star_mse = [C2H6_C2H6_C2H6[4], C2H6_C2H6_C2H4[4], C2H6_C2H6_C2H2[4], C2H6_C2H4_C2H4[4], C2H6_C2H4_C2H2[4], C2H6_C2H2_C2H2[4], C2H4_C2H4_C2H4[4], C2H4_C2H4_C2H2[4], C2H4_C2H2_C2H2[4], C2H2_C2H2_C2H2[4]]
phast_mse = [C2H6_C2H6_C2H6[5], C2H6_C2H6_C2H4[5], C2H6_C2H6_C2H2[5], C2H6_C2H4_C2H4[5], C2H6_C2H4_C2H2[5], C2H6_C2H2_C2H2[5], C2H4_C2H4_C2H4[5], C2H4_C2H4_C2H2[5], C2H4_C2H2_C2H2[5], C2H2_C2H2_C2H2[5]]

labels = ['C2H6_C2H6_C2H6', 'C2H6_C2H6_C2H4', 'C2H6_C2H6_C2H2', 'C2H6_C2H4_C2H4', 'C2H6_C2H4_C2H2', 'C2H6_C2H2_C2H2', 'C2H4_C2H4_C2H4', 'C2H4_C2H4_C2H2', 'C2H4_C2H2_C2H2', 'C2H2_C2H2_C2H2']
x = array([i for i, _ in enumerate(labels)])

#plt.bar(x-1./3.*width, phahst_mue, width/3., label='PHAHST')
#plt.bar(x, phast_star_mue, width/3., label='PHAST*')
#plt.bar(x+1./3.*width, phast_mue, width/3., label='PHAST')

plt.bar(x-1./3.*width, phahst_mse, width/3., label='PHAHST')
plt.bar(x, phast_star_mse, width/3., label='PHAST*')
plt.bar(x+1./3.*width, phast_mse, width/3., label='PHAST')

plt.ylabel("Mean Signed Error")
plt.xlabel("Trimer Composition")

plt.xticks(x, labels)
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.legend(frameon=False)

plt.tight_layout()

#plt.show()
plt.savefig('c2_mse.eps', format='eps')
