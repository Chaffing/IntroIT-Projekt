
def correct_answer(answer: str  ,questions: dict,question: str): # tar in svar = str, dict = frågebateri och frågan ur den slumpade lsitan = str
    if answer.lower().strip() == questions[question].lower().strip():
        return True
    else:
        return False

def false_answer(answer, questions, question): # egentligen överflödig, kan lika gärna använda not correct_answer
    if not correct_answer(answer, questions, question):
        return True
    else:
        return False

