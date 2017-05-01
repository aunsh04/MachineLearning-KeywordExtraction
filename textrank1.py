from summa import keywords
from summa.export import gexf_export
sample_file = open("/Users/Aunsh/NLP_Proj/data/53/53.txt", 'r')
text = sample_file.read()
text = unicode(text, errors='ignore')

print keywords.keywords(text, words=10)
