from heapq import nlargest
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

#text = """Mission denial has been referred to the House Government Operations Committee, where legislation traditionally goes to die. Democrats have a 56-54 majority in the House. House Speaker Joe Tate (D-Detroit) has said that Democrats will maintain control of the chamber under House rules even after two Democratic House members are expected to resign their seats next week after winning their mayoral elections, bringing the chamber to a 54-54 tie until special elections are held.

#Members of the Michigan House can vote to impeach civil officers for corrupt conduct in office, or for crimes and misdemeanors with a majority vote, but two-thirds of the state Senate must then vote in favor to convict and remove that officer. The Senate is led by Democrats, who have a 20-18 majority.

#In the articles, the Republicans argued Nessel violated her oath of office for failing to charge individuals tied to a large number of irregular voter registration forms submitted in Muskegon. 

#A statement from the Michigan State Police, which investigated the irregularities alongside the Attorney General’s Office, Michigan Department of State and the Muskegon Police Department said “none of the irregular voter registrations in Muskegon resulted in voters receiving absentee ballots, any resulting registrations have been voided, and there is no expected impact on any election.”

#The investigation was turned over to the FBI in 2021, according to a report from Bridge Michigan. It remains unclear whether the investigation is ongoing or has concluded without charges, with Nessel spokesman Danny Wimmer telling Bridge the decision to prosecute fraud lies with the FBI. 

#The articles also allege that the charges filed against 16 Republicans tied to an effort to submit false electoral votes for former President Donald Trump in the 2020 election, were brought as a political attack.  """

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    # prints stop words

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    #print(doc)
    tokens = [token.text for token in doc]
    #print(tokens)
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1


                #print(word_freq)

    max_freq = max(word_freq.values())
    #print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

        #print(word_freq)

    sent_tokens = [sent for sent in doc.sents]    

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]


    select_len = int(len(sent_tokens) * 0.3)
    #print(select_len)
    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    #print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    #print(text)
    #print(summary)
    #print("Length of original text", len(text.split(' ')))
    #print("Length of summarized text", len(summary.split(' ')))

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))








             
