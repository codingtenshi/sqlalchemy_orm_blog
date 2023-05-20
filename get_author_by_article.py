from session import session
from models import Article, Author


def main():
    article = session.query(Article).get(1)
    print(article, article.author)


if __name__ == '__main__':
    main()