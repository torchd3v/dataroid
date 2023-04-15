#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bot:    
    def __init__(self,data,sampling=False,**kwargs):
        '''
        Fit's a model by automaticaly identifying discrete and continuous columns.
        
        # Parameters:
        #     data (DataFrame):The data which will be used for training.
        #     sampling (Boolean):Sampling 1000 data points randomly.
        #     **kwargs: Model training parameters. 
        '''
        import pandas as pd
        import ctgan

        self.data = data if sampling==False else data.sample(1000, random_state = 42) 
        
        discrete_columns = []
        for x in data.columns:
            if data[x].dtypes == "O" or data[x].dtypes == "datetime64[ns]" or data[x].dtypes == "category":
                discrete_columns.append(x)
        
        model = ctgan.CTGAN(**kwargs)
        model.fit(data,discrete_columns)
        self.model = model
    
    def generate(self,n):
        '''Takes number of samples to generate and returns DataFrame
        
        # Returns:
        #     df (DataFrame):Synthetically  generated dataframe.  
        '''
        return self.model.sample(n)

