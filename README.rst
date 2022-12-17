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
---------------------------------------------------
This script tests different NLP methods to extract names from texts:

- The `first method <#method-1-nltk-part-of-speech-tag-nnp>`_ makes use of ``nltk`` to get all NPP with more than one part from a given text
- ...

`:star:` This Python script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_

Dependencies
''''''''''''
This is the environment on which the script was tested:

* **Platforms:** macOS
* **Python**: versions **3.7** and **3.8**
* For `method 1 <#method-1-nltk-part-of-speech-tag-nnp>`_:
  
  * `nltk (Natural Language Toolkit) <https://nltk.org/>`_: **v3.7**
  * `numpy <>`_: **v1.21.5** (Python 3.7) and **v1.23.4** (Python 3.8), necessary for ``nltk``

Usage for ``extract_names_from_text.py``
''''''''''''''''''''''''''''''''''''
Run the script ``extract_names_from_text.py``
`````````````````````````````````````````````
Run the script by specifying the method to use for extracting names from texts::

   $ pyton extract_names_from_text.py -m 1

`:information_source:` By default, the `first method <#method-1-nltk-part-of-speech-tag-nnp>`_ is used

List of options for ``extract_names_from_text.py``
```````````````````````````````````````````````````
To display the script's list of options and their descriptions, use the ``-h`` option::

   $ python extract_names_from_text.py -h
   
   usage: python extract_names_from_text.py [OPTIONS]

   Get names from texts

   optional arguments:
     -h, --help            show this help message and exit
     -m METHOD, --method METHOD
                           Method to use for extracting the names from texts.
                           (default: 1)
     -d, --download        Whether to download the nltk packages: punkt,
                           averaged_perceptron_tagger, maxent_ne_chunker, words
                           (default: False)

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
       
   names = get_human_names(text)
   print("LAST, FIRST")
   for name in names: 
       last_first = HumanName(name).last + ', ' + HumanName(name).first
       print(last_first)

`:information_source:`

  The `stackoverflow user 'Gihan Gamage' <https://stackoverflow.com/questions/20290870/improving-the-extraction-of-human-names-with-nltk#comment108366804_20290870>`_ suggests downloading the following nltk packages after the import statements: punkt, averaged_perceptron_tagger, maxent_ne_chunker, words

`:star:` The script can be found at `extract_names_from_text.py <./scripts/extract_names_from_text.py>`_. 

To run the script on the `four texts <./scripts/extract_names_from_text.py#L2>`_::

 $ python extract_names_from_text.py -m 1
 
Ouput::

   #########
   # Text1 #
   #########
   LAST, FIRST
   -----------
   Pauli, Ernst
   Einstein, Albert

   #########
   # Text2 #
   #########
   LAST, FIRST
   -----------
   Anderson, Harry
   Hartley, Miles
   Noyes, Pierre
   Kuhn, Thomas
   Silsbee, Henry
   Hasbrouck, John

   #########
   # Text3 #
   #########
   LAST, FIRST
   -----------
   II, Ferdinando
   Croce, Santa
   , Urban
   Barberini, Francesco

   #########
   # Text4 #
   #########
   LAST, FIRST
   -----------
   Velde, Francois
   Branson, Richard
   Galactic, Virgin
   Krugman, Paul
   Summers, Larry
   Colas, Nick

Extract DOB and DOD from text [TODO]
------------------------------------
`:warning:` TODO
