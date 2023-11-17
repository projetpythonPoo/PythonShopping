from shopping.article import Article


class ArticleGenerator:
    @staticmethod
    def generate(amount_of_articles):
        articles = []
        for i in range(1, amount_of_articles + 1):
            articles.append(Article(i, "description" + str(i), i + 1 * i))
        return articles
