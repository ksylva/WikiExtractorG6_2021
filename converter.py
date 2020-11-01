# Convert the html tables to csv file format
import pandas as pd

chaine = """
<table class="wikitable">
<tbody><tr>
<th>Aspect
</th>
<th>Esperanto
</th>
<th>Ido
</th>
<th>Example
</th></tr>
<tr>
<th>Alphabet
</th>
<td>uses <a href="/wiki/Diacritics" class="mw-redirect" title="Diacritics">diacritics</a><br />(ĉ, ĝ, ĥ, ĵ, ŝ, ŭ)<br />and a digraph<br />(dz)
</td>
<td>uses <a href="/wiki/Digraph_(orthography)" title="Digraph (orthography)">digraphs</a><br />(ch, sh, qu)
</td>
<td>Translation of "chamber", "shoe", and "square":<br /><i><span style="color:red;"><b>ĉ</b></span>ambro</i> / <i><span style="color:red;"><b>ŝ</b></span>uo</i> / <i><span style="color:red;"><b>kv</b></span>adrato</i> (Esp.)<br /><i><span style="color:red;"><b>ch</b></span>ambro</i> / <i><span style="color:red;"><b>sh</b></span>uo</i> / <i><span style="color:red;"><b>qu</b></span>adrato</i> (Ido)
</td></tr>
<tr>
<th>Gender
</th>
<td>masculine by default;<br />feminine optional
</td>
<td>gender-neutral by default;<br />masculine and<br /> feminine optional
</td>
<td>Gender of "elephant":<br /><i>elefanto</i> (default) / <i>elefantino</i> (fem.) (Esp.)<br /><i>elefanto</i> (default) / <i>elefantulo</i> (masc.) / <i>elefantino</i> (fem.) (Ido)
</td></tr>
<tr>
<th>Antonyms
</th>
<td>formed by <i>mal-</i> prefix
</td>
<td>come from<br />natural vocabulary
</td>
<td>Translation of "warm" and "cold":<br /><i>varma</i> / <i><span style="color:red;"><b>mal</b></span>varma</i> (Esp.)<br /><i>varma</i> / <i>kolda</i> (Ido)
</td></tr>
<tr>
<th>Infinitives
</th>
<td><i>-i</i> suffix
</td>
<td><i>-ar</i> suffix
</td>
<td>Translation of "to go":<br /><i>ir<span style="color:red;"><b>i</b></span></i> (Esp.)<br /><i>ir<span style="color:red;"><b>ar</b></span></i> (Ido)
</td></tr>
<tr>
<th>Imperative
</th>
<td><i>-u</i> suffix
</td>
<td><i>-ez</i> suffix
</td>
<td>Translation of "go!":<br /><i>ir<span style="color:red;"><b>u</b></span>!</i> (Esp.)<br /><i>ir<span style="color:red;"><b>ez</b></span>!</i> (Ido)
</td></tr>
<tr>
<th>Plural noun
</th>
<td><i>-oj</i> suffix<br />(<a href="/wiki/Agglutinative" class="mw-redirect" title="Agglutinative">agglutinative</a>)
</td>
<td><i>-i</i> suffix<br />(synthetic)
</td>
<td>Plural of <i>domo</i> ("house"):<br /><i>dom<span style="color:red;"><b>oj</b></span></i> (Esp.)<br /><i>dom<span style="color:red;"><b>i</b></span></i> (Ido)
</td></tr>
<tr>
<th>Adjectives
</th>
<td>Agree with nouns
</td>
<td>Not declined
</td>
<td>Translation of "big dogs":<br /><i>granda<span style="color:red;"><b>j</b></span> hundoj</i> (Esp.)<br /><i>granda hundi</i> (Ido)
</td></tr>
<tr>
<th>Accusative<br />form
</th>
<td>Mandatory
</td>
<td>Only when object<br />precedes subject
</td>
<td>Translation of "I drink milk" / "I milk drink":<br />"mi trinkas lakto<span style="color:red;"><b>n</b></span>" / "mi lakton trinkas" (Esp.)<br />"me drinkas lakto" / "me lakton drinkas" (Ido)
</td></tr>
<tr>
<th>Proper<br />nouns
</th>
<td>Sometimes rendered
</td>
<td>Never rendered
</td>
<td>Translation of "Europe":<br /><i>Eŭropo</i> (Esp.)<br /><i>Europa</i> (Ido)
</td></tr>
<tr>
<th>No. of<br />speakers
</th>
<td>c. 100,000–2,000,000
</td>
<td>c. 100–1,000
</td>
<td>
</td></tr></tbody></table>"""

