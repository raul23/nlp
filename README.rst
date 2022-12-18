===
NLP
===
.. contents:: **Contents**
   :depth: 4
   :local:
   :backlinks: top

Scripts
=======
``extract_names_from_text.py``: Extract names from text
-------------------------------------------------------
This script tests different NLP methods to extract names from text:

- The `first method <#method-1-nltk-part-of-speech-tag-nnp>`_ makes use of ``nltk`` to get all NNP (proper noun, 
  singular) with more than one part from a given text and then the first and last names are returned
- The `second method <#method-2-spacy>`_ feeds the raw text to the NLP model `en_core_web_md 
  <https://spacy.io/models/en#en_core_web_md>`_ and then ``spacy`` produces a document containing among other 
  things named entities with the **PERSON** label. 

`:star:` 

   - The Python script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_
   - The script ``extract_names_from_text.py`` only imports the libraries/modules necessary for the choosen method, 
     e.g. if you choose the `second method <#method-2-spacy>`_, only the ``spacy`` library is imported. Hence, if you 
     are just interested in one particular method, you won't need to download unnecessary libraries.

Texts used for testing
''''''''''''''''''''''
The script ``extract_names_from_text.py`` is tested on the following four texts (taken from Wikpedia and stackoverflow):

.. code-block:: python
   
   # Examples
   # Ref.: https://en.wikipedia.org/wiki/Wolfgang_Pauli
   text1 = """
   Wolfgang Ernst Pauli (/ˈpɔːli/; German: [ˈvɔlfɡaŋ ˈpaʊli]; 25 April 1900 – 
   15 December 1958) was an Austrian theoretical physicist and one of the pioneers 
   of quantum physics. In 1945, after having been nominated by Albert Einstein, 
   Pauli received the Nobel Prize in Physics for his "decisive contribution 
   through his discovery of a new law of Nature, the exclusion principle or Pauli 
   principle". The discovery involved spin theory, which is the basis of a theory 
   of the structure of matter.
   """

   # Ref.: https://en.wikipedia.org/wiki/Philip_W._Anderson
   text2 = """
   Anderson was born in Indianapolis, Indiana, and grew up in Urbana, Illinois. 
   His father, Harry Warren Anderson, was a professor of plant pathology at the 
   University of Illinois at Urbana; his maternal grandfather was a mathematician 
   at Wabash College, where Anderson's father studied; and his maternal uncle was 
   a Rhodes Scholar who became a professor of qEnglish, also at Wabash College. He 
   graduated from University Laboratory High School in Urbana in 1940. Under the 
   encouragement of a math teacher by the name of Miles Hartley, Anderson enrolled 
   at Harvard University to study under a fully-funded scholarship. He 
   concentrated in "Electronic Physics" and completed his B.S. in 1943, after which 
   he was drafted into the war effort and built antennas at the Naval Research 
   Laboratory until the end of the Second World War in 1945. As an undergraduate, 
   his close associates included particle-nuclear physicist H. Pierre Noyes, 
   philosopher and historian of science Thomas Kuhn and molecular physicist Henry 
   Silsbee. After the war, Anderson returned to Harvard to pursue graduate studies 
   in physics under the mentorship of John Hasbrouck van Vleck; he received his 
   Ph.D. in 1949 after completing a doctoral dissertation titled "The theory of 
   pressure broadening of spectral lines in the microwave and infrared regions."
   """

   # Ref.: https://en.wikipedia.org/wiki/Galileo_Galilei
   text3 = """
   Galileo continued to receive visitors until 1642, when, after suffering fever 
   and heart palpitations, he died on 8 January 1642, aged 77. The Grand Duke of 
   Tuscany, Ferdinando II, wished to bury him in the main body of the Basilica of 
   Santa Croce, next to the tombs of his father and other ancestors, and to erect 
   a marble mausoleum in his honour.
   These plans were dropped, however, after Pope Urban VIII and his nephew, 
   Cardinal Francesco Barberini, protested, because Galileo had been condemned by 
   the Catholic Church for "vehement suspicion of heresy". He was instead buried 
   in a small room next to the novices' chapel at the end of a corridor from the 
   southern transept of the basilica to the sacristy. He was reburied in the main 
   body of the basilica in 1737 after a monument had been erected there in his 
   honour; during this move, three fingers and a tooth were removed from his 
   remains. These fingers are currently on exhibition at the Museo Galileo in 
   Florence, Italy.
   """
   
   # Ref.: https://stackoverflow.com/q/20290870
   text4 = """
   Some economists have responded positively to Bitcoin, including 
   Francois R. Velde, senior economist of the Federal Reserve in Chicago 
   who described it as "an elegant solution to the problem of creating a 
   digital currency." In November 2013 Richard Branson announced that 
   Virgin Galactic would accept Bitcoin as payment, saying that he had invested 
   in Bitcoin and found it "fascinating how a whole new global currency 
   has been created", encouraging others to also invest in Bitcoin.
   Other economists commenting on Bitcoin have been critical. 
   Economist Paul Krugman has suggested that the structure of the currency 
   incentivizes hoarding and that its value derives from the expectation that 
   others will accept it as payment. Economist Larry Summers has expressed 
   a "wait and see" attitude when it comes to Bitcoin. Nick Colas, a market 
   strategist for ConvergEx Group, has remarked on the effect of increasing 
   use of Bitcoin and its restricted supply, noting, "When incremental 
   adoption meets relatively fixed supply, it should be no surprise that 
   prices go up. And that’s exactly what is happening to BTC prices."
   """

Dependencies for **extract_names_from_text.py**
'''''''''''''''''''''''''''''''''''''''''''''''
This is the environment on which the script ``extract_names_from_text.py`` was tested:

