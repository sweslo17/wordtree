#encoding=utf-8
from node import node
import jieba.posseg as pseg
import zhon.hanzi
import re
import jieba
import mysql.connector
import datetime
import config
import json

'''tree = node("grandmother", [
		node("daughter", [
			node("granddaughter"),
			node("grandson")]),
		node("son", [
			node("granddaughter"),
			node("grandson")]),
		node("abc")
		])'''
#tree = node('abc',[node('qwe'),node('def')])
#tree.addlist(['xyz','abc'])
#temp_node = tree.search('abc')
#temp_node.addnode('xyz')
#temp = tree.search('abc').addnode('xyz').addnode('xxx')
#print tree
def get_words_list(input_str):
	return jieba.cut(input_str)
#	pass

date = datetime.date.today()
yesterday = date - datetime.timedelta(days=1)
cnx = mysql.connector.connect(host=config.host,user=config.user,passwd=config.passwd,database=config.database)
cur = cnx.cursor()
cur.execute("SELECT content FROM news_data WHERE time>=%s AND time<%s LIMIT 9,1",(yesterday,date))
results = cur.fetchall()
root = node("root",[])
for row in results:
	#content = re.sub('[%s]' % zhon.hanzi.punctuation, " ", row[0])
	#content = re.sub('[%s]' % u'╱,〈〉《︰', " ", title)
	sentance_list = re.split('[%s]' % zhon.hanzi.punctuation,row[0])
	for sentance in sentance_list:
#		print sentance.strip().encode('utf-8')
		cur = root
		for word in get_words_list(sentance.strip()):
			if cur.level_search(word) is None:
				cur.addnode(word)
			cur = cur.level_search(word)
	break

#print json.dumps(root)
print root.jsonify()
			#print word.encode('utf-8')
#		print get_words_list(sentance.strip())

