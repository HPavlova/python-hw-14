# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from .db_config import engine
from .models import Quotes, Author, Base


class SpyderPipeline:
    def process_item(self, item, spider):
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        with session as db:
            if not db.query(Quotes).filter_by(text=item['text']).first():
                if item['author'] != 'Unknown':
                    author = db.query(Author).filter_by(name=item['author']).first()
                    if not author:
                        author = Author(name=item['author'])
                        db.add(author)
                        db.commit()
                        print('Author added to the database')
                author = db.query(Author).filter_by(name=item['author']).first()
                quotes = Quotes(id=item['id'], text=item['text'], author=item['author'])
                quotes.author.append(author)
                db.add(quotes)
                db.commit()
                print('Quotes added to the database')
        print('Item added to the database')
        return item