* **Platforms:** macOS
* **Python**: versions **3.7** and **3.8**
* For `method 1 <#method-1-nltk-part-of-speech-tag-nnp>`_:
  
  * `nltk (Natural Language Toolkit) <https://nltk.org/>`_: **v3.7**
  * `numpy <https://numpy.org/>`_: **v1.21.5** (Python 3.7) and **v1.23.4** (Python 3.8), necessary internally for ``nltk``
  * `nameparser <https://pypi.org/project/nameparser/>`_: **v1.1.2**, for parsing human names into their individual components
* For `method 2 <#method-2-spacy>`_:

  * `spacy <https://spacy.io/>`_: **v2.3.5** (Python 3.7) and **v3.3.1** (Python 3.8)

Usage for **extract_names_from_text.py**
''''''''''''''''''''''''''''''''''''''''
Run the script **extract_names_from_text.py**
`````````````````````````````````````````````
Run the script by specifying the method to use for extracting names from text::

   $ pyton extract_names_from_text.py -m 1

`:information_source:` By default, the `first method <#method-1-nltk-part-of-speech-tag-nnp>`_ is used

List of options for **extract_names_from_text.py**
``````````````````````````````````````````````````
To display the script's list of options and their descriptions, use the ``-h`` option::

   $ python extract_names_from_text.py -h
   
   usage: python extract_names_from_text.py [OPTIONS]

   Get names from texts

   optional arguments:
     -h, --help            show this help message and exit
     -m METHOD, --method METHOD
                           Method to use for extracting the names from texts.
                           (default: 1)
     -d, --download        Whether to download necessary resources for the selected method
                           (default: False)

`:information_source:` These are the resources that needs to be downloaded for each method (with the ``-d`` flag):

  - **Method 1:** 'punkt', 'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words'
  - **Method 2:** 'en_core_web_md'
  
`:star:` Ways to download and install the model 'en_core_web_md' necessary for `method 2 <#method-2-spacy>`_

  1. running the script with the ``-d`` flag, e.g. ``python extract_names_from_text.py -d`` 
  2. running the command 'python -m spacy download en_core_web_md' on the terminal

Method 1: ``nltk`` + part of speech tag **NNP**
'''''''''''''''''''''''''''''''''''''''''''''''
From the  `stackoverflow user 'e h' <https://stackoverflow.com/q/20290870>`_:

 This is what I tried (code is below): I am using nltk to find everything marked as a 
 person and then generating a list of all the NNP parts of that person. I am skipping 
 persons where there is only one NNP which avoids grabbing a lone surname.

