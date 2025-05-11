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
