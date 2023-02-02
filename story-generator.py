import markovify

# Get the raw text for the model
with open("story_file.txt") as f:
    text = f.read()

# Build the Markov model
text_model = markovify.Text(text)

# Generate a story with at least 1000 words
story = ""
while len(story.split()) < 1000:
    story = story + " " + text_model.make_sentence()

# Print the story
print(story)