chaine_2 = """<table class="wikitable">

<tbody><tr>
<th>Grammatical form
</th>
<th>Ido
</th>
<th colspan="2">English
</th>
<th colspan="2">Esperanto
</th></tr>
<tr>
<th><a href="/wiki/Noun" title="Noun">Singular noun</a>
</th>
<td><b> -o</b> (libro)
</td>
<td colspan="2">book
</td>
<td colspan="2"><b>-o</b> (libro)
</td></tr>
<tr>
<th><a href="/wiki/Noun" title="Noun">Plural noun</a>
</th>
<td><b>-i</b> (libri)
</td>
<td colspan="2">books
</td>
<td colspan="2"><b>-oj</b> (libroj)
</td></tr>
<tr>
<th><a href="/wiki/Adjective" title="Adjective">Adjective</a>
</th>
<td><b>-a</b> (varma)
</td>
<td colspan="2">warm
</td>
<td colspan="2"><b>-a</b> (varma)
</td></tr>
<tr>
<th><a href="/wiki/Adverb" title="Adverb">Adverb</a>
</th>
<td><b>-e</b> (varme)
</td>
<td colspan="2">warmly
</td>
<td colspan="2"><b>-e</b> (varme)
</td></tr>
<tr>
<th><a href="/wiki/Infinitive" title="Infinitive">Present tense infinitive</a>
</th>
<td><b>-ar</b> (irar)
</td>
<td>to be going
</td>
<td rowspan="3">to go
</td>
<td><b>-anti</b> (iranti)
</td>
<td rowspan="3"><b>-i</b> (iri)
</td></tr>
<tr>
<th><a href="/wiki/Infinitive" title="Infinitive">Past tense infinitive</a>
</th>
<td><b>-ir</b> (irir)
</td>
<td>to have gone
</td>
<td><b>-inti</b> (irinti)
</td></tr>
<tr>
<th><a href="/wiki/Infinitive" title="Infinitive">Future tense infinitive</a>
</th>
<td><b>-or</b> (iror)
</td>
<td>to be going to go
</td>
<td><b>-onti</b> (ironti)
</td></tr>
<tr>
<th><a href="/wiki/Present_tense" title="Present tense">Present</a>
</th>
<td><b>-as</b> (iras)
</td>
<td colspan="2">go, goes
</td>
<td colspan="2"><b>-as</b> (iras)
</td></tr>
<tr>
<th><a href="/wiki/Past_tense" title="Past tense">Past</a>
</th>
<td><b>-is</b> (iris)
</td>
<td colspan="2">went
</td>
<td colspan="2"><b>-is</b> (iris)
</td></tr>
<tr>
<th><a href="/wiki/Future_tense" title="Future tense">Future</a>
</th>
<td><b>-os</b> (iros)
</td>
<td colspan="2">will go
</td>
<td colspan="2"><b>-os</b> (iros)
</td></tr>
<tr>
<th><a href="/wiki/Imperative_mood" title="Imperative mood">Imperative</a>
</th>
<td><b>-ez</b> (irez)
</td>
<td colspan="2">go!
</td>
<td colspan="2"><b>-u</b> (iru)
</td></tr>
<tr>
<th><a href="/wiki/Conditional_mood" title="Conditional mood">Conditional</a>
</th>
<td><b>-us</b> (irus)
</td>
<td colspan="2">would go
</td>
<td colspan="2"><b>-us</b> (irus)
</td></tr></tbody></table>"""

