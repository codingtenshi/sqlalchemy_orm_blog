from session import session
from models import Author, Article


# def main():
#     for author in session.query(Author): # wyciągnęliśmy autora
#         print(author)

# wyciąganie artykułu
# def main():
#     articles = session.query(Article).filter_by(author_id=1)
#     for article in articles:
#         print(article)

def main():
    for author in session.query(Author): # wyciągnęliśmy wszystkich autorów
        articles = session.query(Article).filter_by(author_id=author.id)
        for article in articles:
            print(author, article)

# można to uprościć; mając autora


def main():
    for author in session.query(Author):
        for article in author.articles:
            print(author, article)


if __name__ == '__main__':
    main()