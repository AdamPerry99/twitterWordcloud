from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt #Displays wordcloud
from PIL import Image #Loads the image
import numpy as np #For colours

#Load .txt file and sets up Stopwords to count the numebr words and remove common words like 'we' and 'I'
text = open('.txt', 'r', encoding="latin-1").read()
stopwords = set(STOPWORDS)

#Accesses a background image for the wordcloud
custom_mask = np.array(Image.open('hashtag.png'))

#Designs wordcloud, styles and generates
wc = WordCloud(background_color = '#DEF3F9', max_font_size = 100, max_words = 50, stopwords = stopwords, mask = custom_mask, contour_width = 3,
contour_color = '#1DA1F2')
wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)

#Formatting of the wordcloud
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

#Send wordcloud to a new file
wc.to_file('.png')
