# Serbian Parliamentary NLP Analysis

This project explores political discourse in Serbia using transcripts from National Assembly sessions. It extracts, structures, and analyzes data to enhance transparency and civic understanding.

## 🔍 Project Goals
- Analyze who speaks the most and how
- Detect recurring topics and patterns
- Build a foundation for AI tools that inform citizens about parliamentary behavior

## Structure
- `data/`: Sample of structured speech data (not the full set, due to size/privacy)
- `notebooks/`: Interactive Jupyter Notebooks for analysis
- `scripts/`: Parser that converts raw .txt to structured JSON
- `requirements.txt`: Dependencies

## Sample Output
- Topic models, word clouds, and speaker statistics
- Sentiment trends (WIP)
- Metadata-enriched political discourse

## Top Speakers

| RANK | SPEAKER              | NUM OF SPEECHES | PARTY                 | Note           |
| ---- | -------------------- | --------------- | --------------------- | -------------- |
| 1    | ANA BRNABIĆ          | 1762            | SNS                   | PREDSEDAVAJUĆA |
| 2    | SNEŽANA PAUNOVIĆ     | 623             | SPS                   | PREDSEDAVAJUĆA |
| 3    | MARINA RAGUŠ         | 454             | SNS                   | PREDSEDAVAJUĆA |
| 4    | MILENKO JOVANOV      | 328             | SNS                   |                |
| 5    | ALEKSANDAR JOVANOVIĆ | 268             | Narodni pokret Srbije |                |
| 6    | STOJAN RADENOVIĆ     | 258             | SNS                   |                |
| 7    | RADOMIR LAZOVIĆ      | 125             | ZLF                   |                |
| 8    | SRĐAN MILIVOJEVIĆ    | 106             | DS                    |                |
| 9    | MILOŠ PARANDILOVIĆ   | 95              | NLS                   |                |
| 10   | ZORAN LUTOVAC        | 90              | DS                    |                |
| 11   | MARINIKA TEPIĆ       | 86              | SSP                   |                |
| 12   | MILOŠ VUČEVIĆ        | 79              | SNS                   | PRIME MINISTER |
| 13   | BORISLAV NOVAKOVIĆ   | 77              | Narodni pokret Srbije |                |
| 14   | DANIJELA NESTOROVIĆ  | 74              | Narodni pokret Srbije |                |
| 15   | ELVIRA KOVAČ         | 57              | SVM-VMSZ              | PREDSEDAVAJUĆA |

## Speech length (No of characters)
| RANK | SPEAKER                     | SPEECH LEN (CHAR) | PARTY                 | Note           |
| ---- | --------------------------- | ----------------- | --------------------- | -------------- |
| 1    | ANA BRNABIĆ                 | 799335            | SNS                   | PREDSEDAVAJUĆA |
| 2    | MILENKO JOVANOV             | 696929            | SNS                   |                |
| 3    | MILOŠ VUČEVIĆ               | 482097            | SNS                   | PRIME MINISTER |
| 4    | SNEŽANA PAUNOVIĆ            | 470949            | SPS                   | PREDSEDAVAJUĆA |
| 5    | DANIJELA NESTOROVIĆ         | 283581            | Narodni pokret Srbije |                |
| 6    | DUBRAVKA ĐEDOVIĆ HANDANOVIĆ | 262915            | SNS                   | MINISTER       |
| 7    | ALEKSANDAR MARTINOVIĆ       | 218080            | SNS                   | MINISTER       |
| 8    | SINIŠA MALI                 | 213075            | SNS                   |                |
| 9    | ŽIVOTA STARČEVIĆ            | 151432            | JS                    |                |
| 10   | MARINA RAGUŠ                | 146521            | SNS                   | PREDSEDAVAJUĆA |
| 11   | ALEKSANDAR JOVANOVIĆ        | 144590            | Narodni pokret Srbije |                |
| 12   | MIROSLAV ALEKSIĆ            | 141545            | Narodni pokret Srbije |                |
| 13   | RADOMIR LAZOVIĆ             | 138195            | ZLF                   |                |
| 14   | MARIJAN RISTIČEVIĆ          | 133678            | SNS                   |                |
| 15   | ALEKSANDAR VULIN            | 133602            | PS                    | MINISTER       |

## Topics

| Topic # | Top Words                                                                | Probable Theme                              | Interpretation                                                                                                           |
| ------- | ------------------------------------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **0**   | zakon, godina, srbija, imati, hteti, ministarstvo, obrazovanje, građanin | **Public Policy & Legislation**             | General discussion of laws, government ministries, and citizens’ rights, likely around national policy or legal reforms. |
| **1**   | litijum, rudnik, tinto, sredina, zakon, projekt                          | **Environmental Concerns & Lithium Mining** | Focused on Rio Tinto, lithium mining, and its impact on the environment and legislation.                                 |
| **2**   | srbija, republika, razvoj, država, zemlja                                | **National Development & Strategy**         | Talk of Serbia’s development, government, and national identity. High-level political or economic strategy themes.       |
| **3**   | hteti, čovek, imati, kazati, vlada, govoriti                             | **Political Rhetoric & Governance**         | Speeches reflecting personal appeals, leadership intentions, and critiques of governance.                                |
| **4**   | porođaj, porodiljski, bolovanje, trudan                                  | **Maternal & Family Policy**                | Centered around maternity, childbirth, and family leave policies. Likely from social/health policy discussions.          |
| **5**   | imati, hvati, izvoliti, narodni, poslanik                                | **Parliamentary Procedure & Formalities**   | Language typical in formal sessions — calling on MPs, presence, and formal phrases. Possibly procedural or ironic.       |
| **6**   | privoditi, kraj, isteklo, reklamiranje, potpredsednica                   | **Session Closure & Miscellaneous**         | A mixed set likely from session endings, odd terms, and possibly sarcastic or humorous remarks.                          |
| **7**   | godina, evro, milion, milijarda                                          | **Budget & Economy**                        | Financial discussion — budget, expenditures, and national economic outlook.                                              |
| **8**   | narodni, poslanik, amandman, glasanje, zakon                             | **Legislative Process & Amendments**        | Focused on voting, proposing laws, and parliamentary decision-making. Core legislative procedures.                       |
| **9**   | poslovnik, replika, vreme, kazati                                        | **Debate Rules & Floor Management**         | Deals with speaking time, requests, and adherence to parliamentary rulebook — classic floor debate content.              |
