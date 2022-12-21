===
NLP
===
.. contents:: **Contents**
   :depth: 4
   :local:
   :backlinks: top

Script #1: ``extract_names_from_text.py``: Extract names from text
==================================================================
This script tests different NLP methods to extract names from text:

- The `first method <#method-1-nltk-part-of-speech-tag-nnp>`_ makes use of ``nltk`` to get all NNP (proper noun, 
  singular) with more than one part from a given text and then the first and last names are returned
- The `second method <#method-2-spacy>`_ feeds the raw text to the NLP model `en_core_web_md 
  <https://spacy.io/models/en#en_core_web_md>`_ and then ``spacy`` produces a document containing among other 
  things named entities with the **PERSON** label. 

`:star:` 

   - The Python script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_
   - The script ``extract_names_from_text.py`` only imports the third-party libraries/modules necessary for the chosen method, 
     e.g. if you choose the `second method <#method-2-spacy>`_, only the ``spacy`` library is imported. Hence, if you 
     are just interested in one particular method, you won't need to download unnecessary libraries.

Texts used for testing
----------------------
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
-----------------------------------------------
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
----------------------------------------
Run the script **extract_names_from_text.py**
'''''''''''''''''''''''''''''''''''''''''''''
Run the script by specifying the method to use for extracting names from text::

   $ pyton extract_names_from_text.py -m 1

`:information_source:` By default, the `first method <#method-1-nltk-part-of-speech-tag-nnp>`_ is used

List of options for **extract_names_from_text.py**
''''''''''''''''''''''''''''''''''''''''''''''''''
To display the script's list of options and their descriptions, use the ``-h`` option::

   $ python extract_names_from_text.py -h
   
   usage: python extract_names_from_text.py [OPTIONS]

   Extract names from texts

   optional arguments:
     -h, --help            show this help message and exit
     -m METHOD, --method METHOD
                           Method to use for extracting the names from texts.
                           (default: 1)
     -d, --download        Whether to download necessary resources for the selected method
                           (default: False)

`:information_source:` These are the resources that need to be downloaded for each method (with the ``-d`` flag):

  - **Method 1:** 'punkt', 'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words'
  - **Method 2:** 'en_core_web_md'
  
`:star:` Ways to download and install the model 'en_core_web_md' necessary for `method 2 <#method-2-spacy>`_

  1. running the script ``extract_names_from_text.py`` with the ``-d`` flag::
  
      $ python extract_names_from_text.py -d
  2. Installing it separately from the script by running the following command on the terminal::
  
      $ python -m spacy download en_core_web_md

Method 1: ``nltk`` + part of speech tag **NNP**
-----------------------------------------------
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
    suggests downloading the following NLTK packages after the import statements: punkt, averaged_perceptron_tagger, 
    maxent_ne_chunker, words
  - The Python code returns the first and last name (e.g. Albert Einstein) for each person found in the text

Run method 1 (nltk)
'''''''''''''''''''
`:star:` The script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_. 

To run method 1 (``nltk``) on the `four texts <./scripts/extract_names_from_text.py#L2>`_::

 $ python extract_names_from_text.py -m 1
 
Ouput::

   Extracting names with method #1

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
-------------------
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

|

`:star:` The script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_. 

`:star:` Ways to download and install the model 'en_core_web_md' which is necessary for method 2

  1. running the script ``extract_names_from_text.py`` with the ``-d`` flag::
  
      $ python extract_names_from_text.py -d
  2. Installing it separately from the script by running the following command on the terminal::
  
      $ python -m spacy download en_core_web_md

|

`:information_source:` about the ``if`` condition

  - ``str(ent) not in names``: to avoid displaying duplicated names
  - ``len(ent) > 1``: to avoid displaying names with only one part (e.g. Anderson)

|
Run method 2 (spacy)
''''''''''''''''''''
`:star:` The script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_. 

To run method 2 (``spacy``) on the `four texts <./scripts/extract_names_from_text.py#L2>`_::

 $ python extract_names_from_text.py -m 2 -d
 
Ouput::

   Extracting names with method #2

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

Script #2: ``detect_lang.py``: Detect text language
===================================================
This script tests different NLP methods to detect text language:

- The `first method <#method-1-detect-only-if-it-is-english-or-not-i-e-binary-classification-nltk-english-corpus>`_ 
  checks each unique word from a given text against the ``nltk`` English corpus and if the % of words that are unusual 
  (i.e. not part of the corpus) exceeds a threshold, then the text is English. Otherwise, it is non-English. It is thus
  a simple binary classifier. Its application might be limited but depending on your use case, it might actually do the job.
- The `second method <#method-2-identify-text-language-with-nltk-classify-textcat>`_ uses the
  ``textcat`` classifier from ``nltk`` to determine the text language. It takes longer to process
  than the first method, but it is able to identify a text language which is returned as a language code in *ISO 639-3*, unlike the
  first method which can only tell if a text is English or not. ``textcat`` supports `255 languages <https://arxiv.org/pdf/1801.07779.pdf>`_.
- The `third method <#method-3-identify-text-language-with-langdetect>`_ uses
  ``langdetect`` to determine the text language. It is quicker to process than the first and second methods. Like the second and fourth
  methods, it is able to identify a text language which is returned as a language code in *ISO 639-1* 
  (`55 languages supported by langdetect <https://pypi.org/project/langdetect/>`_).
- The `fourth method <#method-4-identify-text-language-with-cld-2>`_ uses
  `Compact Langauge Detect 2 (CLD-2) <https://github.com/aboSamoor/pycld2>`_ to determine the text language. It is 
  quicker to process than all the other methods: it is almost instantaneous. It is able to identify multiple languages in text. 
  For each language detected, it returns a tuple containing among other things the language full name and the language code 
  in *ISO 639-1* (`over 165 languages supported by CLD-2 <https://github.com/aboSamoor/pycld2>`_).

`:star:` 

   - The Python script can be found at `detect_lang.py <./scripts/detect_lang.py>`_
   - The script ``detect_lang.py`` only imports the third-party libraries/modules necessary for the choosen method, 
     e.g. if you choose the `first method <#method-1-detect-only-if-it-is-english-or-not-i-e-binary-classification-nltk-english-corpus>`_, 
     only the ``nltk`` library is imported.

|

`:information_source:` Comparison of the CLD-2, ``textcat``, ``langdetect`` and ``langid`` tools for language identification.

.. raw:: html

  <p align="center"><img src="./images/comparison.png"></p>

This table is taken from Martin Thoma's excellent paper "The WiLI benchmark dataset for written 
language identification" where many NLP tools for language detection are tested and compared against
the `WiLI-2018 - Wikipedia Language Identification database <https://zenodo.org/record/841984>`_.

**Reference:** Thoma, Martin. `"The WiLI benchmark dataset for written language identification." <https://arxiv.org/abs/1801.07779>`_ 
*arXiv preprint arXiv:1801.07779* (2018).

Texts used for testing
----------------------
The script ``detect_lang.py`` is tested on the following eight texts (all taken from Wikpedia):

.. code-block:: python

   # Examples from Wikipedia
   # Ref.: https://en.wikipedia.org/wiki/Freeman_Dyson [ENGLISH]
   text1_english = """
   Freeman John Dyson FRS (15 December 1923 – 28 February 2020) was an English-American 
   theoretical physicist and mathematician known for his works in quantum field theory, 
   astrophysics, random matrices, mathematical formulation of quantum mechanics, condensed 
   matter physics, nuclear physics, and engineering.[a][8] He was Professor Emeritus in the 
   Institute for Advanced Study in Princeton and a member of the Board of Sponsors of the 
   Bulletin of the Atomic Scientists.
   """

   # Ref.: https://fr.wikipedia.org/wiki/Freeman_Dyson [FRENCH]
   text2_french = """
   Il contribue notamment aux fondements de l'électrodynamique quantique en 1948. Il fait 
   également de nombreuses contributions à la physique des solides, l’astronomie et l’ingénierie 
   nucléaire. On lui doit plusieurs concepts qui portent son nom, tels que la transformée de 
   Dyson (en) , l'arbre de Dyson (en) , la série de Dyson (en) et la sphère de Dyson.
   """

   # Ref.: https://es.wikipedia.org/wiki/Enrico_Fermi [SPANISH]
   text3_spanish = """
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
   text4_english = """
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
   text5_english = """
   Kaluza's insight is remembered as the Kaluza–Klein theory (also named after physicist Oskar 
   Klein). However, the work was neglected for many years, as attention was directed towards 
   quantum mechanics. His idea that fundamental forces can be explained by additional dimensions 
   did not re-emerge until string theory was developed. It is, however, also notable that many of 
   the aspects of this body of work were already published in 1914 by Gunnar Nordström, but his 
   work also went unnoticed and was not recognized when the ideas re-emerged.
   """

   # Ref.: https://de.wikipedia.org/wiki/Theodor_Kaluza_(Physiker) [German]
   text6_german = """
   Kaluza entstammte einer deutschen katholischen Familie aus der Stadt Ratibor in Oberschlesien 
   (jetzt Racibórz in Polen). Er selbst wurde in Wilhelmsthal, einem Dorf, das 1899 der Stadt Oppeln 
   (heute Opole) eingemeindet wurde, geboren. Seine Jugend verlebte er in Königsberg (Preußen), wo 
   sein Vater Max Kaluza Professor für Anglistik war.
   """

   # Ref.: https://it.wikipedia.org/wiki/Makoto_Kobayashi_(fisico) [ITALIAN]
   text7_italian = """
   Makoto Kobayashi (小林誠 Kobayashi Makoto; Nagoya, 7 aprile 1944) è un fisico giapponese, 
   molto conosciuto per il suo lavoro sulla violazione CP.
   """

   # Ref: https://fr.wikipedia.org/wiki/Makoto_Kobayashi_(physicien) [FRENCH]
   text8_french = """
   Il est co-lauréat avec Toshihide Maskawa du prix Nobel de physique de 2008 (l'autre moitié a 
   été remise à Yoichiro Nambu) « pour la découverte de l'origine de la brisure de symétrie qui 
   prédit l'existence d'au moins trois familles de quarks dans la nature ».
   """

Dependencies for **detect_lang.py**
-----------------------------------
This is the environment on which the script ``detect_lang.py`` was tested:

* **Platforms:** macOS
* **Python**: versions **3.7** and **3.8**
* For `method 1 <#method-1-detect-only-if-it-is-english-or-not-i-e-binary-classification-nltk-english-corpus>`_ (``nltk`` English corpus):
  
  * `nltk (Natural Language Toolkit) <https://nltk.org/>`_: **v3.7**, "for building Python programs to work 
    with human language data"
  
    ``pip install nltk``
  * `numpy <https://numpy.org/>`_: **v1.21.5** (Python 3.7) and **v1.23.4** (Python 3.8), `optional 
    <https://www.nltk.org/install.html#mac-unix>`_ for ``nltk``
    
    ``pip install numpy``
* For `method 2 <#method-2-identify-text-language-with-nltk-classify-textcat>`_ (``nltk.classify.textcat``):
  
  * `nltk (Natural Language Toolkit) <https://nltk.org/>`_: **v3.7**, "for building Python programs to work 
    with human language data"
  
    ``pip install nltk``
  * `numpy <https://numpy.org/>`_: **v1.21.5** (Python 3.7) and **v1.23.4** (Python 3.8), `optional 
    <https://www.nltk.org/install.html#mac-unix>`_ for ``nltk``
    
    ``pip install numpy``
  * `pycountry <https://pypi.org/project/pycountry/>`_: **v22.3.5** it's **optional**. Used for converting the language 
    code returned by ``nltk.classify.textcat`` into the language full name. If ``pycountry`` is not found, then only binary 
    classification will be done (i.e. detect if a given text is English or non-English).
    
    ``pip install pycountry``
* For `method 3 <#method-3-identify-text-language-with-langdetect>`_ (``langdetect``):
  
  * `langdetect <https://pypi.org/project/langdetect/>`_: **v1.0.9**, a direct port of Google's language-detection 
    library from Java to Python
    
    ``pip install langdetect``
  * `pycountry <https://pypi.org/project/pycountry/>`_: **v22.3.5** it's **optional**. Used for converting the language 
    code returned by ``nltk.classify.textcat`` into the language full name. If ``pycountry`` is not found, then only binary 
    classification will be done (i.e. detect if a given text is English or non-English).
    
    ``pip install pycountry``
* For `method 4 <#method-4-identify-text-language-with-cld-2>`_ (**CLD-2**):
  
  * `pycld2 <https://github.com/aboSamoor/pycld2>`_: **v0.41**, Python bindings for the Compact Langauge Detect 2 (CLD2)
  
  ``pip install pycld2``
* For `method 5 <#method-5-identify-text-language-with-langid>`_ (``langid``):
  
  * `languid <https://pypi.org/project/langid/>`_: **v1.1.6**, a standalone Language Identification (LangID) tool.
  
    ``pip install pycld2``
  * `numpy <https://numpy.org/>`_: **v1.21.5** (Python 3.7) and **v1.23.4** (Python 3.8), **required** internally for ``languid``
  
  ``pip install numpy``

Usage for **detect_lang.py**
----------------------------
Run the script **detect_lang.py**
'''''''''''''''''''''''''''''''''
Run the script by specifying the method to use for detecting the text language::

   $ pyton extract_names_from_text.py -m 1

