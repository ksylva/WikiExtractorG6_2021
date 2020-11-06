# Functional aspect

I. List of uri: wikiurl.txt

1. Retrieve URIs to form URLs  
2. Browse URLs to retrieve the table(s) (html format)  
3. Convert to CSV format  

1.Dictionary of urls: read the file ''wikiurls,txt'' and for each line, we will create a url.

|Key : uri (page name)|Value : ‘’https://en...’’|
|---|---|
|Comparison_between_Esperanto_and_Ido|https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido|
|Comparison_between_Esperanto_and_Interlingua|https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Interlingua|

2. Browse URLs to retrieve the table(s) (html format)  
a- Library: urllib  
b- Library : beautifulsoup  
* Dictionary of tables with for key: uri and for value: list of tables in the page  

|Key : uri|Value: list of tables|
|---|---|
|Comparison_between_Esperanto_and_Ido | ["\<table class="\wikitable">\</table>"\,"\<table class="\wikitable"\>\</table>\"\]|
|Comparison_between_Esperanto_and_Interlingua | ["\<table class="wikitable">\</table>"\,<table class="\wikitable\"\>\</table>\"\] |

3. Convert to CSV  
  a- Library : pandas
