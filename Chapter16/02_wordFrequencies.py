"""
    16.2 Word Frequencies
"""

from collections import defaultdict

paragraph = "Lorem ipsum dolor sit amet, diam decore erroribus his ei, viderer habemus dolores pro ea. In sea purto eirmod. Vis ex purto aeterno debitis. At dolore nonumes reprehendunt vim, iudico exerci volumus sit ex. Eum alterum antiopam at, ei usu impetus delicatissimi. Et pro doctus voluptua, quo iusto virtute accommodare in.\
            Pro imperdiet necessitatibus an, mei saperet euripidis delicatissimi ex. Vim te tantas mandamus, omittam offendit interesset vis ad. Quando pertinax at per, bonorum postulant sed no, eos eu atqui contentiones. Vel ex utroque menandri, vis ad oratio interpretaris. Eu porro dicant mandamus vix.\
            Mea ut accumsan evertitur posidonium, cum everti adipiscing at. Ea nam natum choro graecis. Te est habeo noster nostro, nonumes verterem sea id. Veri putent voluptatibus vim ei, hendrerit conceptam elaboraret an eos.\
            Eos novum dolores assueverit ne, usu quem feugait appellantur eu, id cum quod solum efficiantur. Mea ad atqui liber laboramus. Ornatus admodum te vis. Quo ut movet elitr fierent, id per alia ubique repudiare. Laudem putant corpora mei ad. Per everti albucius explicari ad, cum in modus eirmod.\
            Ex lobortis inciderint nec. Ei duo eius error. Id decore iracundia pri, et alii solum eam. Summo vidisse his te, id voluptua theophrastus mei. Ei odio quaeque duo. Laoreet delicata vim ex, nam eu aliquam inermis molestie, his omnes eirmod suavitate an."

def process(word):
    return word.lower().replace(",", "").replace(".", "")

def occurrences(paragraph, word):
    freqDict = defaultdict(int)
    for word in paragraph.split(" "):
        word = process(word)
        freqDict[word] += 1
    if word in freqDict:
        return freqDict[word]
    else:
        return 0

if __name__ == "__main__":
    print(occurrences(paragraph, "quem"))