`:information_source:` By default, the `first method <#method-1-detect-only-if-it-is-english-or-not-i-e-binary-classification-nltk-english-corpus>`_ is used.

List of options for **detect_lang.py**
''''''''''''''''''''''''''''''''''''''
To display the script's list of options and their descriptions, use the ``-h`` option::

   $ python detect_lang.py -h
   
   usage: python detect_lang.py [OPTIONS]

   Detect text language

   optional arguments:
     -h, --help            show this help message and exit
     -m METHOD, --method METHOD
                           Method to use for detecting text language. Choices are 
                           1: nltk English corpus, 
                           2: nltk.classify.textcat, 
                           3: langdetect 
                           4: cld2
                           5: langid
                           (default: 1)
     -t THRESHOLD, --threshold THRESHOLD
                           If this threshold (% of words in the text vocabulary that are unusual) 
                           is exceeded, then the language of the text is not English. NOTE: This is
                           an option for method 1. (default: 25)
     -d, --deterministic   Make the language detection algorithm used for method 3 (langdetect) 
                           deterministic. (default: False)
     -v, --verbose         Show more information for the given method such as the words considered 
                           as unusual (method 1). (default: False)
     --log-level {debug,info,warning,error}
                           Set logging level. (default: info)

`:information_source:` The ``-t/--threshold`` option 

