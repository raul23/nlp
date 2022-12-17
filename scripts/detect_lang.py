import argparse
import time
# Examples from Wikipedia
# Ref.: English and French
# https://en.wikipedia.org/wiki/Freeman_Dyson
# https://fr.wikipedia.org/wiki/Freeman_Dyson
text1 = """
Freeman John Dyson FRS (15 December 1923 – 28 February 2020) was an English-American 
theoretical physicist and mathematician known for his works in quantum field theory, 
astrophysics, random matrices, mathematical formulation of quantum mechanics, condensed 
matter physics, nuclear physics, and engineering.[a][8] He was Professor Emeritus in the 
Institute for Advanced Study in Princeton and a member of the Board of Sponsors of the 
Bulletin of the Atomic Scientists.

Il contribue notamment aux fondements de l'électrodynamique quantique en 1948. Il fait 
également de nombreuses contributions à la physique des solides, l’astronomie et l’ingénierie 
nucléaire. On lui doit plusieurs concepts qui portent son nom, tels que la transformée de 
Dyson (en) , l'arbre de Dyson (en) , la série de Dyson (en) et la sphère de Dyson.
"""

# Ref.: Spanish and English
# https://es.wikipedia.org/wiki/Enrico_Fermi
# https://en.wikipedia.org/wiki/Enrico_Fermi
text2 = """
Fermi mandó su tesis «Un teorema sobre probabilidad y algunas de sus aplicaciones» (en 
italiano, Un teorema di calcolo delle probabilità ed alcune sue applicazioni) a la Scuola Normale 
Superiore en julio de 1922, y recibió su licenciatura laureada a la temprana edad de 20 años. 
La tesis era sobre imágenes de difracción de rayos X. La Física Teórica no era considerada una 
disciplina en Italia y la única tesis que habría sido aceptada sería una sobre física 
experimental. Por esta razón los físicos italianos fueron lentos al incorporar nuevas ideas 
como la relatividad que venía de Alemania. Como Fermi se sentía como en casa en el laboratorio 
haciendo trabajo experimental, esto no supuso mayor problema para él.

Fermi was fond of pointing out that when Alessandro Volta was working in his laboratory, 
Volta had no idea where the study of electricity would lead.[145] Fermi is generally 
remembered for his work on nuclear power and nuclear weapons, especially the creation of 
the first nuclear reactor, and the development of the first atomic and hydrogen bombs. His 
scientific work has stood the test of time. This includes his theory of beta decay, his work 
with non-linear systems, his discovery of the effects of slow neutrons, his study of pion-nucleon 
collisions, and his Fermi–Dirac statistics. His speculation that a pion was not a fundamental 
particle pointed the way towards the study of quarks and leptons.
"""

# Ref.: English and German
# https://en.wikipedia.org/wiki/Theodor_Kaluza
# https://de.wikipedia.org/wiki/Theodor_Kaluza_(Physiker)
text3 = """
Kaluza's insight is remembered as the Kaluza–Klein theory (also named after physicist Oskar 
Klein). However, the work was neglected for many years, as attention was directed towards 
quantum mechanics. His idea that fundamental forces can be explained by additional dimensions 
did not re-emerge until string theory was developed. It is, however, also notable that many of 
the aspects of this body of work were already published in 1914 by Gunnar Nordström, but his 
work also went unnoticed and was not recognized when the ideas re-emerged.

Kaluza entstammte einer deutschen katholischen Familie aus der Stadt Ratibor in Oberschlesien 
(jetzt Racibórz in Polen). Er selbst wurde in Wilhelmsthal, einem Dorf, das 1899 der Stadt Oppeln 
(heute Opole) eingemeindet wurde, geboren. Seine Jugend verlebte er in Königsberg (Preußen), wo 
sein Vater Max Kaluza Professor für Anglistik war.
"""

# Ref.: Italian and French
# https://it.wikipedia.org/wiki/Makoto_Kobayashi_(fisico)
# https://fr.wikipedia.org/wiki/Makoto_Kobayashi_(physicien)
text4 = """
Makoto Kobayashi (小林誠 Kobayashi Makoto; Nagoya, 7 aprile 1944) è un fisico giapponese, 
molto conosciuto per il suo lavoro sulla violazione CP.

Il est co-lauréat avec Toshihide Maskawa du prix Nobel de physique de 2008 (l'autre moitié a 
été remise à Yoichiro Nambu) « pour la découverte de l'origine de la brisure de symétrie qui 
prédit l'existence d'au moins trois familles de quarks dans la nature ».
"""


def setup_argparser():
    msg = 'Detect language of a text'
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
                        help=f'Method to use to detect language of text. Choices are: [{choices_msg}]')
    parser.add_argument(
        '-d', '--download', action='store_true',
        help='Whether to download necessary nltk resoures for the selected method')
    return parser


if __name__ == '__main__':
    parser = setup_argparser()
    args = parser.parse_args()
    texts = [text1, text2, text3, text4]
    method_msg = f'Finding language of text with method #{args.method}'
    print(method_msg)
    time.sleep(1)
