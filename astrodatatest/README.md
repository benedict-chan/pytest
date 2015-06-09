

### Examples 

http://www.astro.com/wiki/astro-databank/api.php?format=jsonfm&prop=revisions&rvprop=content&titles=Jobs%2C_Steve&action=raw&templates=expand
http://www.astro.com/wiki/astro-databank/api.php
http://www.astro.com/wiki/astro-databank/api.php?action=query&format=json&prop=revisions&rvprop=content&titles=Jobs%2C_Steve
http://www.astro.com/wiki/astro-databank/api.php?action=query&format=json&prop=revisions&rvprop=content&pageids=29562
http://www.astro.com/wiki/astro-databank/api.php?action=query&format=xml&prop=revisions&rvprop=content&titles=Jobs%2C_Steve
http://www.astro.com/wiki/astro-databank/api.php?format=jsonfm&action=parse&pageid=29562
http://www.astro.com/wiki/astro-databank/api.php?action=query&prop=revisions&rvprop=content&titles=Jobs%2C_Steve


#### Categories
http://www.astro.com/wiki/astro-databank/api.php?action=query&list=allcategories
accontinue="0050_deaths" 
http://www.astro.com/wiki/astro-databank/api.php?action=query&list=allcategories&accontinue=0050_deaths


#### Pages
http://www.astro.com/wiki/astro-databank/api.php?action=query&list=allpages
http://www.astro.com/wiki/astro-databank/api.php?action=query&list=allpages&aplimit=500
apcontinue
aplimit


### Templates

http://www.astro.com/astro-databank/Astro-Databank:Handbook_chapter_20
http://www.astro.com/astro-databank/Astro-Databank:Handbook_chapter_20#The_dma_template
http://www.astro.com/astro-databank/Template:Person


### References

http://www.mediawiki.org/wiki/API:Query


### Tools

http://en.wikipedia.org/wiki/Wikipedia:Creating_a_bot
https://blog.scraperwiki.com/2011/12/how-to-scrape-and-parse-wikipedia/
https://classic.scraperwiki.com/scrapers/wikipedia_utils/
https://classic.scraperwiki.com/editor/raw/wikipedia_utils
https://scraperwiki.com/scrapers/wikipedia_utils/edit/

https://github.com/scraperwiki/scraperwiki-python
https://classic.scraperwiki.com/docs/python/python_help_documentation/

https://bitbucket.org/ScraperWiki/scraperwiki-classic/wiki/Home

### ScraperWiki

scraperwiki.sqlite.execute("ALTER TABLE data ADD COLUMN processed bit default 0")
scraperwiki.sqlite.show_tables()

scraperwiki.sqlite.execute("UPDATE data SET processed = 1 WHERE page_id = %s" % page_id)
scraperwiki.sqlite.commit()


### Error page_id

<div style="display: none;">

Some sql scripts to use for analysis

```
SELECT  uc.category_id, count(*) as c, cat.scat, cat.CategoryNotes from user_category uc
inner join category cat on cat.category_id = uc.category_id
group by uc.category_id order by c desc
```



Phonegap?

npm update -g
npm install -g phonegap
npm install -g iconic
----npm install -g cordova ionic

</div>