chaine_3 = """<table class="wikitable" style="text-align:center">
<tbody><tr>
<th colspan="3" rowspan="3">
</th>
<th colspan="2">Relative and
<p>interrogative
</p>
</th>
<th colspan="2">Demonstrative
</th>
<th colspan="2">Indeterminate
</th>
<th>Most
<p>Indeterminate
</p>
</th>
<th colspan="2">Negative
</th>
<th colspan="2">Collective
</th></tr>
<tr>
<th>Esperanto
</th>
<th>Ido
</th>
<th>Esperanto
</th>
<th>Ido
</th>
<th>Esperanto
</th>
<th>Ido
</th>
<th>Ido
</th>
<th>Esperanto
</th>
<th>Ido
</th>
<th>Esperanto
</th>
<th>Ido
</th></tr>
<tr>
<th>ki-
</th>
<th>qua, ∅
</th>
<th>ti-
</th>
<th>ita, ∅
</th>
<th>i-
</th>
<th>ula, ∅
</th>
<th>irga
</th>
<th>neni-
</th>
<th>nula
</th>
<th>ĉi-
</th>
<th>omna
</th></tr>
<tr>
<th rowspan="2">Individual
</th>
<th>Esperanto
</th>
<th>-u
</th>
<td colspan="2">kiu
</td>
<td colspan="2">tiu
</td>
<td colspan="3">iu
</td>
<td colspan="2">neniu
</td>
<td colspan="2">ĉiu
</td></tr>
<tr>
<th>Ido
</th>
<th>-u
</th>
<td colspan="2" style="background: #fff1d8">qua
</td>
<td colspan="2" style="background: #fff1d8">ita
</td>
<td colspan="2">ulu
</td>
<td>irgu
</td>
<td colspan="2">nulu
</td>
<td colspan="2">omnu
</td></tr>
<tr>
<th rowspan="2">Thing
</th>
<th>Esperanto
</th>
<th>-o
</th>
<td colspan="2">kio
</td>
<td colspan="2">tio
</td>
<td colspan="3">io
</td>
<td colspan="2">nenio
</td>
<td colspan="2">ĉio
</td></tr>
<tr>
<th>Ido
</th>
<th>-o
</th>
<td colspan="2">quo
</td>
<td colspan="2">ito
</td>
<td colspan="2">ulo
</td>
<td>irgo
</td>
<td colspan="2">nulo
</td>
<td colspan="2">omno
</td></tr>
<tr>
<th rowspan="2">Plural
</th>
<th>Esperanto
</th>
<th>-j
</th>
<td colspan="2">kiuj/kioj
</td>
<td colspan="2">tiuj/tioj
</td>
<td colspan="3">iuj/ioj
</td>
<td colspan="2">neniuj/nenioj
</td>
<td colspan="2">ĉiuj/ĉioj
</td></tr>
<tr>
<th>Ido
</th>
<th>-i
</th>
<td colspan="2">qui
</td>
<td colspan="2">iti
</td>
<td colspan="2">uli
</td>
<td>irgi
</td>
<td colspan="2">nuli
</td>
<td colspan="2">omni
</td></tr>
<tr>
<th>Adjective
</th>
<th>Ido
</th>
<th>-a
</th>
<td colspan="2" style="background: #fff1d8">qua
</td>
<td colspan="2" style="background: #fff1d8">ita
</td>
<td colspan="2">ula
</td>
<td>irga
</td>
<td colspan="2">nula
</td>
<td colspan="2">omna
</td></tr>
<tr>
<th rowspan="2">Motive
</th>
<th>Esperanto
</th>
<th>-al
</th>
<td colspan="2">kial
</td>
<td colspan="2">tial
</td>
<td colspan="3">ial
</td>
<td colspan="2">nenial
</td>
<td colspan="2">ĉial
</td></tr>
<tr>
<th>Ido
</th>
<th>pro
</th>
<td colspan="2">pro quo
</td>
<td colspan="2">pro to
</td>
<td colspan="2">pro ulo
</td>
<td>pro irgo
</td>
<td colspan="2">pro nulo
</td>
<td colspan="2">pro omno
</td></tr>
<tr>
<th rowspan="2">Association
</th>
<th>Esperanto
</th>
<th>-es
</th>
<td colspan="2">kies
</td>
<td colspan="2">ties
</td>
<td colspan="2">ies
</td>
<td>
</td>
<td colspan="2">nenies
</td>
<td colspan="2">ĉies
</td></tr>
<tr>
<th>Ido
</th>
<th>di
</th>
<td colspan="2">di quo
</td>
<td colspan="2">di to
</td>
<td colspan="2">di ulo
</td>
<td>di irgo
</td>
<td colspan="2">di nulo
</td>
<td colspan="2">di omno
</td></tr>
<tr>
<th rowspan="2">Place
</th>
<th>Esperanto
</th>
<th>-e
</th>
<td colspan="2">kie
</td>
<td colspan="2">tie
</td>
<td colspan="3">ie
</td>
<td colspan="2">nenie
</td>
<td colspan="2">ĉie
</td></tr>
<tr>
<th>Ido
</th>
<th>loke
</th>
<td colspan="2" style="background: #ffd8d8">ube
</td>
<td colspan="2" style="background: #ffd8d8">ibe
</td>
<td colspan="2">ulaloke
</td>
<td>irgaloke
</td>
<td colspan="2">nulaloke
</td>
<td colspan="2">omnaloke
</td></tr>
<tr>
<th rowspan="2">Time
</th>
<th>Esperanto
</th>
<th>-am
</th>
<td colspan="2">kiam
</td>
<td colspan="2">tiam
</td>
<td colspan="3">iam
</td>
<td colspan="2">neniam
</td>
<td colspan="2">ĉiam
</td></tr>
<tr>
<th>Ido
</th>
<th>tempe
</th>
<td colspan="2" style="background: #ffd8d8">kande
</td>
<td colspan="2" style="background: #ffd8d8">lore
</td>
<td colspan="2">ulatempe
</td>
<td>irgatempe
</td>
<td colspan="2">nulatempe
</td>
<td colspan="2" style="background: #d8ffd8">omnatempe, sempre
</td></tr>
<tr>
<th rowspan="2">Quality
</th>
<th>Esperanto
</th>
<th>-a
</th>
<td colspan="2">kia
</td>
<td colspan="2">tia
</td>
<td colspan="3">ia
</td>
<td colspan="2">nenia
</td>
<td colspan="2">ĉia
</td></tr>
<tr>
<th>Ido
</th>
<th>-a, speca
</th>
<td colspan="2" style="background: #ffd8d8">quala
</td>
<td colspan="2" style="background: #ffd8d8">tala
</td>
<td colspan="2">ulaspeca
</td>
<td>irgaspeca
</td>
<td colspan="2">nulaspeca
</td>
<td colspan="2">omnaspeca
</td></tr>
<tr>
<th rowspan="2">Manner
</th>
<th>Esperanto
</th>
<th>-el
</th>
<td colspan="2">kiel
</td>
<td colspan="2">tiel
</td>
<td colspan="3">iel
</td>
<td colspan="2">neniel
</td>
<td colspan="2">ĉiel
</td></tr>
<tr>
<th>Ido
</th>
<th>-e, maniere
</th>
<td colspan="2" style="background: #ffd8d8">quale
</td>
<td colspan="2" style="background: #ffd8d8">tale
</td>
<td colspan="2">ule, ulamaniere
</td>
<td>irge, irgamaniere
</td>
<td colspan="2">nule, nulamaniere
</td>
<td colspan="2">omne, omnamaniere
</td></tr>
<tr>
<th rowspan="2">Quantity –
<p>adjective
</p>
</th>
<th>Esperanto
</th>
<th>-om
</th>
<td colspan="2">kiom
</td>
<td colspan="2">tiom
</td>
<td colspan="3">iom
</td>
<td colspan="2">neniom
</td>
<td colspan="2">ĉiom
</td></tr>
<tr>
<th>Ido
</th>
<th>quanta
</th>
<td colspan="2" style="background: #ffd8d8">quanta
</td>
<td colspan="2" style="background: #ffd8d8">tanta
</td>
<td colspan="2" style="background: #ffd8d8">kelka
</td>
<td>irgaquanta
</td>
<td colspan="2">nulaquanta
</td>
<td colspan="2">omnaquanta
</td></tr></tbody></table>"""

dict = {"Comparison_between_Esperanto_and_Ido":[chaine,chaine_2,chaine_3]}


def convert_to_csv(tables):
    for table_key, table_value in tables.items():
        list_of_tables = table_value
        for value in list_of_tables:
            table = value
            dataframe = pd.read_html(table,header=0)
            nb_table = 1
            for table_df in dataframe:
                table_df.to_csv('output/'+table_key+"_"+str(nb_table)+".csv",index=False)
                nb_table += 1



convert_to_csv(dict)