.. code-block:: python

   import nltk
   from nameparser.parser import HumanName
   
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   nltk.download('maxent_ne_chunker')
   nltk.download('words')

   def get_human_names(text):
       tokens = nltk.tokenize.word_tokenize(text)
       pos = nltk.pos_tag(tokens)
       sentt = nltk.ne_chunk(pos, binary = False)
       person_list = []
       person = []
       name = ""
       for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
           for leaf in subtree.leaves():
               person.append(leaf[0])
           if len(person) > 1: #avoid grabbing lone surnames
               for part in person:
                   name += part + ' '
               if name[:-1] not in person_list:
                   person_list.append(name[:-1])
               name = ''
           person = []
       return person_list
   
   text = 'In 1945, after having been nominated by Albert Einstein, Pauli received the Nobel Prize in ' \
          'Physics for his "decisive contribution through his discovery of a new law of Nature, the ' \
          'exclusion principle or Pauli principle".'
   names = get_human_names(text)
   for name in names: 
       print(HumanName(name).first + ' ' + HumanName(name).last)

`:information_source:`

  - The `stackoverflow user 'Gihan Gamage' 
    <https://stackoverflow.com/questions/20290870/improving-the-extraction-of-human-names-with-nltk#comment108366804_20290870>`_ 
    suggests downloading the following nltk packages after the import statements: punkt, averaged_perceptron_tagger, 
    maxent_ne_chunker, words
  - The Python code returns the first and last name (e.g. Albert Einstein) for each person found in the text

`:star:` The script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_. 

To run the script on the `four texts <./scripts/extract_names_from_text.py#L2>`_::

 $ python extract_names_from_text.py -m 1
 
Ouput::

   #########
   # Text1 #
   #########
   Ernst Pauli
   Albert Einstein

   #########
   # Text2 #
   #########
   Harry Anderson
   Miles Hartley
   Pierre Noyes
   Thomas Kuhn
   Henry Silsbee
   John Hasbrouck

   #########
   # Text3 #
   #########
   Ferdinando II
   Santa Croce
   Urban 
   Francesco Barberini

   #########
   # Text4 #
   #########
   Francois Velde
   Richard Branson
   Virgin Galactic
   Paul Krugman
   Larry Summers
   Nick Colas

Method 2: ``spacy``
'''''''''''''''''''
Feeding the raw text to the NLP model `en_core_web_md <https://spacy.io/models/en#en_core_web_md>`_, ``spacy`` then produces a document containing among other things named entities. The entities that are of interest to us are those labeled as **PERSON**.

.. code-block:: python

   import shlex
   import subprocess
   import spacy
   
   # Download the model 'en_core_web_md'
   cmd = 'python -m spacy download en_core_web_md'
   subprocess.run(shlex.split(cmd), capture_output=True)
   model = spacy.load('en_core_web_md')
   
   doc = model(text)
   names = []
   for ent in doc.ents:
       if ent.label_ == 'PERSON' and str(ent) not in names and len(ent) > 1:
           name = str(ent).replace('\n', '')
           print(name)
           names.append(name)

`:star:` The script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_. 

`:star:` Ways to download and install the model 'en_core_web_md' which is necessary for method 2

  1. running the script with the ``-d`` flag, e.g. ``python extract_names_from_text.py -d`` 
  2. running the command 'python -m spacy download en_core_web_md' on the terminal

`:information_source:` about the ``if`` condition

  - ``str(ent) not in names``: to avoid displaying duplicated names
  - ``len(ent) > 1``: to avoid displaying names with only one part (e.g. Anderson)

