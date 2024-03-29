"""
Share Post
==========

This plugin adds share URL to article. These links are textual which means no
online tracking of your readers.
"""

from bs4 import BeautifulSoup
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote
from pelican import signals, contents


def article_title(content):
    main_title = BeautifulSoup(content.title, 'html.parser').prettify().strip()
    sub_title = ''
    if hasattr(content, 'subtitle'):
        sub_title = BeautifulSoup(content.subtitle, 'html.parser').prettify().strip()
    return quote(('%s %s' % (main_title, sub_title)).encode('utf-8'))


def article_url(content):
    site_url = content.settings['SITEURL']
    return quote(('%s/%s' % (site_url, content.url)).encode('utf-8'))


def article_summary(content):
    summary = BeautifulSoup(content.summary, 'html.parser').prettify().strip()
    return quote(('%s' % summary.encode('utf-8')))

def article_tags(content):
    tags = ','.join(str(v) for v in content.tags)
    return quote(tags)


def share_post(content):
    if isinstance(content, contents.Static):
        return
    title = article_title(content)
    url = article_url(content)
    summary = article_summary(content)
    tags = article_tags(content)

    tweet = '%s%%20%s' % (title, url)
    facebook_link = 'http://www.facebook.com/sharer/sharer.php?s=100' \
                    '&p[url]=%s&p[images][0]=&p[title]=%s&p[summary]=%s' \
                    % (url, title, summary)
    gplus_link = 'https://plus.google.com/share?url=%s' % url
    twitter_link = 'http://twitter.com/home?status=%s' % tweet
    mail_link = 'mailto:?subject=%s&amp;body=%s' % (title, url)
    flattr_link = 'https://flattr.com/submit/auto?user_id=TieKei&amp;url=%s&amp;title=%s&amp;description=%s&amp;language=de&amp;tags=%s&amp;category=text' % (url,title,summary,tags)

    share_links = {'twitter': twitter_link,
                   'facebook': facebook_link,
                   'google-plus': gplus_link,
                   'email': mail_link,
                   'flattr': flattr_link
                   }
    content.share_post = share_links


def register():
    signals.content_object_init.connect(share_post)
