<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Domaći zadatak - Algoritmi i strukture podataka</h1>
    <h2>Zadatak nosi 10 poena</h2>
    <p>Domaći zadatak se sastoji iz tri dela:</p>
    <ol>
        <li>
            <h3>(6 poena) Napisati Python3 program koji prevodi zapis iz infiksnog oblika u postfiksni.</h3>
            <p>Obratite pažnju na pravilnu upotrebu zagrada. Podržati upotrebu višecifrenih i razlomljenih brojeva, kao i operatora +, -, *, /, ^ (stepenovanje).</p>
            <p>U implementaciji, dozvoljeno je koristiti modul tokenizer.py (koji pomaže u razdvajanje ulaznog izraza na tokene). Dobijeni tokenizer ne pokriva sve slučajeve koje zadatak treba da podrži tako da je poželjno dopuniti ovaj modul.</p>
            <p>Obezbediti reakciju na različite tipove grešaka kroz konkretne, samostalno kreirane naslednice klase Exception.</p>
            <p>Primeri:</p>
            <ul>
                <li>6.11 – 74 * 2 se prevodi u 6.11 74 2 * -</li>
                <li>(24 – 7) ^ (3.2 + (-7)) se prevodi u 24 7 – 3.2 -7 + ^</li>
                <li>-20 * 7.9 / (3 – 7) se prevodi u -20 7.9 * 3 7 - /</li>
                <li>-20 * .9 / (3 – 7) se prevodi u -20 .9 * 3 7 - /</li>
            </ul>
        </li>
        <li>
            <h3>(3 poena) Napisati Python3 program koji izračunava ukupnu vrednost izraza u postfiksnoj notaciji.</h3>
            <p>Kao i u prvom zadatku, potrebno je podržati upotrebu višecifrenih i razlomljenih brojeva, kao i operatora +, -, *, /, ^ (stepenovanje).</p>
            <p>Primeri:</p>
            <ul>
                <li>6.11 74 2 * - se izračunava u -141.89</li>
                <li>24 7 – 3.2 2 - ^ se izračunava u 29.9597859131</li>
                <li>20 7.9 * 3 7 - / se izračunava u -39.5</li>
            </ul>
        </li>
        <li>
            <h3>(1 poen) Integrisati prvi i drugi zadatak tako da podržavaju izračunavanje infiksnih izraza.</h3>
        </li>
    </ol>
</body>
</html>
