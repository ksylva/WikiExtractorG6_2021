**Scraping tables on Wikipedia (2020-2021)**

This project is a school work intended for students in Master1 MIAGE classic of the ISTIC, University of Rennes1.

**Context of the project**

This work is a scaping of tables from the universal and multilingual encyclopedia, Wikipedia realized by the group6 of M1 MIAGE classic of the school year (2020-2021).
 
**Scraping Wikipedia?**

As its name suggests, in this project, we will be led to extract tables in Wikipedia pages.
    **Process**
    
      1. Go to Wikipedia pages through their URLs
      2. Collect and extract tables (simple or nested) 
      3. Resend their contents in files under CSV
      Note: We only process Wikipedia pages in HTML format.
      
**Objectives**

     *Make work simple and accessible to everyone with the python programming language
     *Develop scraping methods 
     *Test these methods
    
**Actual functionality**

The software takes a file (wikiurl.txt) containing a list of wikipedia page titles and processes each of them to get the HTML URL of the page with a https://en.wikipedia.org/wiki/ prefix. After testing the URL: it processes all the HTML code of each page and tries to extract as many tables as possible in CSV.
    
    - We only process tables marked as "class =" wikitable " ".
    
    - In the conversion to CSV, for a cell concerned by a collspan AND a rowspan at the same time, the pandas library breaks this merge and then copies the info on each row/column.
    
    - When we have a link in a table, we keep it after conversion, Also, for each image in a table, we gather the link of the image to put it in the concerned cell (instead of the image).
