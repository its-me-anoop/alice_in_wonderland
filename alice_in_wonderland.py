import content
import matplotlib.pyplot as plt
import numpy as np


def analyze_content(content_text):
    """
    Function to analyze content for the longest words and their frequencies.
    Plots a bar graph of words against their frequencies.
    """
    highest_scoring_words = {}
    sentences = content_text.split(".")

    for sentence in sentences:
        if sentence:  # Check for non-empty sentences
            # The highest scoring word in the sentence
            highest_scoring_word = max(sentence.split(), key=len)
            # Increment count of the word
            highest_scoring_words[highest_scoring_word] = (
                highest_scoring_words.get(highest_scoring_word, 0) + 1
            )

    print(highest_scoring_words)

    champion = max(highest_scoring_words, key=highest_scoring_words.get)
    print(
        f"The most used word with highest score is : {champion} with a score of {highest_scoring_words[champion]}"
    )

    # Filter out words that appear only once
    frequent_words = {k: v for k, v in highest_scoring_words.items() if v != 1}
    words = list(frequent_words.keys())
    scores = list(frequent_words.values())

    # Plotting Bar chart for better visualization of word frequencies
    plt.figure(figsize=(15, 10))  # Adjust figure size as needed
    plt.bar(words, scores)
    plt.xlabel("Words")
    plt.ylabel("Scores")
    plt.title("Word Scores")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    text_content = content.content()
    analyze_content(content_text=text_content)
