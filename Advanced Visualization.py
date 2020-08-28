# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:38:28 2020

@author: AKshay
"""
#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import the csv dataset
dataset = pd.read_csv("P4-Movie-Ratings.csv")

#rename columns
dataset.columns= ['Film','Genre','CriticRating','AudienceRating','BudgetMillions'\
                  ,'Year']
    
#coversion of variables into categorical variables
dataset['Film'] =dataset.Film.astype('category')   
dataset['Genre'] =dataset.Genre.astype('category') 
dataset['Year'] =dataset.Year.astype('category') 

#dataset.info()
#dataset.describe()    
'''
#Joint plot
sns.set_style("darkgrid")
j=sns.jointplot(data=dataset, x='CriticRating', y='AudienceRating')
plt.show()

#join plot in hexagon style
sns.set_style("darkgrid")
j=sns.jointplot(data=dataset, x='CriticRating', y='BudgetMillions', kind='hex')
plt.show()


#already studied graph as probability distribution function
sns.set_style("darkgrid")
m1=sns.distplot(dataset.AudienceRating, bins=15)
plt.show()

m2=sns.distplot(dataset.CriticRating, bins=15)
plt.show()

#histogram

#p1=plt.hist(dataset[dataset.Genre=='Action'].BudgetMillions,bins=15)
#p2=plt.hist(dataset[dataset.Genre=='Thriller'].BudgetMillions,bins=15)

#stacked histrogram
#p3=plt.hist(dataset[dataset.Genre=='Comedy'].BudgetMillions,bins=15)


#######################################
#powerful visualizations
list1=list()
mylables=list()
for gen in dataset.Genre.cat.categories:
    list1.append(dataset[dataset.Genre==gen].BudgetMillions)
    mylables.append(gen)
h=plt.hist(list1, bins=30, stacked=True, rwidth=1,label=mylables)
plt.legend()
plt.show()

#kde plot (Kernel density estimation)
vis1=sns.lmplot(data=dataset,x='CriticRating',y='AudienceRating',\
                fit_reg=False, hue='Genre',height=7, aspect=1)
plt.show()
k1=sns.kdeplot(dataset.CriticRating, dataset.AudienceRating,\
               shade=True, shade_lowest=False,cmap='Reds')
k1b=sns.kdeplot(dataset.CriticRating, dataset.AudienceRating,\
               cmap='Reds')
plt.show()

###########################################################################
#working with subplots
f,axes=plt.subplots(1,2,figsize=(12,6),sharex=True, sharey=True)
k1c=sns.kdeplot(dataset.BudgetMillions, dataset.AudienceRating,ax=axes[0])
k1d=sns.kdeplot(dataset.BudgetMillions, dataset.CriticRating,ax=axes[1])
k1c.set(xlim=(-20,160))
############################################################################

#building boxplot and violinplot
v=sns.boxplot(data=dataset[dataset.Genre=='Drama'],x='Year',y='CriticRating')
plt.show()
v1=sns.violinplot(data=dataset[dataset.Genre=='Drama'],x='Year',y='AudienceRating')
plt.show()
###################################

#Create a Facet Grid
g=sns.FacetGrid(dataset,row='Genre',col='Year',hue='Genre')
kws=dict(s=50,linewidth=0.5,edgecolor='black')
g=g.map(plt.scatter,'CriticRating','AudienceRating',**kws )

 
#can populate with any type of chart. Example:histograms
g=sns.FacetGrid(dataset,row='Genre',col='Year',hue='Genre')
g=g.map(plt.hist,'BudgetMillions')

#############################################

#Create a Facet Grid and controlling and adding diagonals
g=sns.FacetGrid(dataset,row='Genre',col='Year',hue='Genre')
kws=dict(s=50,linewidth=0.5,edgecolor='black')
g=g.map(plt.scatter,'CriticRating','AudienceRating',**kws )
g.set(xlim=(0,100),ylim=(0,100))
for ax in g.axes.flat:
    ax.plot((0,100),(0,100), c='gray',ls='--')
g.add_legend()

#######################################################################

#building dashboard (combination of all the types of charts)
sns.set_style("dark",{"axes.facecolor":"black"})
f,axes=plt.subplots(2,2,figsize=(12,6)) #(sharex=True, sharey=True)
#plot[0,0]
k1=sns.kdeplot(dataset.BudgetMillions, dataset.AudienceRating,\
                shade=True, shade_lowest=True, cmap='inferno',\
                ax=axes[0,0])
k1a=sns.kdeplot(dataset.BudgetMillions, dataset.AudienceRating,\
                cmap='cool',ax=axes[0,0])
#plot[0,1]
k2=sns.kdeplot(dataset.BudgetMillions, dataset.CriticRating,\
                shade=True, shade_lowest=True, cmap='inferno',\
                ax=axes[0,1])
k2a=sns.kdeplot(dataset.BudgetMillions, dataset.CriticRating,\
                cmap='cool',ax=axes[0,1])
#k1.set(xlim=(-20,160))
#k2.set(xlim=(-20,160))
#plot[1,0]

#v1=sns.violinplot(data=dataset[dataset.Genre=='Drama'],\
                  #x='Year',y='AudienceRating',\
                  #ax=axes[1,0])
v1=sns.violinplot(data=dataset,\
                  x='Year',y='BudgetMillions',\
                  palette='YlOrRd',ax=axes[1,0])
#plot[1,1]
k3=sns.kdeplot(dataset.CriticRating, dataset.AudienceRating,\
               shade=True, shade_lowest=False,cmap='Blues_r',ax=axes[1,1])

k3a=sns.kdeplot(dataset.CriticRating, dataset.AudienceRating,\
               cmap='gist_gray_r', ax=axes[1,1])
'''
#powerful visualizations
sns.set_style("whitegrid")
list1=list()
mylables=list()
for gen in dataset.Genre.cat.categories:
    list1.append(dataset[dataset.Genre==gen].BudgetMillions)
    mylables.append(gen)
fig,ax=plt.subplots()
fig.set_size_inches(11.7,8.27) #size of A4 paper
h=plt.hist(list1, bins=30, stacked=True, rwidth=1,label=mylables)
plt.title('Movie Budget Distribution', fontsize=35,\
          color='Darkblue', fontname='Times new roman')
plt.ylabel('Number of movies',fontsize=25, color='Red')
plt.xlabel('Budget in Millions',fontsize=25, color='Green')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(frameon=True,fancybox=True,prop={'size':20}, shadow=True, framealpha=1)
plt.show()