from wordcloud import STOPWORDS,WordCloud
import matplotlib as plt
import seaborn as sns


class TweetDfVisualization:
    
    def __init__(self, processedDf):
        self.df = processedDf
        
    
    def create_wordcloud(self):
        # Displays a figure of the most used words
        plt.figure(figsize=(20, 10))
        plt.imshow(WordCloud(width=1000,height=600,stopwords=STOPWORDS).generate(' '.join(self.df.cleaned_tweet.values)))
        plt.axis('off')
        plt.title('Most Frequent Words In Tweets',fontsize=16)
        plt.savefig('wordcloud.png')
        plt.show()

    def create_viz(self):
        red='#FF5C5C'
        dark_green = '#00A300'
        yellow = '#FFC55C'
        blue = '#7EC8E3'
        green = '#00D100'

        category_color_dict = {'very negative':red, 'negative':yellow, 'neutral':blue, 'positive':green, 'very positive':dark_green}
        fig, axes = plt.subplots(2,2, figsize=(20, 20))
        temp_select_df = self.df['classified_polarity'].value_counts(sort=False)
        explode = (0.4, 0.4, 0.4, 0.4, 0.4)
        colors= [category_color_dict[i] for i in temp_select_df.index]

        temp_select_df.plot.pie(ax=axes[0,0] ,ylabel='', autopct='%1.1f%%',
                 shadow=True, startangle=90, explode = explode, colors=colors)

        sns.countplot(ax=axes[1,0], data=self.df, x='classified_polarity', hue='classified_subjectivity', palette="ch:1")
        sns.set_context('paper')
        sns.set_style('dark')
        axes[1,0].set(xlabel='Polarity', ylabel='Count', title='POLARITY WITH SUBJECTIVITY')
        axes[1,0].legend(title='Subjectivity', loc='upper right')
        plt.subplots_adjust(top = 0.99, bottom=0.1, hspace=0.2, wspace=0.4)

        colors= [category_color_dict[i] for i in temp_select_df.index]
        temp_select_df = self.df['classified_polarity'].value_counts(sort=False)
        temp_select_df.plot.bar(ax=axes[0,1] ,xlabel='Polarity', ylabel='Count', color=colors, title='POLARITY COUNT')

        sns.countplot(ax=axes[1,1], data=self.df, x='classified_subjectivity', palette="ch:1")
        axes[1,1].set(xlabel='Count', ylabel='Polarity', title='SUBJECTIVITY COUNT')
        #plt.show()

        plt.savefig('viz.png')