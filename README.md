## Datoteke
* `python single_words.py` - Vrne dve datoteki lematiziranega besedila podanega korpusa. Ena vsebuje piko na koncu povedi, druga ne. Kot argumenta prejme željeno ime podatkovne množice in datoteko kjer se korpus nahaja 
* `python get_VID_prunes.py` - Vrne datoteko, ki vsebuje primere primere neprekinjenih VID iz korpusa PARSEME.
* `group_words_advanced.py` - Vrne datoteko, ki vsebuje lematizirano besedilo v katerem so besede združene v skupine. Kot argument prejme ime podatkovne množice.
* `get_VIDs_and_OTHRs.py` - Vrne datoteko, ki vsebuje izbrane vektorje, ki bodo dodani v podatkovno množico. Kot argument prejme ime podatkovne množice.
* `calculate_csv.py` - Za izbrane vektorje izračuna značilke in vrne datoteko, ki vsebuje podatkovno množico. Kot argument prejme ime podatkovne množice.
* `analyze_dataset.py` - Izračuna povprečno število besed v skupini v podatkovni množici. Kot argument prejme ime podatkovne množice.
* `learning_plotdata.py` - Izriše korelacijsko matriko podatkovne množice. Kot argument prejme ime podatkovne množice.
* `learning_evaluate.py` - Evalvira uspešnost metode podpornih vektorjev, naključnih gozdov in logistične regresije. Vrne tudi ocene pomembnosti atribuv, ki jih lahko pridobimo z metodama naključnih gozdov in logistične regresije. Kot argument prejme ime podatkovne množice.
* Mapa `datasets` vsebuje podatkovni množici uporabljeni pri diplomski nalogi, mapa `vectors` pa pripadajoče vektorje.



### Primer uporabe za ccGigafida
1. Iz [CLARIN.SI](https://www.clarin.si/repository/xmlui/handle/11356/1035) prenesemo datoteko `ccGigafidaV1_0.zip` ter jo razsirimo v `ccGigafidaV1_0`.
2. Iz [LINDAT/CLARIN](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2842) prenesemo datoteko `SL.tgz` ter jo razsirimo v `SL`.
3. Zaženemo `python single_words.py ccgigafida ccGigafidaV1_0`.
4. Zaženemo `python get_VID_prunes.py`.
5. Zaženemo `python group_words_advanced.py ccgigafida`.
6. Zaženemo `fasttext skipgram -input data/ccgigafida_grouped_VIDs.txt -output vectors/ccgigafida_grouped_VIDs`.
7. Zaženemo `fasttext skipgram -input data/ccgigafida_single_concat.txt -output vectors/ccgigafida_single_concat`.
8. Zaženemo `python get_VIDs_and_OTHRs.py ccgigafida`.
9. Če želimo uravnotežimo dolžine skupin v OTHRs.vec, v pomoč je `analyze_dataset.py`
10. Zaženemo `python calculate_csv.py ccgigafida`.
11. Zaženemo `python learning_plotdata.py ccgigafida`.
12. Zaženemo `python learning_evaluate.py ccgigafida`.
