Title: Apache Redirect Exception
Date: 2014-04-17 02:35
Tags: tech
Slug: apache-redirect-exception
Category: public
Summary: How to define redirect exceptions in apache
language: en_US

Tonight I had to define an exception to my <dfn title="The Apache HTTP Server">Apache</dfn> redirect rules. Since the ["planet" rss-aggregator of my university](http://planet.mafiasi.de) doesn't support <abbr title="Secure Sockets Layer">SSL</abbr> connections to fetch its feeds, I made an exception so that my <abbr title="Really Simple Syndication">RSS</abbr> feed is also [available via <abbr title="Hypertext Transfer Protocol">HTTP</abbr>](http://tim-kraemer.de/uni.rss). However if you explicitly use the <abbr title="HyperText Transfer Protocol Secure">HTTPS</abbr> protocol it should be [available via <abbr title="Secure Sockets Layer">SSL</abbr>](https://tim-kraemer.de/uni.rss) too.

This is the resulting apache virtual-host config:

```
<VirtualHost *:80>
	ServerName tim-kraemer.de
	[...]
	RedirectMatch permanent ^/(?!uni.rss$).* https://tim-kraemer.de/
	DocumentRoot /home/tim/www/
	<Directory />
		Require all granted
		[...]
	</Directory>
</VirtualHost>
```

The `RedirectMatch permanent` clause sends an <dfn title="The HTTP response status code 301 Moved Permanently is used for permanent redirection, meaning current links or records using the URL that the 301 Moved Permanently response is received for should be updated to the new URL provided in the Location field of the response.">HTTP 301 header</dfn>, to tell the client that the website is permanently redirected to the encrypted <abbr title="HyperText Transfer Protocol Secure">HTTPS</abbr> version. `^/(?!uni.rss$).*` is an <dfn title="In theoretical computer science and formal language theory, a regular expression (abbreviated regex or regexp) is a sequence of characters that forms a search pattern, mainly for use in pattern matching with strings, or string matching, i.e. &quot;find and replace&quot;-like operations. The concept arose in the 1950s, when the American mathematician Stephen Kleene formalized the description of a regular language, and came into common use with the Unix text processing utilities ed, an editor, and grep (global regular expression print), a filter.">regular-expression</dfn>, which matches on everything (and therefore redirects every url) except the url-part 'uni.rss', which is one of the adresses of my [RSS-feed](https://tim-kraemer.de/blog/feeds/all.rss).

