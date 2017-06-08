# Determining-Political-Orientation-Croatian


# Determining-Political-Orientation-Croatian


	Za ovaj seminar radio sam program za određivanje političke orijentacije autora komentara.
Program sam izrađivao u programskom jeziku Python.
Prvi korak je bio prikupljanje komentara s Facebook stranice Index.hr. Za potrebe toga
koristio sam skriptu koja je skidala zadnjih 1000 postova sa stranice, a zatim drugu skriptu koja je skidala sve komentare s tih postova. Tako sam dobio oko 27000 komentara. Komentare sam
filtrirao po broju lajkova te sam uzeo samo komentare s 5 ili više lajkova. Razlog tome je što mnogi komentari su „smeće“ jer većina komentara danas je kada netko označi nekog u komentaru ili
ostave samo emotikon. Nakon filtriranja dobio sam oko 2500 komentara, te sam uzeo prvih 2000
komentara po broju lajkova za daljnju obradu.

	Nakon toga sam krenuo ručno označavati 2000 komentara. Komentare sam označavao u tri
klase, lijeva, neutralna i desna. Ovaj korak je bio vremenski zahtjevniji i najmonotoniji, ali od
ključne važnosti je da se komentari ispravno označe da bi se dogodio šum u podatcima (šum je
nepravilno označavanje podataka zbog čega model radi neprecizno).
	
	Idući korak je pripremanje podataka za obradu, ali da bi ispravno pripremio podatke morao
sam odlučiti koji du model koristiti. Odlučio sam se za stroj potpornih vektora. Dakle, morao sam
transformirati komentare u vektore. To sam uradio pomoću Word2vec modela. Taj model, koji je
razvio Google, iznimno je koristan u obradbi prirodnog jezika. On omogućava da svaku riječ
prikažemo pomoću 300-dimenzionalnog normiranog vektora. Taj vektor je unikatan za svaku riječ
te se u njemu ne gubi značenje riječi. Riječi koje su slične po značenju imat će veliku kosinusnu
sličnost između pripadajućih vektora. Algoritam kako dobiti vektor iz riječi je izvan domene ovog
seminara te ga neću ovdje objašnjavati. TakeLab mi je ustupio Word2vec fileove za hrvatski jezik
koji sadrži oko 930000 riječi hrvatskog jezika. Vektor komentara se jednostavno dobije tako da se
zbroje vektori riječi unutar komentara te se zatim normiranjem dobivenog vektora. 

	Greška bi bila kada bih odmah krenuo vektorizirati riječ po riječ iz komentara. Hrvatski jezik
je specifičan po tome što sadrži promjenjive i nepromjenjive riječi. Važno je prvo korjenovati svaku riječ te izbaciti sve nepromjenjive riječi. Riječi se korjenuju jer npr. riječi „država“ i „državi“ imaju isto značenje, a nepromjenjive riječi se izbacuju jer su to riječi bez značenja. Za korjenovanje riječi sam koristio Python skriptu „Croatian stemmer“ koji su izradili Nikola Ljubešić i Ivan Pandžić s Filozofskog fakulteta.

	Nakon što sam korjenovao komentare, krenuo sam radio vektorizaciju. Ovdje sam naišao
na prvi veći problem. Datoteka sa svim vektorima hrvatskog jezika je ogromna (2.7 GB) te treba 
jako puno vremena dok se ona obradi i učita u Python Dictionary. Da ne bi morao svaki put
prilikom pokretanja programa stvarati novi dictionary, koristio sam „pickleziranje“, odnosno
spremanje objekata u datoteku te ih kasnije učitavanje iz datoteke. NAPOMENA: Da bi program radio potrebno je skinuti Vector_dict.txt (pickleziranu verziju dictionarya i staviti u korijenski direktorij. Vector_dict.txt se može skinuti sa: dropb) Nakon što sam napokon vektorizirao komentare i spremio ih u datoteku, mogao sam krenuti s učenjem modela.
Za učenje modela i svu potrebnu logiku strojnog učenja koristio sam biblioteku „sklearn“.
Komentare sam učitao u matricu dimenzije 2000x300, a vrijednosti klasa u transponirani vektor
dimenzije 300. Zatim sam podijelio komentare na train i test split. Nakon prvog učenja modela,
testirao sam modela na test splitu te dobio rezultat od 44 %. Ukupno u svojim komentarima imam
oko 800 komentara neutralne orijentacije, oko 600 komentara lijeve orijentacije te oko 600
komentara desne orijentacije. Kada bih sve komentare proglasio da su neutralni, točnost bi mi bila
oko 40 %, što je značilo da moj početni model radi bolje od toga za 4%.

	Zatim sam krenuo u dijagnostiku i ispravljanje modela. Koristio sam GridSearchCV klasu iz
sklearn biblioteke za optimiranje parametara. Nakon što sam optimirao parametre dobio sam
točnost od 55 %. Smatram da s prilično jednostavnom logikom programa koji evaluira komentare
prema samo značenju riječi kojih sadrži ne mogu dobiti mnogo bolju točnost jer ipak detekcija
stava je složen problem koji zahtjeva kompliciranije modele od ovog kojeg sam ja koristio.
Nakon što sam dobio model, ugradio sam ga u svoj program koji čita od korisnika komentar
te uz pomoć modela određuje koje je političke orijentacije autor komentara.