- This option applies to `method 1 <#method-1-detect-only-if-it-is-english-or-not-i-e-binary-classification-nltk-english-corpus>`_.
- It refers to the % of unique words from a given text that are unusual and above which the 
  text is not English. By default, the threshold value is 25% which means that if more than 25% of unique words in a given text
  are unusual, then the text is most likely not English.
- As explained in `method 1 <#method-1-detect-only-if-it-is-english-or-not-i-e-binary-classification-nltk-english-corpus>`_, 
  a given text is considered unusual if there are words that are not part of the ``nltk`` English corpus. 

|

`:information_source:` The ``-d/--deterministic`` option sets the seed used by ``langdetect`` to 0 in order for the
language detection algorithm to be `deterministic <https://pypi.org/project/langdetect/>`_. Hence, everytime you run 
the code on a given text, you will get the same result.

|

`:star:` By default, the `second method <#method-2-identify-text-language-with-nltk-classify-textcat>`_ 
performs multiclass classification (if ``pycountry`` is found) but if the ``-v/--verbose`` option is used, then results for binary 
classification are also shown.

Method 1: detect only if it is English or not, i.e. binary classification (``nltk`` English corpus)
---------------------------------------------------------------------------------------------------
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

|

Thus method 1 is limited in its application: it can only tell if a given text is English or not (a simple binary classifier). 
The way it does it is simple but still interesting depending on your use case: 

