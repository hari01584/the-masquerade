import people_also_ask

class SERP:
    def __init__(self):
        pass

    def answer(self, query, count=5, wordlen=100, max_retry=10):
        fault_retry = 0
        for question in people_also_ask.generate_related_questions(query):
            print("Parsing", question)
            print("-" * 80)
            ans = people_also_ask.get_answer(question)
            print(ans)
            print("-" * 80)
            # break


if __name__ == "__main__":
    serp = SERP()
    serp.answer("Livspace")