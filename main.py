import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import seaborn as sea

color = plt.cm.hsv(np.linspace(0, 1, 20))
# %%
#data
google_Data = pd.read_csv('D:\DATA sCIENCE\job_skills.csv')
google_Data.info()
google_Data.describe()
print("Missing Value", google_Data.isnull().sum().sum())
plt.show()
#
# #company
Companies = google_Data["Company"].value_counts().values.tolist()
sea.catplot(x="Company", data=Companies, kind="count")
sea.show


# # Which jobs are most popular jobs and titles at Google?
Categories= google_Data['Category'].value_counts()
print(Categories)

Categories.plot(kind='bar', title='Most Popular Jobs', figsize=(12,8))
plt.title("Most Popular 20 Job  of Google", fontsize = 20)
plt.xlabel('Names of Job ', fontsize = 10)
plt.ylabel('Count', fontsize = 10)
plt.show()

# # #Location: Most popular locations of google
Location=google_Data['Location']
print(Location)
Location.value_counts().sort_values(ascending = False).head(20).plot.bar()
plt.title("Most Popular 20 Job Locations of Google")
plt.xlabel('Names of Job Locations', fontsize = 10)
plt.ylabel('count', fontsize = 10)
plt.show()
#
# # Responsibilities: Responsibilities for the job
Responsibilities = google_Data['Responsibilities']
print(Responsibilities)
Responsibilities.value_counts().sort_values(ascending = False).head(5).plot.pie()
plt.title("30 Required Responsibilities of Google")
plt.xlabel('Names of Job Locations', fontsize = 10)
plt.ylabel('count', fontsize = 10)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(background_color = 'lightyellow',
                      max_words = 30,
                      width = 2000,
                      height = 2000).generate(str(Responsibilities))

plt.rcParams['figure.figsize'] = (12, 12)
plt.axis('off')
plt.imshow(wordcloud)
plt.title('Most Available Responsibilities', fontsize = 30)
plt.show()

# # Minimum Qualifications: Minimum Qualifications for the job
MinQualifications = google_Data['Minimum Qualifications']
stopwords = set(STOPWORDS)
wordcloud = WordCloud(background_color = 'lightyellow',
                      width = 2000,
                      height = 2000).generate(str(MinQualifications))

plt.rcParams['figure.figsize'] = (12, 12)
plt.axis('off')
plt.imshow(wordcloud)
plt.title('Minimum Qualifications for google jobs', fontsize = 30)
plt.show()

# # Preferred Qualifications: Preferred Qualifications for the job
PrefQualifications = google_Data['Preferred Qualifications']
stopwords = set(STOPWORDS)
wordcloud = WordCloud(background_color = 'lightblue',
                      width = 2000,
                      height = 2000).generate(str(PrefQualifications))

plt.rcParams['figure.figsize'] = (12, 12)
plt.axis('off')
plt.imshow(wordcloud)
plt.title('Preferred Qualifications in Google', fontsize = 30)
plt.show()