1. Every unique word (making sure they are all lowercase and consisting of alphabet letters) from a given text is checked 
   against the ``nltk`` English corpus
2. Those words from the given text that are not part of this corpus are considered as unusual
3. The proportion of unique words from the given text that are unusual is used to determine if the given text is English or 
   not: if the proportion in % is less than the threshold (by default, it is 25%), then the text is English. Otherwise, the 
   text is non-English.

`:information_source:` 

   - The **threshold** was not part of the original code snippet. It was added to allow binary classification 
     of text (English or Not English) instead of just saying a given text is unusual/an outlier for having too many non-English words.
   - You could even save locally the ``nltk`` English corpus and hence no need to import ``nltk``. Depending on your use case, this
     might be worthwhile as your code won't depend on a third-party library for a simple task of detecting whether a given text is English or not.
   - Another possible addition is to use corpora from other languages (e.g. French, Spanish) so you can convert this binary classifier
     into a multiclass classifier capable of identifying many text languages.

Run method 1 (nltk English corpus)
''''''''''''''''''''''''''''''''''
`:star:` The script can be found at `detect_lang.py <./scripts/detect_lang.py>`_. 

To run method 1 (``nltk`` English corpus) on the `eight texts <./scripts/detect_lang.py#L5>`_::

 $ python detect_lang.py -m 1
 
Ouput::

   Verbose option disabled
   importing nltk

   Detecting text language with method #1: nltk English corpus

   #############################
   Text1: english (true language)
   #############################
   The text is classified as english: 10% of words in the text vocabulary are unusual (threshold = 25%)
   VALID classification
   Took 0.212 second

   #############################
   Text2: french (true language)
   #############################
   The text is classified as non-english: 71% of words in the text vocabulary are unusual (threshold = 25%)
   VALID classification
   Took 0.206 second

   #############################
   Text3: spanish (true language)
   #############################
   The text is classified as non-english: 75% of words in the text vocabulary are unusual (threshold = 25%)
   VALID classification
   Took 0.208 second

   #############################
   Text4: english (true language)
   #############################
   The text is classified as english: 14% of words in the text vocabulary are unusual (threshold = 25%)
   VALID classification
   Took 0.198 second

   #############################
   Text5: english (true language)
   #############################
   The text is classified as english: 19% of words in the text vocabulary are unusual (threshold = 25%)
   VALID classification
   Took 0.201 second

   #############################
   Text6: german (true language)
   #############################
   The text is classified as non-english: 74% of words in the text vocabulary are unusual (threshold = 25%)
   VALID classification
   Took 0.202 second

   #############################
   Text7: italian (true language)
   #############################
   The text is classified as non-english: 79% of words in the text vocabulary are unusual (threshold = 25%)
   VALID classification
   Took 0.199 second

   #############################
   Text8: french (true language)
   #############################
   The text is classified as non-english: 72% of words in the text vocabulary are unusual (threshold = 25%)
   VALID classification
   Took 0.202 second


   ### Performance of method 1: nltk English corpus ###
   task: binary classification
   0.0% error classification

   Total time: 1.63 second

Method 2: identify text language with ``nltk.classify.textcat``
---------------------------------------------------------------
From the  `stackoverflow user 'RK1' <https://stackoverflow.com/a/58432286>`_:

 Super late but, you could use ``textcat`` classifier in ``nltk``, `here 
 <https://www.nltk.org/api/nltk.classify.html#nltk.classify.textcat.TextCat>`_. 
 This `paper <http://www.let.rug.nl/~vannoord/TextCat/textcat.pdf>`_ discusses the algorithm.

 It returns a language code in ISO 639-3, so I would use ``pycountry`` to get the full name.

.. code-block:: python

   import nltk
   import py
   
   
   phrase_one = "good morning"
   phrase_two = "goeie more"

   tc = nltk.classify.textcat.TextCat() 
   guess_one = tc.guess_language(phrase_one)
   guess_two = tc.guess_language(phrase_two)

   guess_one_name = pycountry.languages.get(alpha_3=guess_one).name
   guess_two_name = pycountry.languages.get(alpha_3=guess_two).name
   print(guess_one_name)
   print(guess_two_name)

Output::

 English
 Afrikaans
   
However, `RK1 <https://stackoverflow.com/a/58432286>`_ also warns that this method is not 100% reliable:

 Disclaimer obviously this will not always work, especially for sparse data

 Extreme example

 .. code-block:: python
 
    guess_example = tc.guess_language("hello")
    print(pycountry.languages.get(alpha_3=guess_example).name)
    Konkani (individual language)

|

`:information_source:` 

   - This second method is capable of identifying many languages, unlike the `first method 
     <#method-1-detect-only-if-it-is-english-or-not-i-e-binary-classification-nltk-english-corpus>`_ which can only tell if the text is
     English or non-English.
   - However, compared to the first method, the second method takes longer to process when performing 
     binary classification: more than 10 times longer.
   - `pycountry <https://pypi.org/project/pycountry/>`_ is optional. It is used for converting the language code 
     returned by ``nltk.classify.textcat`` into the language full name. If ``pycountry`` is not found, then only binary 
     classification will be performed (i.e. detect if a given text is English or non-English).
     
     To install it: ``pip install pycountry``
 
Run method 2 (nltk.classify.textcat)
''''''''''''''''''''''''''''''''''''
`:star:` The script can be found at `detect_lang.py <./scripts/detect_lang.py>`_. 

To run method 2 (``nltk.classify.textcat``) on the `eight texts <./scripts/detect_lang.py#L5>`_::

 $ python detect_lang.py -m 2
 
Ouput::

   Verbose option disabled
   importing nltk
   importing pycountry

   Detecting text language with method #2: nltk.classify.textcat

   #############################
   Text1: english (true language)
   #############################
   classifying ...
   The text is classified as english [valid]
   Took 5.247 seconds

   #############################
   Text2: french (true language)
   #############################
   classifying ...
   The text is classified as french [valid]
   Took 1.654 second

   #############################
   Text3: spanish (true language)
   #############################
   classifying ...
   The text is classified as portuguese [invalid]
   Took 3.893 seconds

   #############################
   Text4: english (true language)
   #############################
   classifying ...
   The text is classified as english [valid]
   Took 3.52 seconds

   #############################
   Text5: english (true language)
   #############################
   classifying ...
   The text is classified as english [valid]
   Took 2.924 seconds

   #############################
   Text6: german (true language)
   #############################
   classifying ...
   The text is classified as german [valid]
   Took 1.998 second

   #############################
   Text7: italian (true language)
   #############################
   classifying ...
   The text is classified as english [invalid]
   Took 0.898 second

   #############################
   Text8: french (true language)
   #############################
   classifying ...
   The text is classified as french [valid]
   Took 1.604 second


   ### Performance of method 2: nltk.classify.textcat ###
   task: multiclass classification
   25.0% error classification

   Total time: 21.74 seconds

|

`:star:` By default, the second method shows results for the multiclass classification (if the ``pycountry`` package is found) 
but if the ``-v/--verbose`` option is used, then results for binary classification are also shown so you can compare them with 
those of the other methods.

We are only showing results for the last text analyzed::

 $ python detect_lang.py -m 2 -v
 
Ouput::

   #############################
   Text8: french (true language)
   #############################
   Number of words in the text: 45
   classifying ...
   Guessed language: fra
   Binary classification: the text is classified as non-english [valid]
   The text is classified as french [valid]
   Took 1.674 second


   ### Performance of method 2: nltk.classify.textcat ###
   task: binary classification
   12.5% error classification

   task: multiclass classification
   25.0% error classification

   Total time: 22.53 seconds

Method 3: identify text language with ``langdetect``
----------------------------------------------------
``langdetect`` is a port of Nakatani Shuyo's language-detection library (version from 03/03/2014) from Java to Python 
(see `official documentation <https://pypi.org/project/langdetect/>`_).

From the  `stackoverflow user 'SVK' <https://stackoverflow.com/a/38752290>`_:

 This library is not from NLTK either but certainly helps.

 ``$ sudo pip install langdetect``

 Supported Python versions 2.6, 2.7, 3.x.

 .. code-block:: python
 
    >>> from langdetect import detect

    >>> detect("War doesn't show who's right, just who's left.")
    'en'
    >>> detect("Ein, zwei, drei, vier")
    'de'
    
 https://pypi.org/project/langdetect/
 
 P.S.: Don't expect this to work correctly always:
 
 .. code-block:: python
 
      >>> detect("today is a good day")
      'so'
      >>> detect("today is a good day.")
      'so'
      >>> detect("la vita e bella!")
      'it'
      >>> detect("khoobi? khoshi?")
      'so'
      >>> detect("wow")
      'pl'
      >>> detect("what a day")
      'en'
      >>> detect("yay!")
      'so'

`:warning:` As the `official documentation notes <https://pypi.org/project/langdetect/>`_, the algorithm is **non-deterministic**. 
Thus, if you run the code multiple times on a given text, you might get different results. Especially if the text is very short or 
ambiguous (e.g. using two languages). To make sure you get the same results, set the seed to 0 before running the language detection code:

.. code-block:: python

   from langdetect import DetectorFactory
   DetectorFactory.seed = 0

|

`:information_source:` 

   - This third method is capable of identifying many languages, just like the `second method 
     <#method-2-identify-text-language-with-nltk-classify-textcat>`_.
   - However, compared to the `second method <#method-2-identify-text-language-with-nltk-classify-textcat>`_, 
     the third method takes way less time to process when performing language classification: more than 30 times quicker.
   - Also, the third method is quicker than the `first method  
     <#method-1-detect-only-if-it-is-english-or-not-i-e-binary-classification-nltk-english-corpus>`_ when performing 
     binary classification: more than twice faster.
   - `pycountry <https://pypi.org/project/pycountry/>`_ is optional. It is used for converting the language code 
     returned by ``langdetect.detect`` into the language full name. If ``pycountry`` is not found, then only binary 
     classification will be performed (i.e. detect if a given text is English or non-English).
     
     To install it: ``pip install pycountry``

Run method 3 (langdetect)
'''''''''''''''''''''''''
`:star:` The script can be found at `detect_lang.py <./scripts/detect_lang.py>`_. 

To run method 3 (``langdetect``) on the `eight texts <./scripts/detect_lang.py#L5>`_::

 $ python detect_lang.py -m 3
 
Ouput::

   Verbose option disabled
   importing langdetect.detect
   importing pycountry

   Detecting text language with method #3: langdetect

   #############################
   Text1: english (true language)
   #############################
   The text is classified as english [valid]
   Took 0.562 second

   #############################
   Text2: french (true language)
   #############################
   The text is classified as french [valid]
   Took 0.007 second

   #############################
   Text3: spanish (true language)
   #############################
   The text is classified as spanish [valid]
   Took 0.013 second

   #############################
   Text4: english (true language)
   #############################
   The text is classified as english [valid]
   Took 0.007 second

   #############################
   Text5: english (true language)
   #############################
   The text is classified as english [valid]
   Took 0.007 second

   #############################
   Text6: german (true language)
   #############################
   The text is classified as german [valid]
   Took 0.007 second

   #############################
   Text7: italian (true language)
   #############################
   The text is classified as italian [valid]
   Took 0.006 second

   #############################
   Text8: french (true language)
   #############################
   The text is classified as french [valid]
   Took 0.006 second


   ### Performance of method 3: langdetect ###
   task: multiclass classification
   0.0% error classification

   Total time: 0.57 second

`:star:` By default, the third method shows results for the multiclass classification (if the ``pycountry`` package is found) 
but if the ``-v/--verbose`` option is used, then results for binary classification are also shown so you can compare them with 
those of the other methods.

We are only showing results for the last text analyzed::

 $ python detect_lang.py -m 3 -v -d
 
Ouput::

   #############################
   Text8: french (true language)
   #############################
   Number of words in the text: 45
   Seed=0
   Guessed language: fr
   Binary classification: the text is classified as non-english [valid]
   The text is classified as french [valid]
   Took 0.006 second


   ### Performance of method 3: langdetect ###
   task: binary classification
   0.0% error classification

   task: multiclass classification
   0.0% error classification

   Total time: 0.64 second

`:information_source:` We also used the ``-d/--deterministic`` option. Hence, the seed is set to 0.

Method 4: identify text language with **CLD-2**
-----------------------------------------------
From Dick Sites' `documentation <https://github.com/CLD2Owners/cld2>`_ for the ``cld2`` C++ library:

 - CLD2 probabilistically detects over 80 languages in Unicode UTF-8 text, either plain text or HTML/XML.
 - The design target is web pages of at least 200 characters (about two sentences); CLD2 is not designed 
   to do well on very short text, lists of proper names, part numbers, etc.
 - CLD2 is a Naïve Bayesian classifier, using one of three different token algorithms.

The  `stackoverflow user 'Martin Thoma' <https://stackoverflow.com/a/48436520>`_ compared **CLD-2** with other NLP 
tools for language identification:

 You might be interested in my paper `The WiLI benchmark dataset for written language identification 
 <https://arxiv.org/pdf/1801.07779.pdf>`_. I also benchmarked a couple of tools.

 TL;DR:

 - CLD-2 is pretty good and extremely fast
 - `lang-detect <https://pypi.python.org/pypi/langdetect>`_ is a tiny bit better, but much slower
 - langid is good, but CLD-2 and lang-detect are much better
 - NLTK's Textcat is neither efficient nor effective.
   
 You can install `lidtk <https://github.com/MartinThoma/lidtk>`_ and classify languages::
 
   $ lidtk cld2 predict --text "this is some text written in English"
   eng
   $ lidtk cld2 predict --text "this is some more text written in English"
   eng
   $ lidtk cld2 predict --text "Ce n'est pas en anglais"                  
   fra

|

`:information_source:` The GitHub pages of **CLD-2** Python bindings are 

- Rami Al-Rfou et al.: https://github.com/aboSamoor/pycld2 [NOTE: this is the one used in method 4]

  ``$ pip install pycld2``
- Greg Bowyer et al.: https://github.com/GregBowyer/cld2-cffi

  ``$ pip install cld2-cffi``

Run method 4 (**CLD-2**)
''''''''''''''''''''''''
`:star:` The script can be found at `detect_lang.py <./scripts/detect_lang.py>`_. 

To run method 4 (**CLD-2**) on the `eight texts <./scripts/detect_lang.py#L5>`_::

 $ python detect_lang.py -m 4
 
Ouput::

   Verbose option disabled
   importing pycld2

   Detecting text language with method #4: cld2

   #############################
   Text1: english (true language)
   #############################
   The text is classified as english [valid]
   Took 0.001 second

   #############################
   Text2: french (true language)
   #############################
   The text is classified as french [valid]
   Took 0.0 second

   #############################
   Text3: spanish (true language)
   #############################
   The text is classified as spanish [valid]
   Took 0.0 second

   #############################
   Text4: english (true language)
   #############################
   The text is classified as english [valid]
   Took 0.0 second

   #############################
   Text5: english (true language)
   #############################
   The text is classified as english [valid]
   Took 0.0 second

   #############################
   Text6: german (true language)
   #############################
   The text is classified as german [valid]
   Took 0.0 second

   #############################
   Text7: italian (true language)
   #############################
   The text is classified as italian [valid]
   Took 0.0 second

   #############################
   Text8: french (true language)
   #############################
   The text is classified as french [valid]
   Took 0.0 second


   ### Performance of method 4: cld2 ###
   task: multiclass classification
   0.0% error classification

   Total time: 0.0 second

`:star:` By default, the fourth method shows results for the multiclass classification 
but if the ``-v/--verbose`` option is used, then results for binary classification are also shown so you can compare them with 
those of the other methods.

We are only showing results for the last text analyzed::

 $ python detect_lang.py -m 4 -v 
 
Ouput::

   #############################
   Text8: french (true language)
   #############################
   Number of words in the text: 45
   Guessed language: fr
   Binary classification: the text is classified as non-english [valid]
   The text is classified as french [valid]
   Took 0.0 second


   ### Performance of method 4: cld2 ###
   task: binary classification
   0.0% error classification

   task: multiclass classification
   0.0% error classification

   Total time: 0.0 second

Method 5: identify text language with ``langid``
------------------------------------------------
From the `official documentation <https://github.com/saffsd/langid.py>`_:

   ``langid.py`` is a standalone Language Identification (LangID) tool.

   The design principles are as follows:

   1. Fast
   2. Pre-trained over a large number of languages (currently 97)
   3. Not sensitive to domain-specific features (e.g. HTML/XML markup)
   4. Single .py file with minimal dependencies
   5. Deployable as a web service