To run the script on the `four texts <./scripts/extract_names_from_text.py#L2>`_::

 $ python extract_names_from_text.py -m 2 -d
 
Ouput::

   #########
   # Text1 #
   #########
   Wolfgang Ernst Pauli
   Albert Einstein

   #########
   # Text2 #
   #########
   Harry Warren Anderson
   Miles Hartley
   H. Pierre Noyes
   Thomas Kuhn
   Henry Silsbee
   John Hasbrouck van Vleck

   #########
   # Text3 #
   #########
   Pope Urban VIII
   Francesco Barberini

   #########
   # Text4 #
   #########
   Francois R. Velde
   Richard Branson
   Paul Krugman
   Larry Summers
   Nick Colas

``detect_lang.py``: Detect text language
----------------------------------------
This script tests different NLP methods to detect text language:

- The `first method <#method-1-detect-only-if-it-is-english-or-not-nltk-based-on-words>`_ ... TODO
- The second method ... TODO

`:star:` 

   - The Python script can be found at `detect_lang.py <./scripts/detect_lang.py>`_
   - The script ``detect_lang.py`` only imports the libraries/modules necessary for the choosen method, 
     e.g. if you choose the `first method <#method-1-detect-only-if-it-is-english-or-not-nltk-based-on-words>`_, 
     only the ``nltk`` library is imported.
     
