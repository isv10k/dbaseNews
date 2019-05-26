from sqlite_conn import SqliteConn


DB_PATH = 'dbase.sqlite'


def execute_query(query_string):
    """Executes query and returns data from data base"""
    with SqliteConn(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query_string)
        conn.commit()
        data = cursor.fetchall()
        if data:
            return data


def create_db():
    sql_create_users = '''
        CREATE TABLE IF NOT EXISTS
        Users(
            UsersId INTEGER PRIMARY KEY AUTOINCREMENT       NOT NULL,
            FirstName   TEXT(20)    NOT NULL,
            LastName    TEXT(20)    NOT NULL,
            Email       CHAR(50)
        );
    '''
    execute_query(sql_create_users)

    sql_create_subscriptions = '''
        CREATE TABLE IF NOT EXISTS
        Subscriptions(
            SubscriptionsId INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
            UserId      INTEGER     NOT NULL,
            CONSTRAINT subscriptions_users_fkey
                FOREIGN KEY (UserId)
                REFERENCES Users(UsersId)
        );
    '''
    execute_query(sql_create_subscriptions)

    sql_create_categories = '''
        CREATE TABLE IF NOT EXISTS
        Categories(
            CategoryId INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
            Name        TEXT(20)    NOT NULL
        );
    '''
    execute_query(sql_create_categories)

    sql_create_news = '''
        CREATE TABLE IF NOT EXISTS
        News(
            NewsId INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
            CategoryId      INTEGER     NOT NULL,
            Url             TEXT(100)   NOT NULL,
            CONSTRAINT news_categories_fkey
                FOREIGN KEY (CategoryId)
                REFERENCES Categories(CategoryId)
        );
    '''
    execute_query(sql_create_news)

    sql_create_subscriptions_line = '''
        CREATE TABLE IF NOT EXISTS
        SubscriptionsLine(
            SubscriptionsLineId INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
            SubscriptionId      INTEGER     NOT NULL,
            NewsId              INTEGER     NOT NULL,
            CONSTRAINT line_subscriptions_fkey
                FOREIGN KEY (SubscriptionId)
                REFERENCES Subscriptions(SubscriptionId),
            CONSTRAINT line_news_fkey
                FOREIGN KEY (NewsId)
                REFERENCES News(NewsId)
        );
    '''
    execute_query(sql_create_subscriptions_line)

    sql_create_keywords = '''
        CREATE TABLE IF NOT EXISTS
        Keywords(
            KeywordId INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
            Name        TEXT(20)    NOT NULL
        );
    '''
    execute_query(sql_create_keywords)

    sql_create_news_keywords = '''
        CREATE TABLE IF NOT EXISTS
        NewsKeywords(
            NewsKeywordsId INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
            KeywordId      INTEGER     NOT NULL,
            NewsId         INTEGER     NOT NULL,
            CONSTRAINT newskeywords_keywords_fkey
                FOREIGN KEY (KeywordId)
                REFERENCES Keywords(KeywordId),
            CONSTRAINT newskeywords_news_fkey
                FOREIGN KEY (NewsId)
                REFERENCES News(NewsId)
        );
    '''
    execute_query(sql_create_news_keywords)


if __name__ == '__main__':

    create_db()

