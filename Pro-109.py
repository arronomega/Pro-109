import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv
df = pd.read_csv("StudentsPerformance.csv")
mean = sum(df["math score"].tolist())/len(df["math score"].tolist())
st_d = st.stdev(df["math score"].tolist())
median = st.median(df["math score"].tolist())
mode = st.mode(df["math score"].tolist())
h =df["math score"].tolist()
meanH = st.mean(h)
modeh = st.mode(h)
medianh = st.median(h)
h_d = st.stdev(h)
h_f_s_d_s , h_f_s_d_e =meanH-h_d,meanH+h_d
h_s_s_d_s , h_s_s_d_e =meanH-(2*h_d),meanH+(2*h_d)
h_t_s_d_s , h_t_s_d_e =meanH-(3*h_d),meanH+(3*h_d)
hlodstd =[res for res in h if res > h_f_s_d_s and res < h_f_s_d_e ]
hlodstd1 =[res for res in h if res > h_s_s_d_s and res < h_s_s_d_e ]
hlodstd2 =[res for res in h if res > h_t_s_d_s and res < h_t_s_d_e ]
print("{}% of data for height lies within 1 standard deviation".format(len(hlodstd)*100.0/len(h)))
print("{}% of data for height lies within 2 standard deviations".format(len(hlodstd1)*100.0/len(h)))
print("{}% of data for height lies within 3 standard deviations".format(len(hlodstd2)*100.0/len(h)))