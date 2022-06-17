# Ml-depression-indicator

A machine learning group project to determine whether a person suffers from major depression based on the BDC questionnaire and his or her fatigue level. Fatigue level is calculated according to the frequency of blinking. Before counting the frequency of blinking, Mediapipe Face Mesh will be used to compute the eye aspect ratio (EAR)  to determine the eyes' state. The idea of correlating fatigue level and depression is based on research by Targum & Fava in 2011. After determining whether users suffer from depression and their respective fatigue levels, the users are required to take another questionnaire on their personalities and preferences. Lastly, with the type of depression, fatigue level and personality, we recommend depression alleviating activities based on a recommendation system. 

## Collaborators

- Cheok Xin Yu ([XinYu27](https://github.com/XinYu27))
- Kuck Swee Nien ([KuckSN](https://github.com/KuckSN))
- Law Shiao Yin ([zzzhxlxyyy](https://github.com/zzzhxlxyyy))
- Lim Wei Xin ([Programmer420-1](https://github.com/Programmer420-1))
- Nah Wan Jun ([nwjun](https://github.com/nwjun))

## Installation Guide

1. Install all the required libraries by running the following code.

```terminal
pip install -r requirements.txt
```

1. Enter the code below in the terminal to run the streamlit page.

```terminal
streamlit run *"Depression Test.py"
```

## Reference

Al-gawwam, S., & Benaissa, M. (2018). Robust Eye Blink Detection Based on Eye 
Landmarks and Savitzky–Golay Filtering. Information, 9(4), 93. 
https://doi.org/10.3390/info9040093
 
Arafat Islam, Naimur Rahaman, Md Atiqur Rahman Ahad. A Study on Tiredness 
Assessment by Using Eye Blink Detection. Jurnal Kejuruteraan, 31(2), 209-214. 
https://doi.org/10.17576/jkukm-2019-31(2)-04
 
Asma, U.H., Roy, A., Paul, G. & Raha, M. 2014. Fatigue estimation through face monitoring 
and eye blinking. International Conference on Mechanical Industrial & Energy 
Engineering, 1-5.

Balandong, R. P., Ahmad, R. F., Mohamad Saad, M. N., & Malik, A. S. (2018). A Review on 
EEG-Based Automatic Sleepiness Detection Systems for Driver. IEEE Access, 6, 
22908–22919. https://doi.org/10.1109/access.2018.2811723

Barkved, K. (2022, March 9). How to know if your machine learning model has good 
performance: Obviously AI. Data Science without code.
https://www.obviously.ai/post/machine-learning-model-performance

Burns, D., Westra, H., Trockel, M., & Fisher,A. (2012, April 22). Motivation and changes in
 depression - cognitive therapy and research. SpringerLink.
https://link.springer.com/article/10.1007/s10608-012-9458-3

Chau, M., & Betke, M. (2005). Real Time Eye Tracking and Blink Detection with USB 
Cameras. Boston Univ. Comput. Sci., 2215.

Chioka. (2013). Class imbalance problem.
http://www.chioka.in/class-imbalance-problem/#:~:text=What%20is%20the%20Clas
s%20Imbalance,class%20of%20data%20(negative).

Danisman, T, Bilasco, I., Djeraba, C. & Ihaddadene, N. (2010). Drowsy driver detection 
system using eye blink patterns. International Conference on Machine and Web 
Intelligence, 230-233.

Holtz, C., Sowell, R., VanBrackle, L., Velasquez, G., & Hernandez-Alonso, V. (2014). A 
quantitative study of factors influencing quality of life in rural Mexican 
women diagnosed with HIV. Journal of the Association of Nurses in AIDS Care. 
https://www.sciencedirect.com/science/article/abs/pii/S1055329014000491

Ji, Y., Wang, S., Zhao, Y., Wei, J., & Lu, Y. (2019). Fatigue State Detection Based on 
Multi-Index Fusion and State Recognition Network. IEEE Access, 7, 64136–64147. 
https://doi.org/10.1109/access.2019.2917382

Jia, H., Xiao, Z., & Ji, P. (2021). Fatigue Driving Detection Based on Deep Learning and 
Multi-Index Fusion. IEEE Access, 9, 147054–147062. 
https://doi.org/10.1109/access.2021.3123388

Lew, B., Kõlves, K., Lester, D., Chen, W. S., Ibrahim, N. B., Khamal, N. R. B., Mustapha, F., 
Chan, C. M. H., Ibrahim, N., Siau, C. S., & Chan, L. F. (2022). Looking Into Recent 
Suicide Rates and Trends in Malaysia: A Comparative Analysis. Frontiers in Psychiatry, 12. https://doi.org/10.3389/fpsyt.2021.770252

Soukupova, T. & Cech, J. 2016. Real-time eye blink detection using facial landmarks. 21st 
Computer Vision Winter Workshop, 3-