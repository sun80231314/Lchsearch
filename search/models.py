
# Create your models here.
from elasticsearch_dsl import DocType, Date, Completion, Keyword, Text, Integer
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])

# 伯乐在线文字类型
class JobboleType(DocType):
    title = Text(analyzer="ik_max_word")
    url = Keyword()
    url_object_id = Keyword()
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"
        doc_type = "article"

