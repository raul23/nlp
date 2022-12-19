import argparse
import sys
import time

nltk = None
pycountry = None

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


def import_modules(method, download):
    global nltk, pycountry
    if method in [1, 2]:
        print('importing nltk')
        import nltk
        if method == 2:
            try:
                import pycountry
            except ImportError:
                print("The package pycountry is not installed. Thus only "
                      "binary classification of text language will be performed.")
    else:
        print(f'Unsupported method #{method}')
    if download:
        download_packages(method)


# Ref.: https://stackoverflow.com/a/3384659
def is_text_english(text, threshold, verbose):
    text = text.split()
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    text_vocab = set(w.lower() for w in text if w.lower().isalpha())
    unusual = text_vocab.difference(english_vocab)
    prop_unusual = len(unusual) / len(text_vocab)
    msg = f'{round(prop_unusual*100)}% of words in the text vocabulary are unusual (threshold = {threshold}%)'
    if verbose:
        print(f'unusual words: {unusual}')
    if prop_unusual * 100 > threshold:
        print(f'The text is classified as non-english: {msg}')
        return False
    else:
        print(f'The text is classified as english: {msg}')
        return True


# Ref.: https://stackoverflow.com/a/25300927
def range_type(astr, min=0, max=100):
    if astr.isdecimal():
        value = int(astr)
    else:
        value = float(astr)
    if min <= value <= max:
        return value
    else:
        raise argparse.ArgumentTypeError(f'value not in range [{min}, {max}]')


def setup_argparser():
    msg = 'Detect text language'
    parser = argparse.ArgumentParser(
        description='',
        usage=f"python %(prog)s [OPTIONS]\n\n{msg}",
        # ArgumentDefaultsHelpFormatter
        # HelpFormatter
        # RawDescriptionHelpFormatter
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    choices = [1, 2]
    choices_msg = ', '.join(map(str, choices))
    parser.add_argument('-m', '--method', metavar='METHOD', dest='method', choices=choices,
                        default=1, type=int,
                        help=f'Method to use to detect text language. Choices are: [{choices_msg}]')
    parser.add_argument('-t', '--threshold', metavar='THRESHOLD', dest='threshold',
                        default=25, type=range_type,
                        help='If this threshold (%% of words in the text vocabulary that are unusual) '
                             'is exceeded, then the language of the text is not English.')
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='Show more information for the given method such as the words considered as unusual (method 1).')
    return parser


if __name__ == '__main__':
    parser = setup_argparser()
    args = parser.parse_args()
    texts = [(v, k.split('_')[-1]) for k, v in globals().items() if k.startswith('text')]
    method_msg = f'Detecting text language with method #{args.method}'
    print(method_msg)
    time.sleep(1)
    import_modules(args.method, False)
    print()
    binary_class_error = 0
    multi_class_error = 0
    total_time = 0
    for i, (text, true_lang) in enumerate(texts, start=1):
        print("#############################")
        print(f'Text{i}: {true_lang} (true language)')
        print("#############################")
        start_time = time.time()
        if args.method == 1:
            is_english = is_text_english(text, args.threshold, args.verbose)
            guess_lang = 'english' if is_english else true_lang
            if guess_lang != true_lang:
                binary_class_error += 1
                print('INVALID classification')
            else:
                print('VALID classification')
        elif args.method == 2:
            print('classifying ...')
            tc = nltk.classify.textcat.TextCat()
            guess_lang = tc.guess_language(text)
            # Binary classification
            binary_guess_lang = 'english' if guess_lang == 'eng' else true_lang
            if binary_guess_lang != true_lang:
                binary_class_error += 1
                valid_msg = '[invalid]'
            else:
                valid_msg = '[valid]'
            if args.verbose:
                msg = 'Binary classification: the text is classified as'
                if binary_guess_lang != 'english':
                    print(f'{msg} non-english {valid_msg}')
                else:
                    print(f'{msg} english {valid_msg}')
            # Multi-classification
            try:
                guess_lang_name = pycountry.languages.get(alpha_3=guess_lang).name.lower()
            except ImportError:
                pass
            else:
                if guess_lang_name != true_lang:
                    multi_class_error += 1
                    valid_msg = '[invalid]'
                else:
                    valid_msg = '[valid]'
                print(f'The text is classified as {guess_lang_name} {valid_msg}')
        else:
            print(f'Unsupported method #{args.method}')
            sys.exit(1)
        time_current_text = time.time() - start_time
        total_time += time_current_text
        print(f"Took {round(time_current_text, 3)} second{'s' if time_current_text >= 2 else ''}")
        print()
    print(f'\n### Performance of method {args.method} ###')
    # Messages for methods 1 and 2
    msg1 = 'task: binary classification'
    msg2 = f'{binary_class_error/len(texts)*100}% error classification'
    if args.method == 1:
        print(msg1)
        print(msg2)
    elif args.method == 2:
        if args.verbose:
            print(msg1)
            print(msg2 + '\n')
        print('task: multi-classification')
        print(f'{multi_class_error/len(texts)*100}% error classification')
    else:
        print(f'Unsupported method #{args.method}')
        sys.exit(1)
    print(f"\nTotal time: {round(total_time, 2)} second{'s' if total_time >= 2 else ''}")
