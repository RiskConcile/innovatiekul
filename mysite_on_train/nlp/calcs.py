from wordcloud import WordCloud , STOPWORDS
from io import BytesIO
import base64

import matplotlib
#matplotlib.use('TkAgg')
matplotlib.use('Agg')

def generate_image(text_snippet):
    stopwords = set(STOPWORDS)
    impage_png = None
    wordcloud = WordCloud(background_color = 'white',
                stopwords = stopwords,
                max_words=30,
                max_font_size=40).generate(str(text_snippet))
    
    fig , ax = matplotlib.pyplot.subplots(1,1,figsize=(5,3))
    matplotlib.pyplot.imshow(wordcloud);
    ax.axis('off')

    buffer = BytesIO()
    matplotlib.pyplot.savefig(buffer,format='png')
    impage_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(impage_png)
    graphic = graphic.decode('utf-8')
    del impage_png
    return graphic