Texts used for testing
''''''''''''''''''''''
The script ``detect_lang.py`` is tested on the following eight texts (all taken from Wikpedia):

.. code-block:: python

   # Examples from Wikipedia
   # Ref.: https://en.wikipedia.org/wiki/Freeman_Dyson [ENGLISH]
   text1 = """
   Freeman John Dyson FRS (15 December 1923 – 28 February 2020) was an English-American 
   theoretical physicist and mathematician known for his works in quantum field theory, 
   astrophysics, random matrices, mathematical formulation of quantum mechanics, condensed 
   matter physics, nuclear physics, and engineering.[a][8] He was Professor Emeritus in the 
   Institute for Advanced Study in Princeton and a member of the Board of Sponsors of the 
   Bulletin of the Atomic Scientists.
   """

   # Ref.: https://fr.wikipedia.org/wiki/Freeman_Dyson [FRENCH]
   text2 = """
   Il contribue notamment aux fondements de l'électrodynamique quantique en 1948. Il fait 
   également de nombreuses contributions à la physique des solides, l’astronomie et l’ingénierie 
   nucléaire. On lui doit plusieurs concepts qui portent son nom, tels que la transformée de 
   Dyson (en) , l'arbre de Dyson (en) , la série de Dyson (en) et la sphère de Dyson.
   """

   # Ref.: https://es.wikipedia.org/wiki/Enrico_Fermi [SPANISH]
   text3 = """
   Fermi mandó su tesis «Un teorema sobre probabilidad y algunas de sus aplicaciones» (en 
   italiano, Un teorema di calcolo delle probabilità ed alcune sue applicazioni) a la Scuola Normale 
   Superiore en julio de 1922, y recibió su licenciatura laureada a la temprana edad de 20 años. 
   La tesis era sobre imágenes de difracción de rayos X. La Física Teórica no era considerada una 
   disciplina en Italia y la única tesis que habría sido aceptada sería una sobre física 
   experimental. Por esta razón los físicos italianos fueron lentos al incorporar nuevas ideas 
   como la relatividad que venía de Alemania. Como Fermi se sentía como en casa en el laboratorio 
   haciendo trabajo experimental, esto no supuso mayor problema para él.
   """

   # Ref.: https://en.wikipedia.org/wiki/Enrico_Fermi [ENGLISH]
   text4 = """
   Fermi was fond of pointing out that when Alessandro Volta was working in his laboratory, 
   Volta had no idea where the study of electricity would lead.[145] Fermi is generally 
   remembered for his work on nuclear power and nuclear weapons, especially the creation of 
   the first nuclear reactor, and the development of the first atomic and hydrogen bombs. His 
   scientific work has stood the test of time. This includes his theory of beta decay, his work 
   with non-linear systems, his discovery of the effects of slow neutrons, his study of pion-nucleon 
   collisions, and his Fermi–Dirac statistics. His speculation that a pion was not a fundamental 
   particle pointed the way towards the study of quarks and leptons.
   """

   # Ref.: https://en.wikipedia.org/wiki/Theodor_Kaluza [ENGLISH]
   text5 = """
   Kaluza's insight is remembered as the Kaluza–Klein theory (also named after physicist Oskar 
   Klein). However, the work was neglected for many years, as attention was directed towards 
   quantum mechanics. His idea that fundamental forces can be explained by additional dimensions 
   did not re-emerge until string theory was developed. It is, however, also notable that many of 
   the aspects of this body of work were already published in 1914 by Gunnar Nordström, but his 
   work also went unnoticed and was not recognized when the ideas re-emerged.
   """

   # Ref.: https://de.wikipedia.org/wiki/Theodor_Kaluza_(Physiker) [German]
   text6 = """
   Kaluza entstammte einer deutschen katholischen Familie aus der Stadt Ratibor in Oberschlesien 
   (jetzt Racibórz in Polen). Er selbst wurde in Wilhelmsthal, einem Dorf, das 1899 der Stadt Oppeln 
   (heute Opole) eingemeindet wurde, geboren. Seine Jugend verlebte er in Königsberg (Preußen), wo 
   sein Vater Max Kaluza Professor für Anglistik war.
   """

   # Ref.: https://it.wikipedia.org/wiki/Makoto_Kobayashi_(fisico) [ITALIAN]
   text7 = """
   Makoto Kobayashi (小林誠 Kobayashi Makoto; Nagoya, 7 aprile 1944) è un fisico giapponese, 
   molto conosciuto per il suo lavoro sulla violazione CP.
   """

   # Ref: https://fr.wikipedia.org/wiki/Makoto_Kobayashi_(physicien) [FRENCH]
   text8 = """
   Il est co-lauréat avec Toshihide Maskawa du prix Nobel de physique de 2008 (l'autre moitié a 
   été remise à Yoichiro Nambu) « pour la découverte de l'origine de la brisure de symétrie qui 
   prédit l'existence d'au moins trois familles de quarks dans la nature ».
   """

Dependencies for **detect_lang.py**
'''''''''''''''''''''''''''''''''''''''''''''''
This is the environment on which the script ``detect_lang.py`` was tested:

* **Platforms:** macOS
* **Python**: versions **3.7** and **3.8**
* For `method 1 <#method-1-detect-only-if-it-is-english-or-not-nltk-based-on-words>`_:
  
  * `nltk (Natural Language Toolkit) <https://nltk.org/>`_: **v3.7**
  * `numpy <https://numpy.org/>`_: **v1.21.5** (Python 3.7) and **v1.23.4** (Python 3.8), necessary internally for ``nltk``

