from faker import Faker

from session import session
from models import Author, Article


def main():
    author = session.query(Author).get(1)
    fake = Faker()
    article = Article(
        title=fake.sentence(),
        content='New Article content'
    )
    # relationship
    author.articles.append(article)  # dodaje art., który stworzyliśmy
    session.commit()  # wysyłamy dane do bazy danych


if __name__ == '__main__':
    main()