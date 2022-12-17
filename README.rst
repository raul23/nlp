===
NLP
===
.. contents:: **Contents**
   :depth: 4
   :local:
   :backlinks: top

Scripts
=======
**extract_names_from_text.py**: Extract names from text
-------------------------------------------------------
This script tests different NLP methods to extract names from text:

- The `first method <#method-1-nltk-part-of-speech-tag-nnp>`_ makes use of ``nltk`` to get all NNP (proper noun, 
  singular) with more than one part from a given text and then the first and last names are returned
- The `second method <#method-2-spacy>`_ feeds the raw text to the NLP model `en_core_web_md 
  <https://spacy.io/models/en#en_core_web_md>`_, spacy produces a document containing among other things named entities. 

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
  * `numpy <https://numpy.org/>`_: **v1.21.5** (Python 3.7) and **v1.23.4** (Python 3.8), necessary for ``nltk``
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

Method 1: ``nltk`` + part of speech tag ``NNP``
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
Feeding the raw text to the NLP model `en_core_web_md <https://spacy.io/models/en#en_core_web_md>`_, ``spacy`` produces a document containing among other things named entities. The entities that are of interest to us are those labeled as **PERSON**.

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
   print()

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

Extract DOB and DOD from text [TODO]
------------------------------------
`:warning:` TODO
