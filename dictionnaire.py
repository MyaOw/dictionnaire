import csv
try:
    with open('textinput.txt', 
            'r', encoding='utf-8') as f:
        data = f.read()
except:
    print("Zut, il y a un problème avec le fichier !")
else:
    def punctuation(data):
        """ 
        Remplace la ponctuation par des espaces
        """
        PUNCT_LIST = [".", ";", ":", "!", "?", "/", "\\", ",", "#", 
                    "@", "$", "&", ")", "(", "'", "\"", "’", "…", 
                    "–", "—", "-", "\n", "\t", "0", "1", "2", "3",
                    "4", "5", "6", "7", "8", "9"]
        withoutpunct = ''
        for i in data:
            if i not in PUNCT_LIST:
                withoutpunct += i
            else:
                withoutpunct += ' '
        return withoutpunct.lower()
    withoutpunct = punctuation(data)

    def words(data):
        """
        Retourne les mots en éléments d'une liste, enlève les None
        """
        word = data.split()
        word = list(filter(None, word)) # enlève les None de la liste
        return word
    words = words(withoutpunct)

    def countwords(words):
        countw = len(words) # compte le nombre d'éléments de la liste
        return countw
    countw = countwords(words)
    print(countw)

    def countoccurences(data):
        """ 
        crée un dictionnaire avec comme valeurs (mot, compte) pour 
        mot dans les mots sans doublon.
        A set is an unordered collection with no duplicate elements.
        """
        occur = dict((x, data.count(x)) for x in set(data)) 
        return occur
    occur = countoccurences(words)

    def mostfrequent(occur):
        """
        on print sinon ça sort de la boucle avec return.
        on reverse pour l'avoir du plus grand au plus petit
        A lambda function is a small anonymous function. 
        A lambda function can take any number of arguments, 
        but can only have one expression.
        """
        reduceddict = {}
        BANNED_LIST = ['moi', 'toi', 'soi', 'mon', 'ma', 'mes', 'leur', 
                        'comme', 'cette', 'tout', 'plus', 'si', 'au', 
                        'sa', 'son', 'ses', 'qu', 'se', 'qui', 'est', 
                        'ce', 'lui', 'du', 'le', 'la', 'les', 'de', 
                        'et', 'que', 'en', 'je', 'tu', 'il', 'elle',
                        'nous', 'vous', 'ils', 'elles', 'pas', 'ne',
                        'un', 'une', 'des', 'dans', 'sur', "par", 
                        "pour", "avec", "mais", "sans", "était", 
                        "avait", "dit", "bien", "être"]
        for k, v in occur.items():
            if len(k) == 1:
                continue
            elif k in BANNED_LIST:
                continue
            else:
                reduceddict.update({k: v})
        print(sorted(reduceddict.items(),
                     key=lambda x: x[1], reverse=True)[:10]) 

    mostfrequent(occur)

    with open('words.csv', 'w', newline='') as csvfile:
        fieldnames = ['word', 'occurences']
        writer = csv.DictWriter(csvfile, delimiter =";", 
                fieldnames=fieldnames)
        writer.writeheader()

        def writeincsv(occur):
            for k, v in occur.items():
                writer.writerow({'word': k, 'occurences': v})
        writeincsv(occur)
