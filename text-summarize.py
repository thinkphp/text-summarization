from summa import summarizer

def generate_summary(text):

    summary = summarizer.summarize(text)
    
    return summary

# Example text
input_text = """
The play, set in Verona, Italy, begins with a street brawl between Montague and Capulet servants who, like the masters they serve, are sworn enemies. Prince Escalus of Verona intervenes and declares that further breach of the peace will be punishable by death. Later, Count Paris talks to Capulet about marrying his daughter Juliet, but Capulet asks Paris to wait another two years and invites him to attend a planned Capulet ball. Lady Capulet and Juliet's Nurse try to persuade Juliet to accept Paris's courtship.
Meanwhile, Benvolio talks with his cousin Romeo, Montague's son, about Romeo's recent depression. Benvolio discovers that it stems from unrequited infatuation for a girl named Rosaline, one of Capulet's nieces. Persuaded by Benvolio and Mercutio, Romeo attends the ball at the Capulet house in hopes of meeting Rosaline. However, Romeo instead meets and falls in love with Juliet. Juliet's cousin, Tybalt, is enraged at Romeo for sneaking into the ball but is stopped from killing Romeo by Juliet's father, who does not wish to shed blood in his house. After the ball, in what is now famously known as the "balcony scene", Romeo sneaks into the Capulet orchard and overhears Juliet at her window vowing her love to him in spite of her family's hatred of the Montagues. Romeo makes himself known to her, and they agree to be married. With the help of Friar Laurence, who hopes to reconcile the two families through their children's union, they are secretly married the next day.
"""

# Generate and print the summary
summary = generate_summary(input_text)
print(summary)
