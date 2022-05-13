import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

    list = input("Re-enter list.")
  else:
    pass
  list_array = np.array(list).reshape(3,3)
  calculations = {"mean":[],"variance":[],"standard deviation":[],"max":[],"min":[],"sum":[]}
  #mean calculations
  row_means = np.average(list_array,axis=1).tolist()
  column_means = np.average(list_array, axis=0).tolist()
  all_mean = np.average(list_array).tolist()
  mean_list = [column_means,row_means,all_mean]
  calculations["mean"].extend(mean_list)
  #variance calculations
  columns_var = np.var(list_array,axis=0).tolist()
  row_var = np.var(list_array, axis=1).tolist()
  all_var = np.var(list_array).tolist()
  var_list = [columns_var,row_var,all_var]
  calculations["variance"].extend(var_list)
  #standard deviation calculations
  column_std = np.std(list_array,axis=0).tolist()
  row_std = np.std(list_array,axis=1).tolist()
  all_std = np.std(list_array).tolist()
  std_list = [column_std,row_std,all_std]
  calculations["standard deviation"].extend(std_list)
  #max calculations
  column_max = np.amax(list_array,axis=0).tolist()
  row_max = np.amax(list_array,axis=1).tolist()
  all_max =np.amax(list_array).tolist()
  max_list = [column_max,row_max,all_max]
  calculations["max"].extend(max_list)
  #min calculations
  column_min = np.amin(list_array,axis=0).tolist()
  row_min = np.amin(list_array,axis=1).tolist()
  all_min =np.amin(list_array).tolist()
  min_list = [column_min,row_min,all_min]
  calculations["min"].extend(min_list)
  #sum calculations
  column_sum = np.sum(list_array,axis=0).tolist()
  row_sum = np.sum(list_array,axis=1).tolist()
  all_sum =np.sum(list_array).tolist()
  sum_list = [column_sum,row_sum,all_sum]
  calculations["sum"].extend(sum_list)
  
  
  
  
  
    
  
  
  



  return calculations