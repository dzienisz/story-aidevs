# Mission 3 Solved (API)

## Flaga: `HACKED`

## Process
1.  **Analyzed Endpoints**: `/api-weryfikacja` (Questions) and `/api-wiedza/{query}` (Hints).
2.  **Identified Queries**: Extracted keywords from questions, handled URL encoding (especially for Polish characters like `Księżyc`).
3.  **Gathered Hints**: Used `gather.py` to prompt the knowledge base.
4.  **Built Answer DB**: Compiled a lookup table of correct answers.

## Answer Database
| Question Keyword | Answer |
|------------------|--------|
| Rights / Prawa | **2212** |
| Party / Partia | **Synthetix** |
| Software / Oprogramowanie | **Softo** |
| Professor / Podróże w czasie | **Profesor Maj** |
| Mars Colony / Niepodległość | **Tharsis** |
| President / Prezydent | **Jan Robotex** |
| Leader / Ruch | **Adam Persona** |
| Currency / Waluta | **Devcoin** |
| Hel-3 Corp / Megakorporacja | **Helthree** |
| Oil / Ropa | **2133** |

## Solution Script
Run `python solve.py` to automatically fetch questions, match against the DB, and submit the answers.