Usage for **detect_lang.py**
''''''''''''''''''''''''''''''''''''''''
Run the script **detect_lang.py**
`````````````````````````````````````````````
Run the script by specifying the method to use for detecting the text language::

   $ pyton extract_names_from_text.py -m 1

`:information_source:` By default, the `first method <#method-1-detect-only-if-it-is-english-or-not-nltk-based-on-words>`_ is used

List of options for **detect_lang.py**
``````````````````````````````````````````````````
To display the script's list of options and their descriptions, use the ``-h`` option::

   $ python detect_lang.py -h
   
   usage: python detect_lang.py [OPTIONS]

   Detect text language

   optional arguments:
     -h, --help            show this help message and exit
     -m METHOD, --method METHOD
                           Method to use to detect text language. Choices are: [1, 2] (default: 1)
     -t THRESHOLD, --threshold THRESHOLD
                           If this threshold (% of words or letters in the text that are unusual) 
                           is exceeded, then the language of the text is not English. (default: 25)

`:information_source:` The ``-t/--threshold`` option 

- This option applies to methods 1 and 2.
- It refers to the % of words or letters that are unusual and above which the given 
  text is not English. By default, the threshold value is 25% which means that if more than 25% of words or letters in a given text
  are unusual, then the text is most likely not English.
- As explained in `method 1 <#method-1-detect-only-if-it-is-english-or-not-nltk-based-on-words>`_, a given text is considered
  unusual if there are words that are not part of the ``nltk`` English corpus. 

Method 1: detect only if it is English or not (``nltk`` + based on words)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
From the  `stackoverflow user 'William Niu' <https://stackoverflow.com/a/3384659>`_:

 Have you come across the following code snippet?
 
 from http://groups.google.com/group/nltk-users/browse_thread/thread/a5f52af2cbc4cfeb?pli=1&safe=active

.. code-block:: python

   english_vocab = set(w.lower() for w in nltk.corpus.words.words())
   text_vocab = set(w.lower() for w in text if w.lower().isalpha())
   unusual = text_vocab.difference(english_vocab) 

The `stackoverflow user 'whege' <https://stackoverflow.com/questions/3182268/nltk-and-language-detection#comment128930397_3384659>`_ comments the following about this code snippet:

 This is such a good answer. The simplicity of checking if the words are in the vocab is an 
 amazingly direct approach to this kind of task. Granted it doesn't give you the actual language 
 or translate, but if you simply need to know if it's an outlier, this is brilliant.

Thus method 1 is very restricted in its application: it can only tell if a given text is English or not. The way it does it is simple but still interesting depending on your use case: 

1. Every word (making sure they are all lowercase and consisting of alphabet letters) from a given text is checked 
   against the ``nltk`` English corpus
2. Those words from the given text that are not part of this corpus are considered as unusual
3. The proportion of words from the given text that are unusual is used to determine if the given text is English or not: if the proportion in % is 
   less than the threshold (By default, it is 25%), then the text is English. Otherwise, the text is not English.

`:information_source:` The threshold was not part of the original code snippet. It was added to allow binary classification of text (English or Not English) instead of just saying a given text is unusual/an outlier for having too many non-english words.

`:star:` The script can be found at `detect_lang.py <./scripts/detect_lang.py>`_. 

To run the script on the `eight texts <./scripts/detect_lang.py#L5>`_::

 $ python detect_lang.py -m 1
 
Ouput::

   Detecting text language with method #1
   importing nltk

   ###########################
   Text1: english (true label)
   ###########################
   The text is classified as English: 10% of words in the text are unusual (threshold = 25%)

   ###########################
   Text2: french (true label)
   ###########################
   The text is classified as non-English: 71% of words in the text are unusual (threshold = 25%)

   ###########################
   Text3: spanish (true label)
   ###########################
   The text is classified as non-English: 75% of words in the text are unusual (threshold = 25%)

   ###########################
   Text4: english (true label)
   ###########################
   The text is classified as English: 14% of words in the text are unusual (threshold = 25%)

   ###########################
   Text5: english (true label)
   ###########################
   The text is classified as English: 19% of words in the text are unusual (threshold = 25%)

   ###########################
   Text6: german (true label)
   ###########################
   The text is classified as non-English: 74% of words in the text are unusual (threshold = 25%)

   ###########################
   Text7: italian (true label)
   ###########################
   The text is classified as non-English: 79% of words in the text are unusual (threshold = 25%)

   ###########################
   Text8: french (true label)
   ###########################
   The text is classified as non-English: 72% of words in the text are unusual (threshold = 25%)

   ### Performance of method 1 ###
   0.0% error classification (labels: ENGLISH and NOT ENGLISH)

Extract DOB and DOD from text [TODO]
------------------------------------
`:warning:` TODO
