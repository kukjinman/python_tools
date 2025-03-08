from wordcloud import WordCloud
import matplotlib.pyplot as plt

# List of words
words = [
    "Python", "Java", "C++", "JavaScript", "Ruby", "Ruby", "Ruby", "Go", "Rust", "PHP",
    "HTML", "CSS", "SQL", "R", "Python", "Python", "Ruby", "Ruby", "TypeScript", "Dart"
]

# Join the list into a single string with spaces
text = ' '.join(words)

# Create a WordCloud instance
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()