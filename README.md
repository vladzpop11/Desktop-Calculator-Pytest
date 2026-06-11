{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Bold;\f1\fswiss\fcharset0 Helvetica;\f2\fnil\fcharset0 AppleColorEmoji;
\f3\froman\fcharset0 Times-Roman;\f4\fswiss\fcharset0 Helvetica-Bold;\f5\fmodern\fcharset0 Courier;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid201\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid3}
{\list\listtemplateid4\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid301\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid4}
{\list\listtemplateid5\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat2\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid401\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid5}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}{\listoverride\listid4\listoverridecount0\ls4}{\listoverride\listid5\listoverridecount0\ls5}}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh15100\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Python Desktop Calculator & Pytest Automation Suite
\f1\b0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \

\f2 \uc0\u55357 \u56524 
\f1  Project Overview\
\pard\pardeftab720\partightenfactor0

\f3 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 This repository contains a robust Desktop Calculator application built in Python, featuring a fully functional Command Line Interface (CLI). More importantly, it demonstrates core software engineering practices by strictly separating business logic from the user interface and implementing comprehensive 
\f0\b Unit Testing
\f3\b0  using the 
\f0\b Pytest
\f3\b0  framework. \
\
This project serves as a practical demonstration of White-Box testing methodologies, input validation, and state management within a Python application.
\f1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
 
\f2 \uc0\u55357 \u56960 
\f1  Key Technical Features\
\pard\tx220\tx720\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\li720\fi-720\pardirnatural\partightenfactor0
\ls1\ilvl0
\f0\b \cf0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Separation of Concerns:
\f3\b0  Independent classes for core arithmetic logic (`Calculator`) and CLI routing (`CalculatorApp`). \
\ls1\ilvl0
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Defensive Programming:
\f3\b0  Strict input validation enforcing strictly numeric data types (`int`, `float`) before execution. \
\ls1\ilvl0
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Advanced Error Handling:
\f3\b0  Graceful exception catching for edge cases (e.g., Division by Zero, Square Root of Negative Numbers) preventing application crashes. \
\ls1\ilvl0
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 State Management:
\f3\b0  Built-in timestamped history tracking for all mathematical operations performed during a session. \
\ls1\ilvl0
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Automated Unit Testing:
\f3\b0  Full test suite covering positive paths, edge cases, and explicit exception assertions using `pytest.raises`.
\f1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
 
\f2 \uc0\u55357 \u57056 \u65039 
\f1  Technology Stack\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls2\ilvl0
\f4\b \cf0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Language
\f1\b0 : Python 3 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls3\ilvl0
\f4\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Testing Framework:
\f1\b0  Pytest  \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls4\ilvl0
\f4\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Architecture:
\f1\b0  Object-Oriented Programming (OOP)\kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \

\f2 \uc0\u55357 \u56514 
\f1  Repository Structure\
\pard\pardeftab720\partightenfactor0

\f3 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 desktop-calculator/ \
\uc0\u9500 \u9472 \u9472  main.py # Application entry point\
\uc0\u9500 \u9472 \u9472  calculator.py # Core calculation logic and application interface \
\uc0\u9500 \u9472 \u9472  test_operations.py # Automated unit test suite using Pytest\
\uc0\u9500 \u9472 \u9472  requirements.txt # Python dependencies list \
\uc0\u9492 \u9472 \u9472  README.md # Project documentation
\f1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \

\f2 \uc0\u9881 \u65039 
\f1  Installation & Setup\
\
1. Clone the repository:\
```bash\
   git clone https://github.com/vladzpop11/desktop-calculator-pytest.git\
   cd your-repo-name\
\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\cf0 2. Create virtual environment\expnd0\expndtw0\kerning0
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\ls5\ilvl0\cf0 \kerning1\expnd0\expndtw0 ```bash\expnd0\expndtw0\kerning0
\
\pard\pardeftab720\partightenfactor0
\cf0     python3 -m venv venv \
    source venv/bin/activate # On Windows use: venv\\Scripts\\activate\
\
3. Install Dependencies\
pip install -r requirements.txt\
\
\
\pard\pardeftab720\sa298\partightenfactor0

\f2 \cf0 \uc0\u55358 \u56810 
\f1  Running the Tests\
\pard\pardeftab720\partightenfactor0

\f3 \cf0 \outl0\strokewidth0 \strokec2 To launch the interactive calculator CLI: python main.py\
\
To run the automated Pytest suite: pytest tests/test_operations.py -v
\f1 \outl0\strokewidth0 \
\pard\pardeftab720\partightenfactor0

\f5\fs26 \cf0 \
\
}