Downloading dataset: 240368it [00:10, 23592.25it/s]
Extracted files: ['train.json', 'dev.json', 'test.json']
Sample record: {'_id': '8813f87c0bdd11eba7f7acde48001122', 'type': 'compositional', 'question': 'Who is the mother of the director of film Polish-Russian War (Film)?', 'context': [['Maheen Khan', ['Maheen Khan is a Pakistani fashion and costume designer, also an award winner fashion designer for fashion labels like" The Embroidery HouseMaheen" and" Gulabo".', 'She has done many national and international fashion events and shows.', 'She undertook embroidery for the film Snow White and the Huntsman and television series', 'The Jewel in the Crown.']], ['Viktor Yeliseyev', ['Viktor Petrovich Yeliseyev( born June 9, 1950) is a Russian general, orchestra conductor and music teacher.', 'He is the director of the Ministry of the Interior Ensemble, one of the two Russian Red Army Choirs.']], ['Alice Washburn', ['Alice Washburn( 1860- 1929) was an American stage and film actress.', 'She worked at the Edison, Vitagraph and Kalem studios.', 'Her final film Snow White was her only known feature film.', 'She died of heart attack in November 1929.']], ['Minamoto no Chikako', ['She was the mother of Prince Morinaga.']], ['Polish-Russian War (film)', ['Polish-Russian War', '(Wojna polsko-ruska) is a 2009 Polish film directed by Xawery Żuławski based on the novel Polish-Russian War under the white-red flag by Dorota Masłowska.']], ['A Snow White Christmas', ['A Snow White Christmas is a Christmas animated television special produced by Filmation and telecast December 19, 1980, on CBS.', 'It is a sequel to the fairy tale" Snow White", unrelated to Filmation\'s other sequel to" Snow White" titled" Happily Ever After"( 1990).', "The film's plot revolves around the return of the Wicked Queen, who is unexpectedly brought back to life during Christmas and casts an evil spell that freezes the entire land.", 'Only the young Snow White, the daughter of the original Snow White, manages to escape and take refuge with the seven giants with her dwarf friend.', 'It is now up to the giants to defeat the Queen forever and save the kingdom.']], ['Snow White and the Three Stooges', ['Snow White and the Three Stooges is the second feature film to star the Three Stooges after their 1959 resurgence in popularity.', 'By this time, the trio consisted of Moe Howard, Larry Fine, and Joe DeRita( dubbed" Curly Joe").', 'Released by 20th Century Fox, this was the trio\'s take on the classic fairy tale" Snow White and the Seven Dwarfs".', 'The film was retitled Snow White and the Three Clowns in Great Britain.', 'This was Walter Lang ‘s final directing film before his retirement.', 'Olympic gold medalist figure skater Carol Heiss starred as Snow White, who must flee her home after The Evil Queen, her evil stepmother, wishes her to be dead.', 'Seeking refuge in the cottage of the seven dwarfs, she accidentally meets the Stooges, who are house sitting for them while they are away.']], ['Xawery Żuławski', ['Xawery Żuławski (born 22 December 1971 in Warsaw) is a Polish film director.', 'In 1995 he graduated National Film School in Łódź.', 'He is the son of actress Małgorzata Braunek and director Andrzej Żuławski.', 'His second feature "Wojna polsko-ruska" (2009), adapted from the controversial best-selling novel by Dorota Masłowska, won First Prize in the New Polish Films competition at the 9th Era New Horizons Film Festival in Wrocław.', 'In 2013, he stated he intends to direct a Polish novel "Zły" by Leopold Tyrmand.', 'Żuławski and his wife Maria Strzelecka had 2 children together:', 'son Kaj Żuławski (born 2002) and daughter Jagna Żuławska (born 2009).']], ['Snow White and the Seven Dwarfs (1955 film)', ['Snow White and the Seven Dwarfs( USA:" Snow White") is a 1955 German film, directed by Erich Kobler, based on the story of Schneewittchen by the Brothers Grimm.']], ['Liberty Ross', ['Liberty Lettice Lark Ross( born 23 September 1978) is an English model and actress.', 'She has appeared in publications such as" VogueHarper\'s Bazaari- D", and" Dazed& Confused".', 'She played the role of Queen Eleanor in the 2012 fantasy film" Snow White and the Huntsman", directed by her then- husband, Rupert Sanders.', 'She is the sister of composers Atticus and Leopold Ross.']]], 'supporting_facts': [['Polish-Russian War (film)', 1], ['Xawery Żuławski', 2]], 'evidences': [['Polish-Russian War', 'director', 'Xawery Żuławski'], ['Xawery Żuławski', 'mother', 'Małgorzata Braunek']], 'answer': 'Małgorzata Braunek'}
/usr/local/lib/python3.11/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: 
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
  warnings.warn(
tokenizer_config.json: 100%
 79.0/79.0 [00:00<00:00, 3.91kB/s]
config.json: 100%
 571/571 [00:00<00:00, 33.9kB/s]
vocab.json: 100%
 899k/899k [00:00<00:00, 3.58MB/s]
merges.txt: 100%
 456k/456k [00:00<00:00, 2.74MB/s]
special_tokens_map.json: 100%
 772/772 [00:00<00:00, 51.8kB/s]
model.safetensors: 100%
 496M/496M [00:02<00:00, 230MB/s]
Device set to use cpu
Evaluating Model:   0%|          | 0/50 [00:00<?, ?it/s]/usr/local/lib/python3.11/dist-packages/transformers/pipelines/question_answering.py:391: FutureWarning: Passing a list of SQuAD examples to the pipeline is deprecated and will be removed in v5. Inputs should be passed using the `question` and `context` keyword arguments instead.
  warnings.warn(
Evaluating Model:   2%|▏         | 1/50 [00:06<05:17,  6.48s/it]Q: Who is the mother of the director of film Polish-Russian War (Film)?
Pred: Dorota Masłowska
GT: ['Małgorzata Braunek']
EM: 0, F1: 0.0000

Evaluating Model:   4%|▍         | 2/50 [00:12<05:06,  6.39s/it]Q: Which film came out first, Blind Shaft or The Mask Of Fu Manchu?
Pred: The Mask of Fu Manchu
GT: ['The Mask Of Fu Manchu']
EM: 1, F1: 1.0000

Evaluating Model:   6%|▌         | 3/50 [00:20<05:17,  6.76s/it]Q: When did John V, Prince Of Anhalt-Zerbst's father die?
Pred: 4 February 1551
GT: ['12 June 1516']
EM: 0, F1: 0.0000

Evaluating Model:   8%|▊         | 4/50 [00:23<04:18,  5.63s/it]Q: What is the award that the director of film Wearing Velvet Slippers Under A Golden Umbrella won?
Pred: Myanmar Motion Picture Academy Awards
GT: ['Myanmar Motion Picture Academy Awards']
EM: 1, F1: 1.0000

Evaluating Model:  10%|█         | 5/50 [00:32<05:00,  6.67s/it]Q: Where was the director of film Ronnie Rocket born?
Pred: Missoula, Montana
GT: ['Missoula, Montana']
EM: 1, F1: 1.0000

Evaluating Model:  12%|█▏        | 6/50 [00:43<06:00,  8.18s/it]Q: Who is Charles Bretagne Marie De La Trémoille's paternal grandfather?
Pred: Louis de La Trémoille
GT: ['Charles Armand René de La Trémoille']
EM: 0, F1: 0.6000

Evaluating Model:  14%|█▍        | 7/50 [00:52<06:07,  8.54s/it]Q: Where was the father of Ștefan I. Nenițescu born?
Pred: Bucharest
GT: ['Galați']
EM: 0, F1: 0.0000

Evaluating Model:  16%|█▌        | 8/50 [00:58<05:27,  7.79s/it]Q: Are North Marion High School (Oregon) and Seoul High School both located in the same country?
Pred: all four schools being located on the same campus
GT: ['no']
EM: 0, F1: 0.0000

Evaluating Model:  18%|█▊        | 9/50 [01:04<04:43,  6.92s/it]Q: Which film has the director who was born later, El Extraño Viaje or Love In Pawn?
Pred: 1964 Spanish black drama film
GT: ['El Extraño Viaje']
EM: 0, F1: 0.0000

Evaluating Model:  20%|██        | 10/50 [01:10<04:29,  6.74s/it]Q: Who is the maternal grandfather of Antiochus X Eusebes?
Pred: Guillaume Wittouck
GT: ['Ptolemy IX Lathyros']
EM: 0, F1: 0.0000

Evaluating Model:  22%|██▏       | 11/50 [01:15<04:03,  6.23s/it]Q: Which film has the director died first, Crimen A Las Tres or The Working Class Goes To Heaven?
Pred: 1935
GT: ['The Working Class Goes To Heaven']
EM: 0, F1: 0.0000

Evaluating Model:  24%|██▍       | 12/50 [01:17<03:12,  5.06s/it]Q: Which film has the director born first, Once A Gentleman or The Girl In White?
Pred: The Girl in White
GT: ['Once A Gentleman']
EM: 0, F1: 0.0000

Evaluating Model:  26%|██▌       | 13/50 [01:25<03:34,  5.81s/it]Q: Which film has the director who died earlier, Il Seduttore or The Trial Of Joan Of Arc?
Pred: The Trial of Joan of Arc
GT: ['The Trial Of Joan Of Arc']
EM: 1, F1: 0.8000

Evaluating Model:  28%|██▊       | 14/50 [01:27<02:51,  4.76s/it]Q: Where was the director of film Thomas Jefferson (Film) born?
Pred: Brazilian
GT: ['Brooklyn']
EM: 0, F1: 0.0000

Evaluating Model:  30%|███       | 15/50 [01:40<04:13,  7.24s/it]Q: Why did Grand Duke Kirill Vladimirovich Of Russia's wife die?
Pred: suffering a stroke
GT: ['stroke']
EM: 0, F1: 0.6667

Evaluating Model:  32%|███▏      | 16/50 [01:44<03:31,  6.23s/it]Q: Where was the place of death of the director of film Beat Girl?
Pred: Nice
GT: ['Nice']
EM: 1, F1: 1.0000

Evaluating Model:  34%|███▍      | 17/50 [01:52<03:46,  6.86s/it]Q: Who died first, Fleetwood Sheppard or George William Whitaker?
Pred: Fleetwood Sheppard
GT: ['Fleetwood Sheppard']
EM: 1, F1: 1.0000

Evaluating Model:  36%|███▌      | 18/50 [01:56<03:10,  5.97s/it]Q: Which film has the director born first, The Raven'S Dance or Keïta! L'Héritage Du Griot?
Pred: The Raven's Dance
GT: ["The Raven'S Dance"]
EM: 1, F1: 1.0000

Evaluating Model:  38%|███▊      | 19/50 [02:01<02:53,  5.59s/it]Q: When did Jean Martin (Singer)'s husband die?
Pred: –2004
GT: ['1983']
EM: 0, F1: 0.0000

Evaluating Model:  40%|████      | 20/50 [02:05<02:31,  5.04s/it]Q: Which film has the director who died earlier, Tangled Destinies or The Daltons' Women?
Pred: The Daltons' Women
GT: ['Tangled Destinies']
EM: 0, F1: 0.0000

Evaluating Model:  42%|████▏     | 21/50 [02:08<02:13,  4.60s/it]Q: Which film was released earlier, Moment Of Danger or The Ballad Of Josie?
Pred: The Ballad of Little Jo
GT: ['Moment Of Danger']
EM: 0, F1: 0.2857

Evaluating Model:  44%|████▍     | 22/50 [02:13<02:12,  4.72s/it]Q: What nationality is the director of film World And Time Enough?
Pred: gay
GT: ['United States']
EM: 0, F1: 0.0000

Evaluating Model:  46%|████▌     | 23/50 [02:18<02:10,  4.84s/it]Q: Which film has the director died earlier, Poker In Bed or The Machine To Kill Bad People?
Pred: Querelle
GT: ['The Machine To Kill Bad People']
EM: 0, F1: 0.0000

Evaluating Model:  48%|████▊     | 24/50 [02:24<02:12,  5.09s/it]Q: Which film whose director is younger, Heads I Win, Tails You Lose or The Incredible Sarah?
Pred: Christopher Cantwell
GT: ['Heads I Win, Tails You Lose']
EM: 0, F1: 0.0000

Evaluating Model:  50%|█████     | 25/50 [02:30<02:10,  5.20s/it]Q: Who is Catherine Of Pomerania, Countess Palatine Of Neumarkt's father-in-law?
Pred: Christian I
GT: ['Rupert']
EM: 0, F1: 0.0000

Evaluating Model:  52%|█████▏    | 26/50 [02:34<01:56,  4.84s/it]Q: Who is Marie Zéphyrine Of France's paternal grandmother?
Pred: Louis, Dauphin of France
GT: ['Marie Leszczyńska']
EM: 0, F1: 0.0000

Evaluating Model:  54%|█████▍    | 27/50 [02:38<01:51,  4.86s/it]Q: Which film has the director died earlier, Condemned Women or Faces In The Dark?
Pred: Faces in the Dark
GT: ['Condemned Women']
EM: 0, F1: 0.0000

Evaluating Model:  56%|█████▌    | 28/50 [02:42<01:36,  4.38s/it]Q: Who is the spouse of the director of film Eden And After?
Pred: Alain Robbe-Grillet
GT: ['Catherine Robbe-Grillet']
EM: 0, F1: 0.5000

Evaluating Model:  58%|█████▊    | 29/50 [02:50<01:54,  5.47s/it]Q: Where was the place of death of Anastasia Of Serbia's husband?
Pred: 16 October 1962
GT: ['Hilandar']
EM: 0, F1: 0.0000

Evaluating Model:  60%|██████    | 30/50 [02:51<01:27,  4.35s/it]Q: Are Fire In Hell and The Tiger: An Old Hunter'S Tale from the same country?
Pred: South Korean
GT: ['yes']
EM: 0, F1: 0.0000

Evaluating Model:  62%|██████▏   | 31/50 [02:54<01:10,  3.70s/it]Q: Which film was released more recently, Lo Zappatore or Placer Sangriento?
Pred: Lo Zappatore
GT: ['Placer Sangriento']
EM: 0, F1: 0.0000

Evaluating Model:  64%|██████▍   | 32/50 [02:59<01:15,  4.20s/it]Q: Was Şemsettin Baş or Gwenc'Hlan Le Scouëzec born first?
Pred: South African
GT: ["Gwenc'Hlan Le Scouëzec"]
EM: 0, F1: 0.0000

Evaluating Model:  66%|██████▌   | 33/50 [03:06<01:26,  5.10s/it]Q: Which film has the director born later, Bhoomiyude Avakashikal or The Majesty Of The Law?
Pred: The Inheritors of the Earth
GT: ['Bhoomiyude Avakashikal']
EM: 0, F1: 0.0000

Evaluating Model:  68%|██████▊   | 34/50 [03:09<01:12,  4.55s/it]Q: Who is Cornelia (Wife Of Caesar)'s child-in-law?
Pred: Julia
GT: ['Pompey']
EM: 0, F1: 0.0000

Evaluating Model:  70%|███████   | 35/50 [03:15<01:11,  4.74s/it]Q: Why did John Middleton Murry's wife die?
Pred: extrapulmonary tuberculosis
GT: ['tuberculosis']
EM: 0, F1: 0.6667

Evaluating Model:  72%|███████▏  | 36/50 [03:30<01:48,  7.78s/it]Q: Who is the paternal grandfather of Taj Al-Dawla?
Pred: Ja'far ibn Fallah
GT: ['Rukn al-Dawla']
EM: 0, F1: 0.0000

Evaluating Model:  74%|███████▍  | 37/50 [03:34<01:29,  6.86s/it]Q: Do both films Payment On Demand and My Cousin From Warsaw have the directors from the same country?
Pred: German
GT: ['yes']
EM: 0, F1: 0.0000

Evaluating Model:  76%|███████▌  | 38/50 [03:36<01:04,  5.39s/it]Q: What is the place of birth of the director of film And The Spring Comes?
Pred: Xi'an, Shaanxi
GT: ["Xi'an"]
EM: 0, F1: 0.6667

Evaluating Model:  78%|███████▊  | 39/50 [03:39<00:49,  4.49s/it]Q: Who died first, Madame Pasca or James A. Donohoe?
Pred: May 25, 1914
GT: ['Madame Pasca']
EM: 0, F1: 0.0000

Evaluating Model:  80%|████████  | 40/50 [03:45<00:49,  4.93s/it]Q: Who was born later, D'Arcy Coulson or Thomas William Adams?
Pred: D'Arcy Coulson
GT: ["D'Arcy Coulson"]
EM: 1, F1: 1.0000

Evaluating Model:  82%|████████▏ | 41/50 [03:49<00:44,  4.91s/it]Q: Are Simonds Catholic College and Saginaw High School (Texas) both located in the same country?
Pred: Saginaw, Texas, United States
GT: ['no']
EM: 0, F1: 0.0000

Evaluating Model:  84%|████████▍ | 42/50 [03:55<00:41,  5.20s/it]Q: Which country Prince Nikolaus Wilhelm Of Nassau's mother is from?
Pred: Württemberg
GT: ['German']
EM: 0, F1: 0.0000

Evaluating Model:  86%|████████▌ | 43/50 [03:58<00:30,  4.42s/it]Q: Which film whose director was born first, 45 Fathers or The Intended?
Pred: The Intended
GT: ['45 Fathers']
EM: 0, F1: 0.0000

Evaluating Model:  88%|████████▊ | 44/50 [04:03<00:27,  4.59s/it]Q: Who is the paternal grandfather of Alexandre Berthier, 3Rd Prince Of Wagram?
Pred: Louis Alexandre Berthier
GT: ['Louis-Alexandre Berthier']
EM: 0, F1: 0.4000

Evaluating Model:  90%|█████████ | 45/50 [04:06<00:20,  4.03s/it]Q: Where was the husband of Caterina Visconti born?
Pred: Milan
GT: ['Pavia']
EM: 0, F1: 0.0000

Evaluating Model:  92%|█████████▏| 46/50 [04:09<00:15,  3.87s/it]Q: Which film has the director who was born later, A Quiet Place In The Country or When Were You Born?
Pred: 1968
GT: ['A Quiet Place In The Country']
EM: 0, F1: 0.0000

Evaluating Model:  94%|█████████▍| 47/50 [04:13<00:11,  3.90s/it]Q: Who was born first, John Beach or Gordon Persons?
Pred: Nelson J. Beach
GT: ['John Beach']
EM: 0, F1: 0.4000

Evaluating Model:  96%|█████████▌| 48/50 [04:20<00:09,  4.85s/it]Q: Which film has the director born earlier, The House By The Cemetery or Charlie Chan In Honolulu?
Pred: Charlie Chan
GT: ['Charlie Chan In Honolulu']
EM: 0, F1: 0.6667

Evaluating Model:  98%|█████████▊| 49/50 [04:22<00:04,  4.07s/it]Q: Who is the child of the director of film La Leona (Film)?
Pred: Víctor Bó
GT: ['Víctor Bó']
EM: 1, F1: 1.0000

Evaluating Model: 100%|██████████| 50/50 [04:26<00:00,  5.33s/it]Q: Who is Blanche Of Portugal (1259–1321)'s paternal grandmother?
Pred: King Afonso III of Portugal
GT: ['Urraca of Castile']
EM: 0, F1: 0.2500

Final EM Score: 18
Final F1 Score: 27.8

